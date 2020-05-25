# Michael Solimano 2020

# Do some analysis of AAPL historical prices
# Practice reading in files, then manipulating data using matplot

import csv
import matplotlib.pyplot as plot
from datetime import datetime

file = 'HistoricalQuotes.csv'
with open(file) as f:
	read_file = csv.reader(f)
	header_row = next(read_file)

#Extract values from this file. The print statement at bottom allowed me to see file contents
	date = []
	close_last = []
	volume = []
	price_open = []
	price_high = []
	price_low = []

	#Append csv file data to lists. Convert string dates into datetime objects.
	for row in read_file:
		this_date = datetime.strptime(row[0], '%m/%d/%Y')
		date.append(this_date)
		close_last.append(row[1])
		volume.append(row[2])
		price_open.append(row[3])
		price_high.append(row[4])
		price_low.append(row[5])

#Reverse lists so that dates are chronological
date.reverse()
close_last.reverse()
volume.reverse()
price_open.reverse()
price_high.reverse()
price_low.reverse()

for index, data in enumerate(header_row):
	print(f"{index}: {data}")

#plot the data

plot.style.use('fivethirtyeight')
fig, ax = plot.subplots()
ax.plot(date, price_high, c='green')
ax.set_title("Monthly price highs: AAPL", fontsize=24)
ax.set_xlabel('Date', fontsize=20)
ax.set_ylabel('Price (high)', fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=12)
fig.autofmt_xdate()
plot.show()