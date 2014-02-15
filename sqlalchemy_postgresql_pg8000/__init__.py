__version__ = '0.0.0'

from sqlalchemy.dialects import registry

registry.register(
    "postgresql", "sqlalchemy_postgresql_pg8000.pg8000",
    "PGDialect_pg8000")
registry.register(
    "postgresql.pg8000", "sqlalchemy_postgresql_pg8000.pg8000",
    "PGDialect_pg8000")
