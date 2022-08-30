from panther_config import detection, testing, PantherEvent

from panther_content.filters import examples


class TestExampleFilters(testing.PantherPythonFilterTestCase):
    def test_always_true(self) -> None:
        f = examples.always_true()

        self.assertIsInstance(f, detection.PythonFilter)
        self.assertFilterIsValid(f)

        self.assertFilterMatches(f, PantherEvent({}))

    def test_is_close_to_pi(self) -> None:
        f = examples.is_close_to_pi("num")

        self.assertIsInstance(f, detection.PythonFilter)
        self.assertFilterIsValid(f)

        self.assertFilterMatches(f, PantherEvent({"num": 3.14}))
        self.assertFilterNotMatches(f, PantherEvent({"num": 4.13}))
