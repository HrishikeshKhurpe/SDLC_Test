from dataclasses import dataclass

@dataclass
class PaymentResponse:
    transaction_id: str
    status: str
    amount: float
    currency: str
