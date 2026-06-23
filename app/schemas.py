from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ApplicationCreate(BaseModel):
    company: str
    role: str
    status: str = "applied"
    notes: Optional[str] = None


class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    date_applied: datetime
    notes: Optional[str] = None

    model_config = {"from_attributes": True}
