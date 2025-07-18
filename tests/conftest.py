import os
import pytest


@pytest.fixture
def enforced_locale():
    # Forces Chrome to use the `en-US` locale for tests, overriding any user-specified locale
    os.environ["LANGUAGE"] = "en-US"
