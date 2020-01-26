from math import floor
import datetime
from datetime import timedelta

def add(moment):
    """add a gigasecond (1,000,000,000 seconds) to a datetime object

    Parameters:
    moment (datetime): Start Date

    Returns:
    datetime: Original date + 1 gigasecond
    """
    
    # Check input is valid
    if type(moment) is not datetime.datetime:
        raise(TypeError)

    # Calculate what a gigasecond actually is.
    # This could be stored just as the values, but it's computationally cheap
    # and costs nothing to show our working.
    gigasecond_days = floor(1E9 / (60 * 60 * 24))
    gigasecond_seconds = 1E9 - gigasecond_days * 24 * 60 * 60

    # Use the timedelta object to add the change in time onto the input
    moment_plus_gigasecond = moment + timedelta(days = gigasecond_days, seconds = gigasecond_seconds)
    
    return moment_plus_gigasecond