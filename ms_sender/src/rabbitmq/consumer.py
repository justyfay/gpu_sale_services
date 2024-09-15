import json
from typing import Dict

import pika

from config import settings
from src.logger import get_logger
from src.schemas.messages.rmq_product_schema import RmqProductSchema

logger = get_logger()


class Consumer:
    def __init__(self):
        """Инициализация переменных для подключения к RMQ."""
        self.rmq_user = settings.rmq_user
        self.rmq_password = settings.rmq_password
        self.rmq_host = settings.rmq_host
        self.rmq_port = settings.rmq_port
        self.current_queue = "product_events"
        self.credentials = pika.PlainCredentials(self.rmq_user, self.rmq_password)
        self.connection_parameters = pika.ConnectionParameters(
            host=self.rmq_host,
            port=self.rmq_port,
            credentials=self.credentials,
            virtual_host=settings.rmq_vhost,
        )
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()

    async def get_messages(self) -> RmqProductSchema | None:
        """Получение всех сообщений из очереди."""
        method_frame, header_frame, body = self.channel.basic_get(self.current_queue)
        if method_frame:
            message: Dict = json.loads(body.decode())
            logger.debug(f"Get messages from queue: {message}")
            self.channel.basic_ack(method_frame.delivery_tag)
            return RmqProductSchema.model_validate(message)
        else:
            logger.warning("No message returned.")
