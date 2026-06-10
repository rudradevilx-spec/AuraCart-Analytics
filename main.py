from pathlib import Path

from app.database.postgres import db_manager
from app.database.repository import ProductRepository
from app.gui.main_window import AuraCartMainWindow


# ---------------- DIRECTORY BOOTSTRAP ---------------- #

def ensure_directories():

    directories = [
        "data",
        "exports",
        "logs",
        "assets"
    ]

    for directory in directories:

        Path(directory).mkdir(
            parents=True,
            exist_ok=True
        )


# ---------------- STARTUP LOGIC ---------------- #

def startup():

    ensure_directories()

    print("\n🚀 Starting AuraCart Analytics Pro...\n")

    db_manager.create_database()

    if not db_manager.health_check():

        raise RuntimeError(
            "❌ Database connection failed. Please check PostgreSQL setup."
        )

    print("✅ Database initialized successfully.")

    try:

        repo = ProductRepository()

        count = repo.get_product_count()

        print(
            f"📦 Products currently stored: {count}"
        )

    except Exception as e:

        print(f"⚠️ Repository warning: {e}")


# ---------------- MAIN ENTRY ---------------- #

def main():

    try:

        startup()

        app = AuraCartMainWindow()
        app.run()

    except Exception as error:

        print(f"\n❌ Fatal Error: {error}")


if __name__ == "__main__":
    main()