from generate_report import generate_call_count
from telco_bridge_report import TelcoBridgeReport

TelcoBridgeReport_obj = TelcoBridgeReport()
generate_call_count_obj = generate_call_count()

if __name__ == '__main__':
    choice = input("Choose from following: \n"
                   "Concurrent report - Input 1 \n"
                   "TelcoBridge report - Input 2 \n")
    if choice == '1':
        generate_call_count_obj.generate_call_count_report()
    elif choice == '2':
        TelcoBridgeReport_obj.generate_telcobridgereport()
    else:
        print('Please choose of the the valid option')
