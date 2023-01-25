import requests
# import pprint

api_key = "692c67f68c0d645297530d27416d3e02"
his_api = "26631f0f41b95fb9f5ac0df9a8f43c92"

# print(jsa['list'][0]['main']['temp'])


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

    def next_12h(self):
        return self.data['list'][:4]

    def next_12h_simplified(self):
        try:
            interesting = self.data['list'][:4]

            result = ""
            for x in interesting:
                descript = x['weather'][0]['description']
                date_t = x['dt_txt'].split(' ')[0]
                time_t = x['dt_txt'].split(' ')[1]
                value = x['main']['temp']
                result += (f"On {date_t} at {time_t} will be {value} celsius description: {descript} \n")

            return result

        except KeyError:
            return f"Error {self.data['cod']}, {self.data['message']}"

# self.data['list'][0]['main']['temp']
# wet = Weather(location='Dubaj')
# print(wet.data)

sec_wet = Weather(city='Madriddd')

# pprint.pprint(sec_wet.next_12h())
# print(sec_wet.next_12h_simplified())
print(sec_wet.next_12h_simplified())
