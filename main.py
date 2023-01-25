import requests

api_key = "692c67f68c0d645297530d27416d3e02"
his_api = "26631f0f41b95fb9f5ac0df9a8f43c92"


class Weather:

    def __init__(self, api_key: str = "26631f0f41b95fb9f5ac0df9a8f43c92",
                 lat: float = None, lon: float = None, city: str = None, units: str = "metric"):

        if city:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
            self.data = requests.get(url).json()

        elif lat and lon:
            url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units={units}"
            self.data = requests.get(url).json()

        else:
            raise AttributeError("provide either city or lon and lat as arguments")

        if self.data['cod'] != "200":
            raise ValueError(f"{self.data['message']}")

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        interesting = self.data['list'][:4]

        result = ""
        for x in interesting:
            descript = x['weather'][0]['description']
            icon = x['weather'][0]['icon']
            date_t = x['dt_txt'].split(' ')[0]
            time_t = x['dt_txt'].split(' ')[1]
            value = x['main']['temp']
            result += (f"On {date_t} at {time_t} will be {value} celsius, description - {descript}, icon - {icon} \n")

        return result


if __name__ == '__main__':
    sec_wet = Weather(city='Madrid')
    print(sec_wet.next_12h_simplified())
