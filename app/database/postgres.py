from pathlib import Path

from sqlalchemy import (
    create_engine,
    text
)

from sqlalchemy.orm import sessionmaker

from app.database.models import Base


class DatabaseManager:

    def __init__(self):

        self.database_path = (
            Path("data") /
            "auracart.db"
        )

        self.connection_string = (
            f"sqlite:///{self.database_path}"
        )

        self.engine = create_engine(
            self.connection_string,
            echo=False,
            future=True
        )

        self.SessionLocal = sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

    def create_database(self):

        Base.metadata.create_all(
            bind=self.engine
        )

    def get_session(self):

        return self.SessionLocal()

    def health_check(self):

        try:

            with self.engine.connect() as connection:

                connection.execute(
                    text("SELECT 1")
                )

            return True

        except Exception:

            return False

    def close(self):

        self.engine.dispose()


db_manager = DatabaseManager()