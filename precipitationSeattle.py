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

#Filter for station and its measurement plus basically everything else:
rain_seattle_month=[0,0,0,0,0,0,0,0,0,0,0,0] #So there is a position that we can later assign it to these positions.
for measurement in rain:
    if 'GHCND:US1WAKG0038' in measurement['station']:
        month= int(measurement['date'].split('-')[1])
        value=measurement['value']
        rain_seattle_month[month-1]+=value #since the value for months starts at 1, but we want to start at 0.
print(f'Total of Jan: {rain_seattle_month[0]}, Total of Feb:{rain_seattle_month[1]}, Total of Mar:{rain_seattle_month[2]} Total of Apr:{rain_seattle_month[3]}, Total of May:{rain_seattle_month[4]}, Total of Jun:{rain_seattle_month[5]}')

#Put it into a json file.
with open ('precipitation_Seattle.json', 'w') as json_file:
    json.dump(rain_seattle_month, json_file)

