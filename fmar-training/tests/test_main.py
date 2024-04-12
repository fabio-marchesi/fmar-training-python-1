from datetime import date

import pytest

from app.main import main


@pytest.mark.parametrize(
    "test_date",
    [
        date(2024, 1, 1),
        date(2020, 2, 2),
    ],
)
def test_main(test_date: date) -> None:
    def _date_provider() -> date:
        return test_date

    assert main(_date_provider=_date_provider) == test_date
