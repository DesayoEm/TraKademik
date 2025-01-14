from datetime import datetime, date
from sqlalchemy.orm import declared_attr
from uuid import UUID, uuid4

from pydantic import(
    BaseModel,
    Field,
    EmailStr
)

from typing import(
    Optional
)