from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    Text
)

from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Product(Base):

    __tablename__ = "products"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(500),
        nullable=False
    )

    price = Column(
        String(100),
        nullable=True
    )

    rating = Column(
        String(50),
        nullable=True
    )

    availability = Column(
        String(100),
        nullable=True
    )

    source_url = Column(
        Text,
        nullable=False
    )

    scraped_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):

        return (
            f"<Product("
            f"id={self.id}, "
            f"name='{self.name}'"
            f")>"
        )


class ScrapeSession(Base):

    __tablename__ = "scrape_sessions"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    target_url = Column(
        Text,
        nullable=False
    )

    started_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )

    status = Column(
        String(50),
        default="Running"
    )

    products_found = Column(
        Integer,
        default=0
    )

    duration_seconds = Column(
        Float,
        nullable=True
    )

    def __repr__(self):

        return (
            f"<ScrapeSession("
            f"id={self.id}, "
            f"status='{self.status}'"
            f")>"
        )