from database import database
from datetime import datetime, timedelta
import sys
import time
import csv
import os.path

db = database()


class TelcoBridgeReport():
    def generate_telcobridgereport(self):
        """
        Generate the report
        """
        report_dict = self.get_telco_report_dict()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        subdirectory = 'reports'
        file_path = os.path.join(
            subdirectory, 'TelcoBridgeReport_'+timestr + ".csv")
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                ["", "Number of calls", "Total call duration", "Total call cost"])
            for report_tag in report_dict:
                writer.writerow(
                    [report_tag, report_dict[report_tag]['call_count'], report_dict[report_tag]['duration'], report_dict[report_tag]['cost']])

    def get_telco_report_dict(self):
        categories = self.receive_category()
        start_time_obj, end_time_obj = self.prepare_time()
        report_dict = {}
        if '*' in categories:
            call_count, duration, cost = db.TOTAL_OUT_TB_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TOTAL_OUT_TB'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.TOTAL_IN_TB_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TOTAL_IN_TB'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.GETCO_IN_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['GETCO_IN'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.MNH_IN_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['MNH_IN'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.GP_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['GP_out'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.GP_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['GP_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.ROBI_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['ROBI_out'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.ROBI_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['ROBI_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.AIRTEL_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['AIRTEL_out'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.AIRTEL_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['AIRTEL_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.BANGLA_LINK_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TOTAL_IN_TB'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.BANGLA_LINK_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['BANGLA_LINK_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.TELETALK_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TELETALK_out'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.TELETALK_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TELETALK_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.BTCL_IN_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['BTCL_IN'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.ISD_out_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['ISD_out'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.ISD_in_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['ISD_in'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.TOTAL_BDIX_OUT_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TOTAL_BDIX_OUT'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            call_count, duration, cost = db.TOTAL_BDIX_IN_call_count_cost_sum(
                start_time_obj, end_time_obj)
            report_dict['TOTAL_BDIX_IN'] = {
                'call_count': str(call_count),
                'duration': str(duration),
                'cost': str(cost)
            }
            return report_dict

        for category in categories:
            # Selected Option start
            if category == '1':
                call_count, duration, cost = db.TOTAL_OUT_TB_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TOTAL_OUT_TB'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '2':
                call_count, duration, cost = db.TOTAL_IN_TB_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TOTAL_IN_TB'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '3':
                call_count, duration, cost = db.GETCO_IN_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['GETCO_IN'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '4':
                call_count, duration, cost = db.MNH_IN_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['MNH_IN'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '5':
                call_count, duration, cost = db.GP_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['GP_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '6':
                call_count, duration, cost = db.GP_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['GP_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '7':
                call_count, duration, cost = db.ROBI_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['ROBI_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '8':
                call_count, duration, cost = db.ROBI_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['ROBI_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '9':
                call_count, duration, cost = db.AIRTEL_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['AIRTEL_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '10':
                call_count, duration, cost = db.AIRTEL_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['AIRTEL_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '11':
                call_count, duration, cost = db.BANGLA_LINK_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TOTAL_IN_TB'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '12':
                call_count, duration, cost = db.BANGLA_LINK_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['BANGLA_LINK_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '13':
                call_count, duration, cost = db.TELETALK_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TELETALK_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '14':
                call_count, duration, cost = db.TELETALK_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TELETALK_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '15':
                call_count, duration, cost = db.BTCL_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['BTCL_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '16':
                call_count, duration, cost = db.BTCL_IN_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['BTCL_IN'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '17':
                call_count, duration, cost = db.ISD_out_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['ISD_out'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '18':
                call_count, duration, cost = db.ISD_in_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['ISD_in'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '19':
                call_count, duration, cost = db.TOTAL_BDIX_OUT_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TOTAL_BDIX_OUT'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }
            elif category == '20':
                call_count, duration, cost = db.TOTAL_BDIX_IN_call_count_cost_sum(
                    start_time_obj, end_time_obj)
                report_dict['TOTAL_BDIX_IN'] = {
                    'call_count': str(call_count),
                    'duration': str(duration),
                    'cost': str(cost)
                }

        return report_dict

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

    def receive_category(self):
        receive_category = input(
            "Enter categories separated by space: \n"
            "TOTAL OUT - TB -- Input 1 \n"
            "TOTAL IN - TB -- Input 2 \n"
            "GETCO-IN -- Input 3 \n"
            "MNH-IN -- Input 4 \n"
            "GP - Out -- Input 5 \n"
            "GP - IN -- Input 6 \n"
            "ROBI - Out -- Input 7 \n"
            "ROBI - IN -- Input 8 \n"
            "AIRTEL - Out -- Input 9 \n"
            "AIRTEL - IN -- Input 10 \n"
            "BANGLA-LINK - Out -- Input 11 \n"
            "BANGLA-LINK - IN -- Input 12 \n"
            "TELETALK - Out -- Input 13 \n"
            "TELETALK - IN -- Input 14 \n"
            "BTCL - Out -- Input 15 \n"
            "BTCL - IN -- Input 16 \n"
            "ISD - Out -- Input 17 \n"
            "ISD - IN -- Input 18 \n"
            "TOTAL-OUT (BDIX) -- Input 19 \n"
            "TOTAL-IN (BDIX) -- Input 20 \n"
            "ALL -- Input (*) \n")
        categoryList = receive_category.split()
        return categoryList
