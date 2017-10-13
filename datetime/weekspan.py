def getLastSunday(currDate):
    lastSunday = currDate - timedelta(days=(currDate.weekday() + 1))
    return lastSunday

def getThisMonday(currDate):
    thisMonday = currDate - timedelta(days=currDate.weekday())
    return thisMonday

# Return last monday to last sunday.
def getLastWeekDateTimeSpan(currDate):
    # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    lastMonday = currDate - timedelta(days=currDate.weekday(), weeks=1)
    lastSunday = lastMonday + timedelta(6)

    return lastMonday.isoformat(), lastSunday.isoformat()

# Return this monday to this sunday.
def getThisWeekDateTimeSpan(currDate):
    # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    thisMonday = currDate - timedelta(days=currDate.weekday())
    thisSunday = thisMonday + timedelta(6)

    return thisMonday.isoformat(), thisSunday.isoformat()

# Return next monday to next sunday.
def getNextWeekDateTimeSpan(currDate):
    # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
    nextMonday = currDate - timedelta(days=currDate.weekday()) + timedelta(weeks=1)
    nextSunday = nextMonday + timedelta(6)

    return nextMonday.isoformat(), nextSunday.isoformat()



if __name__ == "__main__":
  today = date.today()
  thisMonday, thisSunday = getThisWeekDateTimeSpan(today)
        