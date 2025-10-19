'''
Given tz_from, tz_to, start and duration, return a boolean that answers this question:

"Was the package received the day before it was sent?"
Details
Time zones are represented by integers -11 to +12 inclusive (including zero), one zone per hour for a total of 24 zones in one day. This simplification ignores zones below -11 and above +12, 30- and 45-minute offsets, daylight savings, and time folds.

A package is sent between two time zones: tz_from and tz_to, initiated at local hour start (integer between 0 to 23, 24hr clock). The delivery takes duration hours to complete (integer between 0 to 24, inclusive).

Examples
Eg 1.
Given tz_from=3, tz_to=0, start=13, duration=1, return False. A package sent at 13:00 from time zone 3 takes 1 hour to be delivered to time zone 0. The package is received at 11:00 local time, the same day it was sent. Return "False" as it was not received the day before it was sent.

Eg 2.
Given tz_from=12, tz_to=-3, start=5, duration=8, return True. A package sent at 05:00 from time zone 12 takes 8 hours to be delivered to time zone -3. The package is received at 22:00 local time, the day before it was sent. Return "True" as it was received the day before it was sent.
'''

def was_package_received_yesterday(tz_from, tz_to, start, duration):
    arrival_local = start - tz_from + duration + tz_to
    return arrival_local // 24 == -1
