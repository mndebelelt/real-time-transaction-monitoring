import json
import logging

from confluent_kafka import Producer

from app.common.config import settings


logger = logging.getLogger(__name__)


class KafkaTransactionPublisher:

    def __init__(self) -> None:
        self.producer = Producer({
            "bootstrap.servers": settings.kafka_bootstrap_servers
        })
        self.topic = settings.kafka_transactions_topic


    def publish(self, message: dict) -> None:

        payload = json.dumps(message).encode("utf-8")

        self.producer.produce(self.topic, value=payload)

        self.producer.flush()

        logger.info("Published transaction to topic=%s", self.topic)