
import requests,json
import spch_syn

if __name__=='__main__':
    try:
        city=input("Enter Your City : ")
        url=f"https://api.weatherapi.com/v1/current.json?key=fb935f08f31e40b8bf9211825231607&q={city}"
        req=requests.get(url)
        weather_data=json.loads(req.text)
        temp_c=weather_data['current']['temp_c']
        spch_syn.robosp(f'Greetings sir or mam , the current temperature of {city} is {temp_c} degree celsius')
    except:
        spch_syn.robosp("Please enter a valid city name sir or mam")