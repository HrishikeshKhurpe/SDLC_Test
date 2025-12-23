from dataclasses import dataclass
from typing import Dict

@dataclass
class PaymentRequest:
    customer_id: str
    amount: float
    payment_method: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            'customer_id': self.customer_id,
            'amount': self.amount,
            'payment_method': self.payment_method
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaymentRequest':
        return cls(
            customer_id=data['customer_id'],
            amount=data['amount'],
            payment_method=data['payment_method']
        )
