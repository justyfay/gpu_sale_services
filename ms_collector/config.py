from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    net_video_service_url: str
    country_link_service_url: str

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str

    log_level: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_host}:{self.db_port}/{self.db_name}"


class CelerySettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    rmq_user: str
    rmq_password: str
    rmq_vhost: str

    default_exchange_name: str
    default_queue_name: str
    default_routing_key: str

    product_events_queue_name: str
    product_events_routing_key: str

    @property
    def broker_url(self) -> str:
        return f"amqp://{self.rmq_user}:{self.rmq_password}@localhost/{self.rmq_vhost}"


settings = Settings()
celery_settings = CelerySettings()
