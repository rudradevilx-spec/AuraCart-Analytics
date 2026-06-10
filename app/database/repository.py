from datetime import datetime

from requests import session
from sqlalchemy.exc import SQLAlchemyError

from app.database.models import (
    Product,
    ScrapeSession
)

from app.database.postgres import (
    db_manager
)


class ProductRepository:

    def get_products_by_url(
        self,
        source_url
    ):

        session = db_manager.get_session()

        try:

            return (
                session.query(Product)
                .filter(
                    Product.source_url == source_url
                )
                .all()
            )

        finally:

            session.close()

    def add_product(
        self,
        name,
        price,
        rating,
        availability,
        source_url
    ):

        session = db_manager.get_session()

        try:

            product = Product(
                name=name,
                price=price,
                rating=rating,
                availability=availability,
                source_url=source_url
            )

            session.add(product)

            session.commit()

            session.refresh(product)

            return product

        except SQLAlchemyError:

            session.rollback()
            raise

        finally:

            session.close()

    def get_all_products(self):

        session = db_manager.get_session()

        try:

            return (
                session.query(Product)
                .order_by(
                    Product.id.desc()
                )
                .all()
            )

        finally:

            session.close()

    def delete_all_products(self):

        session = db_manager.get_session()

        try:

            session.query(Product).delete()

            session.commit()

        finally:

            session.close()

    def get_product_count(self):

        session = db_manager.get_session()

        try:

            return (
                session.query(Product)
                .count()
            )

        finally:

            session.close()

    def total_products(self):

        session = db_manager.get_session()

        try:

            return (
                session.query(Product)
                .count()
            )

        finally:

            session.close()
    def get_latest_products(
        self,
        limit=100
    ):

        session = db_manager.get_session()

        try:

            return (
                session.query(Product)
                .order_by(
                    Product.scraped_at.desc()
                )
                .limit(limit)
                .all()
            )

        finally:

            session.close()

    def delete_product(
        self,
        product_id
    ):

        session = db_manager.get_session()

        try:

            product = (
                session.query(Product)
                .filter(
                    Product.id == product_id
                )
                .first()
            )

            if product:

                session.delete(product)

                session.commit()

                return True

            return False

        except SQLAlchemyError:

            session.rollback()

            raise

        finally:

            session.close()

from datetime import datetime

from app.database.models import ScrapeSession
from app.database.postgres import db_manager


class SessionRepository:

    def create_session(
        self,
        target_url
    ):

        session = db_manager.get_session()

        try:

            scrape_session = ScrapeSession(
                target_url=target_url
            )

            session.add(scrape_session)

            session.commit()

            session.refresh(
                scrape_session
            )

            return scrape_session

        finally:

            session.close()

    def finish_session(
        self,
        session_id,
        product_count
    ):

        session = db_manager.get_session()

        try:

            scrape_session = (
                session.query(
                    ScrapeSession
                )
                .filter(
                    ScrapeSession.id == session_id
                )
                .first()
            )

            if scrape_session:

                scrape_session.completed_at = (
                    datetime.utcnow()
                )

                scrape_session.products_found = (
                    product_count
                )

                scrape_session.status = (
                    "Completed"
                )

                duration = (
                    scrape_session.completed_at
                    -
                    scrape_session.started_at
                )

                scrape_session.duration_seconds = (
                    duration.total_seconds()
                )

                session.commit()

        finally:

            session.close()

    def get_sessions(self):

        session = db_manager.get_session()

        try:

            return (
                session.query(
                    ScrapeSession
                )
                .order_by(
                    ScrapeSession.id.desc()
                )
                .all()
            )

        finally:

            session.close()

    def total_sessions(self):

        session = db_manager.get_session()

        try:

            return (
                session.query(
                    ScrapeSession
                )
                .count()
            )

        finally:

            session.close()