from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentRequest:
    user_id: str
    amount: float
    currency: str
    payment_method: str
    card_number: Optional[str] = None
    expiry_date: Optional[str] = None
    cvv: Optional[str] = None

    def is_valid(self) -> bool:
        return self.amount > 0 and self.currency and self.payment_method
