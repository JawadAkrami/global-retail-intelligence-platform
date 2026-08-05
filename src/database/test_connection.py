

from sqlalchemy import text

from src.database.connection import engine

with engine.connect() as conn:

    version = conn.execute(
        text("SELECT VERSION();")
    )

    print(version.fetchone()[0])