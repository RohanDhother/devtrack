from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ApplicationCreate(BaseModel):
    company: str = Field(min_length=1, max_length=100)
    role: str = Field(min_length=1, max_length=100)
    status: str = Field(default="applied", pattern="^(applied|interviewing|offer|rejected)$")
    notes: Optional[str] = Field(default=None, max_length=1000)


class ApplicationUpdate(BaseModel):
    company: Optional[str] = Field(default=None, min_length=1, max_length=100)
    role: Optional[str] = Field(default=None, min_length=1, max_length=100)
    status: Optional[str] = Field(default=None, pattern="^(applied|interviewing|offer|rejected)$")
    notes: Optional[str] = Field(default=None, max_length=1000)


class ApplicationResponse(BaseModel):
    id: int
    company: str
    role: str
    status: str
    date_applied: datetime
    notes: Optional[str] = None

    model_config = {"from_attributes": True}
