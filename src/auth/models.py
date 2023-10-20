import datetime

from sqlalchemy import JSON, TIMESTAMP, Boolean, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(
        Integer, unique=True, primary_key=True
    )
    name: Mapped[str] = mapped_column(
        String(length=150), nullable=False
    )
    permission: Mapped[TIMESTAMP] = mapped_column(
        JSON, nullable=False
    )


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(
        Integer, unique=True, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=150), unique=True, nullable=False
    )
    registreted_date: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP, default=datetime.datetime.utcnow
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('role.id'), default=0
    )
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )