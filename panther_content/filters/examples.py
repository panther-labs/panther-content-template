from panther_config import detection, PantherEvent

__all__ = ["always_true", "is_close_to_pi"]


# Simple custom filter definition
def always_true() -> detection.PythonFilter:
    def _always_true(event: PantherEvent) -> bool:
        return True

    return detection.PythonFilter(func=_always_true)


# Custom filter using standard library
def is_close_to_pi(key: str) -> detection.PythonFilter:
    def _is_close_to_pi(event: PantherEvent) -> bool:
        from math import isclose, pi

        val = event.get(key, 0)
        return isclose(val, pi, rel_tol=0.01)

    return detection.PythonFilter(func=_is_close_to_pi)
