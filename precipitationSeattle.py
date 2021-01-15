import json
# open and load the data
with open ('precipitation.json', encoding='utf-8') as precipitation:
    rain=(json.load(precipitation))

#Filter for station and its measurement plus basically everything else:
rain_seattle_month=[0]*12 #So there is a position that we can later assign the total per month to these positions.
rain_seattle_year=0
for measurement in rain:
    if 'GHCND:US1WAKG0038' in measurement['station']:
        month= int(measurement['date'].split('-')[1])
        value=measurement['value']
        rain_seattle_month[month-1]+=value #since the value for months starts at 1, but we want to start at 0.
        rain_seattle_year+= value #This adds all values together to get to the yearly percipitation
percentage_all=[]
for rain_total_month in rain_seattle_month: #Percentages for each month
    percentage_monthly_to_yearly=(rain_total_month/rain_seattle_year)*100
    percentage_all.append(round(percentage_monthly_to_yearly, 2)) #This step is not strictly necessary, but to have a list of all the percentages in one. I am also rounding 
    #the values so it is less of a hassle to look at them
print(percentage_all)
with open ('precipitation_Seattle.json', 'w') as json_file:
    json_file.write('This is the total percipitation for each month \n')
    json.dump(rain_seattle_month, json_file, indent=1)
    json_file.write('This is the total yearfall per year:')
    json.dump(rain_seattle_year, json_file, indent=1)
    json_file.write('\n This is the percentage of the monthly percipiation of the yearly percipitation \n')
    json.dump(percentage_all, json_file, indent=1)
    



