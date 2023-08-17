from pandas import Timestamp


def get_trading_sessions(timeStamp, timeFrame):
    hour = timeStamp.hour
    adjusted_hour = (hour + (timeFrame - 1)) % 24
    print(hour, adjusted_hour)

    asian_open = 3
    asian_close = 11
    london_open = 10
    london_close = 18
    newyork_open = 15
    newyork_close = 23

    asian_session = 1 if asian_open <= hour <= asian_close or asian_open <= adjusted_hour <= asian_close else 0
    london_session = 1 if london_open <= hour <= london_close or london_open <= adjusted_hour <= london_close else 0
    newyork_session = 1 if newyork_open <= hour <= newyork_close or newyork_open <= adjusted_hour <= newyork_close else 0

    if asian_session == 1 and london_session == 1:
        asian_session = 0
        london_session = 0
        asian_london_session = 1
    else:
        asian_london_session = 0

    if london_session == 1 and newyork_session == 1:
        london_newyork_session = 1
        london_session = 0
        newyork_session = 0

    else:
        london_newyork_session = 0

    print(asian_session, asian_london_session, london_session, london_newyork_session, newyork_session)


get_trading_sessions(Timestamp('2023-12-3 20:00'), 4)
