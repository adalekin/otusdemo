import os

from alembic import command
from alembic.config import Config

from products import settings

ALEMBIC_CONFIG = Config(f"{os.path.dirname(os.path.abspath(__file__))}/alembic.ini")
ALEMBIC_CONFIG.set_main_option("sqlalchemy.url", settings.SQLALCHEMY_DATABASE_URI)


def upgrade():
    command.upgrade(ALEMBIC_CONFIG, "head")


def downgrade():
    command.downgrade(ALEMBIC_CONFIG, "base")


def main():
    upgrade()


if __name__ == "__main__":
    main()
