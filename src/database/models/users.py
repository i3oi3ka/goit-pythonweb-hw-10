from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from pydantic import EmailStr

from src.database.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[EmailStr] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
