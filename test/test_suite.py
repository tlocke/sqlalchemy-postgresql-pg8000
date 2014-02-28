from sqlalchemy.testing.suite import *
from nose.plugins.skip import SkipTest

class NumericTest(NumericTest):

    # Skip this test as it fails under PyPy because it doesn't implicitly
    # cast a Decimal to a float.
    def test_numeric_as_float(self):
        raise SkipTest

    # Skip this test as it fails under PyPy because it doesn't implicitly
    # cast a Decimal to a float.
    def test_numeric_as_decimal(self):
        raise SkipTest
