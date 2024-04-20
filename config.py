import os
class Config:
    API_ID=
    API_HASH=""
    TOKEN=""
    SUDO = list(int(i) for i in os.environ.get("SUDO", "").split(" "))
    START_IMG="https://telegra.ph/file/50df257b98a528414de84.jpg"
    
    
    
