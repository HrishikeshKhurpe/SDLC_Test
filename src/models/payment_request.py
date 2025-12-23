from dataclasses import dataclass
from typing import Optional

@dataclass
class PaymentRequest:
    customer_id: str
    amount: float
    payment_method: str
    currency: str = 'USD'
    description: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            'customer_id': self.customer_id,
            'amount': self.amount,
            'payment_method': self.payment_method,
            'currency': self.currency,
            'description': self.description
        }
