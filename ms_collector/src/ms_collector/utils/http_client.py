import time

import httpx

from src.ms_collector.config import settings
from src.ms_collector.logger import get_logger
from src.ms_collector.schemas.additional_product_data_schema import (
    AdditionalProductDataSchema,
)
from src.ms_collector.schemas.main_product_data_schema import MainProductDataSchema


class HttpClient:
    def __init__(self) -> None:
        self.main_products_info_service_url = settings.net_video_service_url
        self.additional_products_info_service_url = settings.country_link_service_url

        self.request_retries = 3
        self.request_timeout = 30
        self.client = httpx.Client()

        self.logger = get_logger()

    @property
    def _headers(self) -> dict[str, str]:
        return {
            "Accept": "application/json",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate, br",
        }

    def _make_request(self, url: str, headers: dict = None) -> httpx.Response:
        for i in range(self.request_retries):
            try:
                response = self.client.get(url=url, headers=headers)
                if response.status_code == 200:
                    return response
            except httpx.ConnectError as connect_error:
                self.logger.error(
                    f"Connect error for url '{url}'. Error: {connect_error}"
                )
                time.sleep(self.request_timeout)
                if i == self.request_retries - 1:
                    raise httpx.ConnectError(
                        f"Failed connect to url '{url}' on '{i + 1}' try. Error: {connect_error}.'"
                    )
            except httpx.HTTPStatusError as http_status_error:
                self.logger.error(
                    f"Response error for url '{url}': {http_status_error}"
                )
                time.sleep(self.request_timeout)
                if i == self.request_retries - 1:
                    raise httpx.ConnectError(
                        f"Bad status code in url '{url}' on '{i + 1}' try. Error: {http_status_error}.'"
                    )
            except httpx.TimeoutException as timeout_error:
                self.logger.error(f"Timeout error for url '{url}': {timeout_error}")
                time.sleep(self.request_timeout)
                if i == self.request_retries - 1:
                    raise httpx.ConnectError(
                        f"Failed try '{i + 1}' to connect '{url}' with timeout "
                        f"'{self.request_timeout}'. Error: {timeout_error}.'",
                    )

    async def get_main_product_data_request(self) -> MainProductDataSchema:
        """Запрос для получения основной информации по товарам."""
        self.logger.debug(
            f"Send GET request to 'NetVideoData': '{self.main_products_info_service_url}'"
        )
        response = self._make_request(
            url=self.main_products_info_service_url, headers=self._headers
        )
        return MainProductDataSchema.model_validate(response.json())

    async def get_additional_product_data_request(self) -> AdditionalProductDataSchema:
        """Запрос для получения дополнительной информации по товарам."""
        self.logger.debug(
            f"Send GET request to 'CountryLink': '{self.additional_products_info_service_url}'"
        )
        response = self._make_request(
            url=self.additional_products_info_service_url, headers=self._headers
        )
        return AdditionalProductDataSchema.model_validate(response.json())
