from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import uuid4

@dataclass
class Transaction:
    id: str = field(default_factory=lambda: str(uuid4()))
    src_account_id: Optional[str] = None
    dst_account_id: Optional[str] = None
    amount_minor: int = 0
    type: str = "TRANSFER"  # DEPOSIT, WITHDRAWAL, TRANSFER
    created_at: datetime = field(default_factory=datetime.utcnow)
    status: str = "POSTED"

    def is_valid(self) -> bool:
        return self.amount_minor > 0 and self.status in {"POSTED", "FAILED", "PENDING"}