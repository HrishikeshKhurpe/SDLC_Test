from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class PaymentResponse:
    transaction_id: str
    status: str
    amount: float
    payment_method: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'PaymentResponse':
        return cls(
            transaction_id=data['transaction_id'],
            status=data['status'],
            amount=data['amount'],
            payment_method=data['payment_method']
        )
