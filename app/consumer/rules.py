from app.common.config import settings


def is_high_amount(amount: float) -> bool:
    return amount > settings.high_amount_threshold