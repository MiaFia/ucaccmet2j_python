import json

# with open('stations.csv') as stations:
#     headers = stations.read()
#     print(headers)
#     stations= []
#     for code in stations:
#         location, state, station = code.strip().split(',')
#         stations.append({'location': location, 'State': state, 'Station': station})

# print(stations)
# open and load the data
with open ('precipitation.json', encoding='utf-8') as precipitation:
    rain=(json.load(precipitation))

#Filter for station and its measurement:
rain_seattle_month={}
for measurement in rain:
    if 'GHCND:US1WAKG0038' in measurement['station']:
        month= int(measurement['date'].split('-')[1])
        value= int(measurement['value'])

#Try to filter for 
# {1: value, 2: value, ...}