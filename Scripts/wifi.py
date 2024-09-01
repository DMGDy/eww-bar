#!/usr/bin/env python3
import sys
import time
import psutil
import subprocess
import re

icons = [ "󰱔 ","󰅛"]

def get_ssid(wdev="wlp170s0"):
    #Get current wifi card status
    ssid_str = subprocess.run(f"nmcli connection | grep {wdev}",
                                    shell = True,
                                    capture_output=True).stdout.decode("utf-8")
    if(len(ssid_str) < 1):
        return (f"{icons[1]} No Connection")

    #if returned string is 0 means there is not any active connection
    pattern = re.compile(r"([A-Za-z0-9\s_.-]+)\s+[0-9a-f-]{8}-[0-9a-f-]{4}-[0-9a-f-]{4}-[0-9a-f-]{4}-[0-9a-f-]{12}")
    #format to just get ssid
    netname = pattern.findall(ssid_str)[0].rstrip()




    if(len(sys.argv) >= 2):
        if(sys.argv[1] == "-i"):
            print(icons[0],end="")
            sys.exit(0)
    return f"{netname}"


def get_network_speed(interface='wlp170s0', duration=1):
    """
    Measure the network speed of a given interface.
    
    :param interface: Network interface to monitor (default is 'eth0')
    :param duration: Duration in seconds to measure speed (default is 1 second)
    :return: Network speed in Mbps (Megabits per second) as a float
    """
    # Get initial byte counts
    init_stats = psutil.net_io_counters(pernic=True)[interface]
    init_bytes = init_stats.bytes_sent + init_stats.bytes_recv
    
    # Wait for specified duration
    time.sleep(duration)
    
    # Get final byte counts
    final_stats = psutil.net_io_counters(pernic=True)[interface]
    final_bytes = final_stats.bytes_sent + final_stats.bytes_recv
    
    # Calculate speed
    bytes_transferred = final_bytes - init_bytes
    bits_transferred = bytes_transferred * 8
    speed_mbps = (bits_transferred / duration) / 1_000_000  # Convert to Mbps
    
    return round(speed_mbps,7)

if __name__ == "__main__":
    speed = get_network_speed()
    unit = str('')
    if speed < 1:
        speed *= 100
        unit = " Kb/s"
    else:
        unit = " Mb/s"

    print(f"{get_ssid()} {speed:.2f}{unit}")
