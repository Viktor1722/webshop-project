import sys
import os

from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
from alembic import context

# Import your Base from models.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from database.models import Base  # Ensure this path is correct

# Load the Alembic configuration
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Set target metadata to the Base from your models
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
