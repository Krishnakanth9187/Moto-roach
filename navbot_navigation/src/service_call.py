#!/usr/bin/env python3
import os
import time

def service_call():
    while True:
        print("cleared")
        os.system('rosservice call /move_base/clear_costmaps "{}"')
        time.sleep(5)
        
service_call()
