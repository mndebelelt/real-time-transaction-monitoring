import logging

from app.common.config import settings
from app.common.logging_config import configure_logging
from app.producer.transaction_generator import generate_transaction


def main() -> None:
    configure_logging(settings.log_level)
    logger = logging.getLogger(__name__)

    transaction = generate_transaction()
    logger.info("Generated sample transaction: %s", transaction.model_dump())


if __name__ == "__main__":
    main()