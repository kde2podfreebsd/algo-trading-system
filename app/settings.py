import os

from envparse import Env

env = Env()

basedir = os.path.abspath(os.path.dirname(__file__))

REAL_DATABASE_URL = env.str(
    "REAL_DATABASE_URL",
    default="postgresql+asyncpg://postgres:postgres@192.168.144.2:5432/postgres",
)  # connect string for the real database

TEST_DATABASE_URL = env.str(
    "TEST_DATABASE_URL",
    default="postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test",
)  # connect string for the test database
