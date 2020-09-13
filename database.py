import mariadb
import os
from dotenv import load_dotenv
import sys

load_dotenv()


class database:
    def connect_db(self):
        try:
            voipswitch = mariadb.connect(
                user=os.getenv('user'),
                password=os.getenv('passwd'),
                host=os.getenv('host'),
                port=3306,
                database=os.getenv('database')
            )

            print('Database connected')
            return voipswitch
        except mariadb.Error as e:
            print('An error happed: ' + str(e))
            return None

    def count_calls(self, query_datetime):
        voipdb = self.connect_db()
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            count_calls = "SELECT count(*) FROM voipswitch.calls where call_start <= %s and call_end >= %s"
            cursor.execute(count_calls, (query_datetime, query_datetime))
            result = cursor.fetchone()
            print(result[0])
            cursor.close()
            voipdb.close()
            return result
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None
