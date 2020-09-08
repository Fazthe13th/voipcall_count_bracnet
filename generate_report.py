from database import connect_db
from datetime import datetime
import sys


class generate_call_count:
    def generate_call_count_report(self):
        start_datetime, end_datetime = self.prepare_time()

    def check_datetime_format(self, date_time):
        try:
            date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M')
            return date_time
        except Exception as e:
            print(str(e))
            return None

    def prepare_time(self):
        start_datetime = input(
            "Enter start date and time in '%Y-%m-%d %H:%M' format:")
        start_time_obj = self.check_datetime_format(start_datetime)
        end_datetime = input(
            "Enter end date and time in '%Y-%m-%d %H:%M' format:")
        end_time_obj = self.check_datetime_format(end_datetime)
        if not start_time_obj or not end_time_obj:
            sys.exit()
        return start_time_obj, end_time_obj
