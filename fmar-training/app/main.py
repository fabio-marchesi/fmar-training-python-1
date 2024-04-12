from datetime import date, datetime
from typing import Callable


def main(_date_provider: Callable[[], date] = datetime.today) -> date:
    """
    Program that prints a date and time.
    :param _date_provider: callable that returns a date and time
    :return: the current date
    """

    current_date = _date_provider()
    print(f"Hello, World! Today is {str(current_date.strftime('%Y-%m-%d'))} 📆")
    return current_date


if __name__ == "__main__":
    main()
