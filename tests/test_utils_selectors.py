import pytest

from tests.utils import Grid


@pytest.mark.parametrize(
    "pin_state,expected_selector",
    [
        ("scrolling", ".ag-header"),
        ("left", ".ag-header .ag-grid-pinned-left-cells"),
        ("right", ".ag-header .ag-grid-pinned-right-cells"),
    ],
)
def test_header_selector_for_pin_state(pin_state, expected_selector):
    grid = Grid(None, "grid")

    assert grid._header_selector_for_pin_state(pin_state) == expected_selector

