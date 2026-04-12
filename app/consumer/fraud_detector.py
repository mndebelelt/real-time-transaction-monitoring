import logging

from app.consumer.rules import is_high_amount


logger = logging.getLogger(__name__)


def evaluate_transaction(transaction: dict) -> list[dict]:
    alerts = []

    if is_high_amount(transaction["amount"]):
        alerts.append(
            {
                "rule_name": "high_amount",
                "reason": "Transaction amount exceeded threshold",
                "risk_score": 80,
            }
        )

    logger.info(
        "Evaluated transaction_id=%s alerts=%s",
        transaction["transaction_id"],
        len(alerts),
    )

    return alerts