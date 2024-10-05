from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime
from typing import Optional
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from src.database import BaseModel


class Message(BaseModel):
    uuid: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid4,
    )
    role: Mapped[str | None] = mapped_column(String(100), nullable=True)
    content: Mapped[str] = mapped_column(String(6000))
    tokens: Mapped[int] = mapped_column(Integer)
    date: Mapped[DateTime] = mapped_column(DateTime)
    chat_uuid: Mapped[UUID] = mapped_column(
        ForeignKey(
            "chat.uuid",
            ondelete="CASCADE",
        )
    )


class Chat(BaseModel):
    uuid: Mapped[UUID] = mapped_column(
        UUID,
        primary_key=True,
        unique=True,
        default=uuid4,
    )
    name: Mapped[str] = mapped_column(String(100))
    tokens: Mapped[int] = mapped_column(Integer)
    messages: Mapped[list["Message"]] = relationship(lazy="joined")
    project_uuid: Mapped[Optional[UUID]] = mapped_column(ForeignKey("project.uuid"))
