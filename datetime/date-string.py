class DatetimeUtility(object):
    """
    Provide utility function related to date or datetime operations
    """

    @staticmethod
    def convert_date_to_db_datetime_string(date, timeStr):
        return date.isoformat() + timeStr

    @staticmethod
    def convert_db_dt_str_to_date(dt_str):
        fmt = '%Y-%m-%d'
        return datetime.strptime(dt_str[:len("YYYY-MM-DD")], fmt).date()

    @staticmethod
    def client_DT_string_to_date(datetime_str):
        """
         convert datetime string from client side to date object
         client side date time string : '2016-07-06T07:00:00.000Z'
        """
        datetimeFormat = '%Y-%m-%dT%H:%M:%S'
        result = datetime.strptime(str(datetime_str)[0:-5], datetimeFormat).date()
        return result

    @staticmethod
    def client_DT_string_to_server_DT_string(datetime_str):
        """
         convert datetime string from client side to server side / db datetime string
         client side date time string : '2016-07-06T07:00:00.000Z'
        """
        if not datetime_str:
            return ""
        result = datetime_str[0:-5]
        return result

    @staticmethod
    def create_datetime_ts(curr_datetime=datetime.now()):
        '''
        In our database, datetime value was saved as string with format "2016-06-03T20:12:20".
        This function returns the formatted datetime string for database
        :param curr_date:
        :return: formatted datetime string
        '''
        return curr_datetime.strftime("%Y-%m-%dT%H:%M:%S")

    @staticmethod
    def get_last_monday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of last monday to current day.
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        last_monday = curr_date - timedelta(days=curr_date.weekday(), weeks=1)
        return last_monday

    @staticmethod
    def get_last_sunday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of last sunday to current day.
        '''
        last_sunday = curr_date - timedelta(days=(curr_date.weekday() + 1))
        return last_sunday

    @staticmethod
    def get_monday_of_previous_weeks(curr_date=date.today(), weeks=1):
        '''
        :param curr_date:
        :return: Date of last monday to current day.
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        last_monday = curr_date - timedelta(days=curr_date.weekday(), weeks=1)
        the_monday = last_monday - timedelta(weeks=weeks - 1)

        return the_monday

    @staticmethod
    def get_sunday_of_previous_weeks(curr_date=date.today(), weeks=1):
        '''
        :param curr_date:
        :return: Date of last sunday to current day.
        '''
        last_sunday = curr_date - timedelta(days=(curr_date.weekday() + 1))
        the_sunday = last_sunday - timedelta(weeks=weeks - 1)
        return the_sunday

    @staticmethod
    def get_this_monday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of this monday to current day.
        '''
        this_monday = curr_date - timedelta(days=curr_date.weekday())
        return this_monday

    @staticmethod
    def get_this_sunday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of this sunday to current day.
        '''
        this_monday = curr_date - timedelta(days=curr_date.weekday() - 6)
        return this_monday

    @staticmethod
    def get_next_monday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of next monday to current day.
        '''
        next_monday = curr_date - timedelta(days=curr_date.weekday()) + timedelta(weeks=1)
        return next_monday

    @staticmethod
    def get_next_sunday(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date of next sunday to current day.
        '''
        this_monday = curr_date - timedelta(days=curr_date.weekday()) + timedelta(days=13)
        return this_monday

    @staticmethod
    def get_last_week_date_span_str(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date string last monday to last sunday with format ""%Y-%m-%d"
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        last_monday = DatetimeUtility.get_last_monday(curr_date)
        last_sunday = DatetimeUtility.get_last_sunday(curr_date)

        return last_monday.isoformat(), last_sunday.isoformat()

    @staticmethod
    def get_this_week_date_span_str(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date string this monday to this sunday with format ""%Y-%m-%d"
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        this_monday = DatetimeUtility.get_this_monday(curr_date)
        this_sunday = DatetimeUtility.get_this_sunday(curr_date)

        return this_monday.isoformat(), this_sunday.isoformat()

    @staticmethod
    def get_next_week_date_span_str(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date string next monday to next sunday with format ""%Y-%m-%d"
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        next_monday = DatetimeUtility.get_next_monday(curr_date)
        next_sunday = DatetimeUtility.get_next_sunday(curr_date)

        return next_monday.isoformat(), next_sunday.isoformat()

    @staticmethod
    def get_last_week_datetime_span_str(curr_date=date.today()):
        '''
        :param curr_date:
        :return: Date string last monday to last sunday with format ""%Y-%m-%d"
        '''
        # weekday()return the day of the week as an integer, where Monday is 0 and Sunday is 6.
        last_monday = DatetimeUtility.get_last_monday(curr_date)
        last_sunday = DatetimeUtility.get_last_sunday(curr_date)

        return last_monday.isoformat() + "T00:00:00", last_sunday.isoformat() + "T23:59:59"