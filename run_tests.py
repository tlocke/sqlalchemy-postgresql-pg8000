from sqlalchemy.dialects import registry

registry.register(
    "postgresql", "sqlalchemy_postgresql_pg8000.pg8000",
    "PostgreSQLDialect_pg8000")
registry.register("postgres.pg8000", "sqlalchemy_postgresql_pg8000.pg8000",
    "PostgreSQLDialect_pg8000")

from sqlalchemy.testing import runner

# use this in setup.py 'test_suite':
# test_suite="run_tests.setup_py_test"
def setup_py_test():
    runner.setup_py_test()

if __name__ == '__main__':
    runner.main()

