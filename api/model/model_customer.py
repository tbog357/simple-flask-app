from dataclasses import dataclass, field
from datetime import datetime

# local import
from api.model.model_base import ModelBase


@dataclass
class ModelCustomer(ModelBase):
    id: str = field(default=None)
    email: str = field(default=None)
    phone: str = field(default=None)
    address: str = field(default=None)
    name: str = field(default=None)
    status: str = field(default=None)
    created_at: datetime = field(default=None)
    updated_at: datetime = field(default=None)
