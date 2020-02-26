from random import randrange
from datetime import timedelta
from datetime import datetime


def random_birthday():
    """
    This function will return a random datetime between two datetime objects.
    """
    now = datetime.now()
    seconds_in_year = 24*60*60*365
    start = now - timedelta(seconds=seconds_in_year*100)
    end = now - timedelta(seconds=seconds_in_year*18)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return datetime.date(start + timedelta(seconds=random_second))
