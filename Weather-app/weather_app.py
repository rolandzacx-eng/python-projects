import json
import requests
API_KEY = "f22af7c77fe041a1aed95054260608"
while True:
    city = input("Enter city name (or type 'exit' to quit): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
    try:
        response = requests.get(url)
        data = response.json()
        print("STATUS:", response.status_code)

        if response.status_code == 200:
            print("Weather in",data["location"]["name"])
            print("temperature:", data["current"]["temp_c"], "c")
            print("Humidity:",data["current"]["humidity"],"%")
            print("Wind:", data["current"]["wind_kph"], "kph")
            print("Condition:",data["current"]["condition"]["text"])

            history_entry = {
                "city": data["location"]["name"],
                "temp_c": data["current"]["temp_c"],
                "condition": data["current"]["condition"]["text"]
            }
            try:
                with open("history.json", "r") as f:
                    history = json.load(f)
            except FileNotFoundError:
                history = []
            history.append(history_entry)

            with open("history.json","w") as f:
                json.dump(history,f,indent=4)
        else:
            print("City not found. Please check the spelling and try again.")
    except requests.exceptions.ConnectionError:
        print("No internet. Please check your network.")
    print()

