from Process_Cloud import WIFI_Init
import os


wifiinit=WIFI_Init("setting_data.json","wifi_decode.json","utf-8")

print(f"T: {wifiinit.One}")