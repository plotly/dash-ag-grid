import pytest

from tests.utils import Grid


@pytest.mark.parametrize(
    "pin_state,expected_selector",
    [
        (
            "scrolling",
            '.ag-header [aria-rowindex="1"] .ag-grid-scrolling-cells, .ag-header-viewport [aria-rowindex="1"]',
        ),
        (
            "left",
            '.ag-header [aria-rowindex="1"] .ag-grid-pinned-left-cells, .ag-pinned-left-header [aria-rowindex="1"]',
        ),
        (
            "right",
            '.ag-header [aria-rowindex="1"] .ag-grid-pinned-right-cells, .ag-pinned-right-header [aria-rowindex="1"]',
        ),
    ],
)
def test_header_selector_for_pin_state(pin_state, expected_selector):
    grid = Grid(None, "grid")

    assert grid._header_selector_for_pin_state(pin_state) == expected_selector
