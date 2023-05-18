from schedule import every, repeat, run_pending
import time
import os

@repeat(every(3).seconds)
def mitigate():
    file = open("mitigate.txt","r")
    result = file.read()
    file.close()
    if (result == "1"):
        os.system("sudo iptables -A INPUT -i eth0 -p tcp --dport 80 -j DROP")
        print("Requests to the host are discareded successfully")
    
while True:
    run_pending()
    time.sleep(1)
