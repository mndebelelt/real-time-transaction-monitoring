import time
import logging

from app.common.config import settings
from app.common.logging_config import configure_logging
from app.producer.transaction_generator import generate_transaction
from app.producer.publisher import KafkaTransactionPublisher


logger = logging.getLogger(__name__)


def run_producer() -> None:
    publisher = KafkaTransactionPublisher()

    logger.info("Starting transaction producer...")

    while True:
        transaction = generate_transaction()

        publisher.publish(transaction.model_dump())

        logger.info(
            "Produced transaction id=%s amount=%s merchant=%s",
            transaction.transaction_id,
            transaction.amount,
            transaction.merchant,
        )

        time.sleep(1)


if __name__ == "__main__":
    configure_logging(settings.log_level)
    run_producer()