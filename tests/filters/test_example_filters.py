from panther_sdk import PantherEvent, detection, testing

from panther_content import custom


class TestExampleFilters(testing.PantherPythonFilterTestCase):
    def test_always_true(self) -> None:
        f = custom.filters.always_true()

        self.assertFilterIsValid(f)

        self.assertFilterMatches(f, PantherEvent({}))

    def test_is_close_to_pi(self) -> None:
        f = custom.filters.is_close_to_pi("num")

        self.assertFilterIsValid(f)

        self.assertFilterMatches(f, PantherEvent({"num": 3.14}))
        self.assertFilterNotMatches(f, PantherEvent({"num": 4.13}))
