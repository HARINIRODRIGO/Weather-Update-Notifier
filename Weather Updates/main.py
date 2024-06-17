from datetime import datetime
import requests
import pywhatkit as pwt
from keys import TWILIO_ACCOUNT_SID, TWILIO_TOKEN, APPID, LOCATION, MY_LAT, MY_LON, PHONE_NUMBER

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
    pwt.sendwhatmsg(phone_no= PHONE_NUMBER, message="It's going to rain today. Remember to bring an ☔",
                    time_hour=datetime.now().hour,
                    time_min=minutes)
