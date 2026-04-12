from random import choice, uniform, randint
from datetime import datetime, UTC

from app.common.utils import generate_uuid
from app.producer.schemas import TransactionEvent


MERCHANTS = [
    ("Amazon", "online_retail"),
    ("Takealot", "online_retail"),
    ("Uber", "transport"),
    ("Checkers", "groceries"),
    ("Shell", "fuel"),
    ("Airbnb", "travel"),
]

COUNTRIES = {
    "ZA": ["Johannesburg", "Cape Town", "Durban", "Pretoria"],
    "GB": ["London", "Manchester"],
    "US": ["New York", "Austin"],
}


def generate_transaction() -> TransactionEvent:
    country = choice(list(COUNTRIES.keys()))
    city = choice(COUNTRIES[country])
    merchant, category = choice(MERCHANTS)

    return TransactionEvent(
        transaction_id=generate_uuid(),
        user_id=randint(1000, 1020),
        card_id=f"CARD_{randint(1, 50):03}",
        merchant=merchant,
        category=category,
        amount=round(uniform(50, 15000), 2),
        currency="ZAR",
        country=country,
        city=city,
        device_id=f"DEVICE_{randint(1, 100):03}",
        timestamp=datetime.now(UTC),
    )