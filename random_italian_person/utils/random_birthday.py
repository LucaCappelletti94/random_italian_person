from random import randrange
from datetime import timedelta
from datetime import datetime


def random_birthday():
    """
    This function will return a random datetime between two datetime objects.
    """
    start = datetime.now() - timedelta(seconds=24*60*60*365*100)
    end = datetime.now() - timedelta(seconds=24*60*60*365*18)
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return datetime.date(start + timedelta(seconds=random_second))
