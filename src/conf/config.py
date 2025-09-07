"""
Configuration module for database connection.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Configuration class for database settings.
    """

    DB_URL = (
        "postgresql+asyncpg://"
        f"{os.getenv('POSTGRES_USER')}:"
        f"{os.getenv('POSTGRES_PASSWORD')}@"
        "localhost:5432/"
        f"{os.getenv('POSTGRES_DB')}"
    )

    def get_db_url(self):
        """
        Returns the database URL.
        """
        return self.DB_URL

    def is_configured(self):
        """
        Checks if all required environment variables are set.
        """
        return all(
            [
                os.getenv("POSTGRES_USER"),
                os.getenv("POSTGRES_PASSWORD"),
                os.getenv("POSTGRES_DB"),
            ]
        )


config = Config
