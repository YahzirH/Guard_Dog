import subprocess

def setup_monitor_mode(interface):
    subprocess.run(['sudo', 'airmon-ng', 'check' 'kill'])
    subprocess.run(['sudo', 'airmon-ng', 'start', interface])
    print(f"{interface} enabled in monitor mode.")

setup_monitor_mode("wlan0")