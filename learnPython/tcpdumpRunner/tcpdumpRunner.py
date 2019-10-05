import subprocess
import time
from datetime import datetime


def run_tcpdump_on_local_machine():
    func_name = "run_tcpdump_on_local_machine - "
    print(func_name + "start")
    interface_name = "ens33"
    curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    capture_file_name = "/tmp/guyCapture_interface_" + interface_name + "_" + curr_time + ".pcap"
    num_sec_to_sleep = 5
    print(func_name + "about to create capture with name:" + capture_file_name)
    p = subprocess.Popen(["tcpdump",
                          "-i", interface_name,
                          "-w", capture_file_name],
                         stdout=subprocess.PIPE)
    print(func_name + "about to sleep for " + str(num_sec_to_sleep) + " seconds")
    time.sleep(num_sec_to_sleep)
    p.terminate()
    print(func_name + "end")