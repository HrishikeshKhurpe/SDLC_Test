from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentRequest:
    customer_id: str
    amount: float
    currency: str
    payment_method: str
    description: Optional[str] = None
