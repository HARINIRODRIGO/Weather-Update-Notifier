from datetime import datetime
import requests
import pywhatkit as pwt

APPID = "97c0dc150275a8098e6d8c280ddc51df"
LOCATION = "Gampaha,Sri Lanka"
MY_LAT = "7.894095"
MY_LON = "80.795271"

TWILIO_ACCOUNT_SID = "AC52a1b9aa7c2b4ece70b824c804213ca4"
TWILIO_TOKEN = "15bd067dbddfb15e0f1a07c46b971475"

details = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": APPID,
    "exclude": "current,minutely,daily"
}

whether_info = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=details)
whether_info.raise_for_status()
data = whether_info.json()

is_rain = False
for i in range(12):
    weather = str(data["hourly"][i]["weather"][0]["id"])
    if weather[0] == "5":
        is_rain = True
        break

if is_rain:
    minutes = datetime.now().minute + 2
    pwt.sendwhatmsg(phone_no="+94701313779", message="It's going to rain today. Remember to bring an ☔",
                    time_hour=datetime.now().hour,
                    time_min=minutes)
