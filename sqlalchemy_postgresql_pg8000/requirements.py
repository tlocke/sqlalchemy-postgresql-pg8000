from sqlalchemy.testing.requirements import SuiteRequirements
from sqlalchemy.testing import exclusions

class Requirements(SuiteRequirements):

    @property
    def reflects_pk_names(self):
        return exclusions.open()

    @property
    def reflects_pk_names(self):
        return exclusions.open()

    @property
    def floats_to_four_decimals(self):
        """target backend can return a floating-point number with four
            significant digits (such as 15.7563) accurately
            (i.e. without FP inaccuracies, such as 15.75629997253418).

        """
        return exclusions.closed()
