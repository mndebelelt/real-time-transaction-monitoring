import json
import logging

from confluent_kafka import Consumer

from app.common.config import settings
from app.common.logging_config import configure_logging


logger = logging.getLogger(__name__)


def run_consumer():

    consumer = Consumer({
        "bootstrap.servers": settings.kafka_bootstrap_servers,
        "group.id": settings.kafka_consumer_group,
        "auto.offset.reset": "earliest",
    })

    consumer.subscribe([settings.kafka_transactions_topic])

    logger.info("Starting Kafka consumer...")

    while True:

        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            logger.error("Consumer error: %s", msg.error())
            continue

        transaction = json.loads(msg.value().decode("utf-8"))

        logger.info(
            "Consumed transaction id=%s amount=%s merchant=%s",
            transaction["transaction_id"],
            transaction["amount"],
            transaction["merchant"],
        )
        
        
if __name__ == "__main__":
    configure_logging(settings.log_level)
    run_consumer()