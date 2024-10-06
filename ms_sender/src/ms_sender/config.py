from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str

    rmq_host: str
    rmq_port: int
    rmq_user: str
    rmq_password: str
    rmq_vhost: str

    log_level: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def broker_url(self) -> str:
        return f"amqp://{self.rmq_user}:{self.rmq_password}@localhost/{self.rmq_vhost}"


settings = Settings()
