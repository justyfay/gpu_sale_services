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

    redis_host: str
    redis_port: int

    log_level: str

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def rmq_url(self) -> str:
        return f"amqp://{self.rmq_user}:{self.rmq_password}@{self.rmq_host}/{self.rmq_vhost}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.redis_host}:{self.redis_port}"


settings = Settings()
