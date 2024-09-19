from datetime import datetime
import requests
import smtplib
import time

MY_LAT = float("Enter Your Target Latitude: ")
MY_LONG = float("Enter Your Target Longitude: ")
THRESHOLD_LAT = (MY_LAT - 5, MY_LAT + 5)
THRESHOLD_LONG = (MY_LONG - 5, MY_LONG + 5)
MY_EMAIL = input("Enter Your Email: ")
MY_PASS = input("Enter Your Password: ")
TIMEZONE_ID = input("Enter Your Timezone ID: ")

def iss():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    return (latitude, longitude)

def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": TIMEZONE_ID
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False

def main():
    if night():
        iss_latitude, iss_longitude = iss()

        if THRESHOLD_LAT[0] <= iss_latitude <= THRESHOLD_LAT[1]:
            if THRESHOLD_LONG[0] <= iss_longitude <= THRESHOLD_LONG[1]:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASS)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg="Subject:ISS Overhead!\n\nHey, the ISS is near your coordinates, now grab your radio, and run to the roof!"
                    )
                
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    while True:
        time.sleep(60)
        print(main())