import requests,json
import spch_syn

if __name__=='__main__':
    try:
        city=input("Enter Your City : ")
        url=f"https://api.weatherapi.com/v1/current.json?key=1434e3c643804d2c8d2105338230508&q={city}"
        req=requests.get(url)
        weather_data=json.loads(req.text)
        temp_c=weather_data['current']['temp_c']
        condition=weather_data['current']['condition']['text']
        print(weather_data)
        spch_syn.robosp(f'Greetings sir or mam , the current temperature of {city} is {temp_c} degree celsius , and the weather condition is {condition}')
    except:
        spch_syn.robosp("Please enter a valid city name sir or mam")
