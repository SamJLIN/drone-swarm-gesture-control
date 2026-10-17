import sys
import traceback
import tellopy
import av
import cv2
import numpy
from time import sleep
import threading
import numpy as np

import time
from pywifi import PyWiFi, const, Profile

def connect_to_wifi(ssid, password=None):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0] 

    iface.scan()  
    time.sleep(2) 

    scan_results = iface.scan_results()
    profile = None

    for result in scan_results:
        if result.ssid == ssid:
            profile = Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN  
            
            if password:  
                profile.akm.append(const.AKM_TYPE_WPA2PSK) 
                profile.cipher = const.CIPHER_TYPE_CCMP  
                profile.key = password  
            else:  
                profile.akm.append(const.AKM_TYPE_NONE)  
                
            break

    if profile is None:
        print(f"未找到SSID為 {ssid} 的網路")
        return

    iface.remove_all_network_profiles()
    iface.add_network_profile(profile)
    iface.connect(profile)

    time.sleep(10)  

    if iface.status() == const.IFACE_CONNECTED:
        print(f"成功連接到 {ssid}")
    else:
        print(f"無法連接到 {ssid}")

if __name__ == "__main__":
    ssid = ""  
    password = None  
    connect_to_wifi(ssid, password)

