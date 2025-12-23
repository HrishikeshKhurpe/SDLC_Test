from dataclasses import dataclass
from decimal import Decimal
from typing import Optional

@dataclass
class PaymentResponse:
    success: bool
    transaction_id: Optional[str] = None
    amount: Optional[Decimal] = None
    currency: Optional[str] = None
    error_message: Optional[str] = None
