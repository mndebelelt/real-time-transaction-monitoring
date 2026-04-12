
import os
from dataclasses import dataclass
from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    kafka_bootstrap_servers: str = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
    kafka_transactions_topic: str = os.getenv("KAFKA_TRANSACTIONS_TOPIC", "transactions")
    kafka_alerts_topic: str = os.getenv("KAFKA_ALERTS_TOPIC", "fraud_alerts")
    kafka_consumer_group: str = os.getenv("KAFKA_CONSUMER_GROUP", "transaction-monitor-group")

    postgres_host: str = os.getenv("POSTGRES_HOST", "localhost")
    postgres_port: int = int(os.getenv("POSTGRES_PORT", "5432"))
    postgres_db: str = os.getenv("POSTGRES_DB", "transaction_monitoring")
    postgres_user: str = os.getenv("POSTGRES_USER", "postgres")
    postgres_password: str = os.getenv("POSTGRES_PASSWORD", "postgres")

    app_env: str = os.getenv("APP_ENV", "local")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")

    high_amount_threshold: float = float(os.getenv("HIGH_AMOUNT_THRESHOLD", "10000"))
    velocity_window_seconds: int = int(os.getenv("VELOCITY_WINDOW_SECONDS", "60"))
    velocity_transaction_count: int = int(os.getenv("VELOCITY_TRANSACTION_COUNT", "5"))
    country_jump_window_seconds: int = int(os.getenv("COUNTRY_JUMP_WINDOW_SECONDS", "300"))


settings = Settings()