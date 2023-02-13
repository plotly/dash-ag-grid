from selenium.webdriver.common.action_chains import ActionChains

from dash.testing.wait import until
from dash.testing.errors import TestingTimeoutError

# we use zero-based columns, but aria colindex is one-based
# so we need to add 1 in a lot of places

class Grid:
    def __init__(self, dash_duo, grid_id):
        self.dash_duo = dash_duo
        self.id = grid_id

    def get_header_cell(self, col):
        return self.dash_duo.find_element(
            f'#{self.id} [aria-rowindex="1"] .ag-header-cell[aria-colindex="{col + 1}"]'
        )

    def wait_for_header_text(self, col, expected):
        self.dash_duo.wait_for_text_to_equal(
            f'#{self.id} [aria-rowindex="1"] .ag-header-cell[aria-colindex="{col + 1}"] .ag-header-cell-text',
            expected
        )

    def wait_for_all_header_texts(self, expected):
        for col, val in enumerate(expected):
            self.wait_for_header_text(col, val)
        cols = len(self.dash_duo.find_elements(f'#{self.id} [aria-rowindex="1"] .ag-header-cell'))
        assert cols == len(expected)

    def _wait_for_count(self, selector, expected, description):
        try:
            until(lambda: len(self.dash_duo.find_elements(selector)) == expected, timeout=3)
        except TestingTimeoutError:
            els = self.dash_duo.find_elements(selector)
            raise ValueError(f"found {len(els)} {description}, expected {expected}")


    def wait_for_pinned_cols(self, expected):
        # TODO: is there a pinned right?
        self._wait_for_count(
            f'#{self.id} .ag-pinned-left-header [aria-rowindex="1"] .ag-header-cell',
            expected,
            "pinned_cols"
        )

    def wait_for_viewport_cols(self, expected):
        self._wait_for_count(
            f'#{self.id} .ag-header-viewport [aria-rowindex="1"] .ag-header-cell',
            expected,
            "viewport_cols"
        )

    def drag_col(self, from_index, to_index):
        from_col = self.get_header_cell(from_index)
        to_col = self.get_header_cell(to_index)
        (
            ActionChains(self.dash_duo.driver)
            .move_to_element(from_col)
            .click_and_hold()
            .move_to_location(
                to_col.location["x"] + to_col.size["width"] * 0.8,
                to_col.location["y"] + to_col.size["height"] * 0.5
            )
            .pause(0.5)
            .release()
        ).perform()

    def pin_col(self, col, pinned_cols=0):
        from_col = self.get_header_cell(col)
        pin_col = self.get_header_cell(pinned_cols)
        (
            ActionChains(self.dash_duo.driver)
            .move_to_element(from_col)
            .click_and_hold()
            .move_to_location(
                pin_col.location["x"] + pin_col.size["width"] * 0.1,
                pin_col.location["y"] + pin_col.size["height"] * 0.5
            )
            .pause(1)
            .release()
        ).perform()

    def wait_for_rendered_rows(self, expected):
        self._wait_for_count(f"#{self.id} .ag-row", expected, "rendered rows")

    def wait_for_cell_text(self, row, col, expected):
        self.dash_duo.wait_for_text_to_equal(
            f'#{self.id} .ag-row[row-index="{row}"] .ag-cell[aria-colindex="{col + 1}"]',
            expected
        )

    def set_filter(self, col, val):
        filter_input = self.dash_duo.find_element(
            f'#{self.id} .ag-floating-filter[aria-colindex="{col + 1}"] input'
        )
        self.dash_duo.clear_input(filter_input)
        filter_input.send_keys(val)
