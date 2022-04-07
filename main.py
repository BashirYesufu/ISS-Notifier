import requests
from datetime import datetime

MY_LAT = 6.465422  # Your latitude
MY_LONG = 3.406448  # Your longitude


def is_iss_overhead():
    api_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    api_response.raise_for_status()
    api_data = api_response.json()

    iss_latitude = float(api_data["iss_position"]["latitude"])
    iss_longitude = float(api_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
