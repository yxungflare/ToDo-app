import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(
        unique=True, primary_key=True
    )
    task_name: Mapped[str] = mapped_column(
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        nullable=False, default=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), unique=False
    )
    creation_date: Mapped[datetime.datetime] = mapped_column(
        nullable=True, default=datetime.datetime.utcnow()
    )