from database import database
from datetime import datetime, timedelta
import sys
import time
import csv
import os.path


db = database()


class generate_call_count:
    def generate_call_count_report(self):
        start_datetime, end_datetime = self.prepare_time()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        subdirectory = 'reports'
        file_path = os.path.join(
            subdirectory, 'concurrent_calls_'+timestr + ".csv")

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["start_time", "end_time", "call_count"])
            while start_datetime != end_datetime:
                new_start_datetime = start_datetime + \
                    timedelta(0, 60)  # for 60 seconds addition
                call_count = db.count_calls(new_start_datetime)
                if not call_count:
                    continue
                writer.writerow(
                    [start_datetime, new_start_datetime, call_count[0]])
                start_datetime = new_start_datetime

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
