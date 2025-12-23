from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentResponse:
    payment_id: str
    status: str
    amount: float
    currency: str
    message: Optional[str] = None
