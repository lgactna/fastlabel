import datetime


def ez_to_aware_datetime(date_str: str) -> datetime.datetime:
    """
    Convert an Eric Zimmerman datetime to an aware datetime object, assumed to
    be UTC.
    """

    # KAPE uses 7 decimal places after the second, but %f is only 6
    # so we need to truncate the last digit
    date_str = date_str[:-1]

    return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f").astimezone(
        datetime.UTC
    )
