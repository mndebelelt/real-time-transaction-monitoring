from pydantic import BaseModel, Field
from datetime import datetime 

class TransactionEvent(BaseModel):
    transaction_id: str
    user_id: int
    card_id: str
    merchant: str 
    category: str
    amount: float = Field(gt=0)
    currency: str
    country: str
    city: str
    device_id: str