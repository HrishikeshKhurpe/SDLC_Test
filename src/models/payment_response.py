from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentResponse:
    transaction_id: str
    status: str
    amount: float
    currency: str
    payment_method: str
    customer_id: str
    description: Optional[str] = None
