import csv

import numpy as np

from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename_sitka = 'sitka_weather_2014.csv'
filename_death_valley = 'death_valley_2014.csv'
with open(filename_sitka) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    sitka_dates, sitka_highs, sitka_lows = [], [], []
    for row in reader:
        try:
            sitka_current_date = datetime.strptime(row[0], "%Y-%m-%d")
            sitka_high = int(row[1])
            sitka_low = int(row[3])
        except ValueError:
            print(sitka_current_date, 'missing data')
        else:
            sitka_dates.append(sitka_current_date)
            sitka_highs.append(sitka_high)
            sitka_lows.append(sitka_low)


with open(filename_death_valley) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    death_valley_dates, death_valley_highs, death_valley_lows = [], [], []
    for row in reader:
        try:
            death_valley_current_date = datetime.strptime(row[0], "%Y-%m-%d")
            death_valley_high = int(row[1])
            death_valley_low = int(row[3])
        except ValueError:
            print(death_valley_current_date, 'missing data')
        else:
            death_valley_dates.append(death_valley_current_date)
            death_valley_highs.append(death_valley_high)
            death_valley_lows.append(death_valley_low)


# Plot data.
fig = plt.figure(dpi=128, figsize=(8, 5))

plt.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
plt.plot(sitka_dates, sitka_lows, c='blue', alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

plt.plot(death_valley_dates, death_valley_highs, c='green', alpha=0.5)
plt.plot(death_valley_dates, death_valley_lows, c='black', alpha=0.5)
plt.fill_between(death_valley_dates, death_valley_highs, death_valley_lows, facecolor='green', alpha=0.1)

print(sitka_dates)
print("\n\n\n")
print(death_valley_dates)

plt.axis([np.min(sitka_dates), np.max(sitka_dates), 0, 150])
# Format plot.
title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
