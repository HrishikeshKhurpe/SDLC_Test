from dataclasses import dataclass
from decimal import Decimal

@dataclass
class PaymentRequest:
    amount: Decimal
    currency: str
    card_number: str
    expiry_date: str
    cvv: str
    customer_name: str
