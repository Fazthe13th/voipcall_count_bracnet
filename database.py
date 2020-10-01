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
            cursor.close()
            voipdb.close()
            return result
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TOTAL_OUT_TB_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TOTAL_IN_TB_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60)"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def GETCO_IN_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff=56"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def MNH_IN_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff=58"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def GP_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '8807117%' OR outbound_called_number LIKE '8807113%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def GP_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60) AND (caller_id LIKE '017%' OR caller_id LIKE '013%')"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def ROBI_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '8808118%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def ROBI_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60) AND caller_id LIKE '018%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def AIRTEL_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '8808116%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def AIRTEL_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60) AND caller_id LIKE '016%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def BANGLA_LINK_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '8809119%' OR outbound_called_number LIKE '8809114%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def BANGLA_LINK_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60) AND (caller_id LIKE '019%' OR caller_id LIKE '014%')"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TELETALK_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '8805115%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TELETALK_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58,60) AND caller_id LIKE '015%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def BTCL_IN_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff=60"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def BTCL_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number REGEXP '^0[2-9]'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def ISD_out_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=4 AND route_type=0 AND outbound_called_number LIKE '00%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def ISD_in_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (56,58) AND caller_id LIKE '00%'"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TOTAL_BDIX_OUT_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_route=5 AND route_type=0"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None

    def TOTAL_BDIX_IN_call_count_cost_sum(self, *args):
        voipdb = self.connect_db()
        start_time_obj, end_time_obj = args
        if not voipdb:
            print('Database not connected')
            sys.exit()
        cursor = voipdb.cursor()
        try:
            report_query = "SELECT count(id_call),sum(duration)/60, sum(cost) FROM voipswitch.calls WHERE call_start BETWEEN %s AND %s AND id_tariff IN (54)"
            cursor.execute(report_query, (start_time_obj, end_time_obj))
            result = cursor.fetchone()
            cursor.close()
            voipdb.close()
            return result[0], result[1], result[2]
        except Exception as e:
            print('Error: ' + str(e))
            cursor.close()
            voipdb.close()
            return None
