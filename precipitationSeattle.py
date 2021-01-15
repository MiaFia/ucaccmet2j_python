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
rain_seattle_month=[0,0,0,0,0,0,0,0,0,0,0,0] #So there is a position that we can later assign it to these positions.
for measurement in rain:
    if 'GHCND:US1WAKG0038' in measurement['station']:
        month= int(measurement['date'].split('-')[1])
        value=measurement['value']
        rain_seattle_month[month-1]+=value #since the value for months starts at 1, but we want to start at 0.
print(rain_seattle_month)


