import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
from jugaad_data.nse import index_raw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

n_years = 3 # Parameter for historical years

def convert_to_date(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%d %b %Y')
    return date_obj

# Get from and to dates
to_date = datetime.date.today()
from_date = to_date - relativedelta(years=n_years)
print(from_date, to_date)

# Fetch the index data 
raw_index_data = index_raw(symbol="NIFTY 50", from_date=from_date, to_date=to_date)

# Converting into dataframe and processing the data
nifty_historical_df = (pd.DataFrame(raw_index_data)\
                            .assign(HistoricalDate=lambda x: x['HistoricalDate'].apply(convert_to_date))\
                            .sort_values('HistoricalDate')\
                            .drop_duplicates()\
                            .loc[lambda x: x['Index Name'] == 'Nifty 50']\
                            .reset_index(drop=True))

plt.figure(figsize=(12, 6))

nifty_historical_df['CLOSE'] = nifty_historical_df['CLOSE'].astype('float')

# Plot the historical Nifty data
plt.plot(nifty_historical_df['HistoricalDate'].values, nifty_historical_df['CLOSE'].values)

# Calculate and plot the trend line
x_values = np.arange(len(nifty_historical_df)).reshape(-1, 1)
y_values = nifty_historical_df['CLOSE'].values.reshape(-1, 1)
regressor = LinearRegression().fit(x_values, y_values)
trend_line = regressor.predict(x_values)
plt.plot(nifty_historical_df['HistoricalDate'].values, trend_line, linestyle='--', color='g', label='Trend Line')

# Set the title and labels
plt.title('Nifty Index')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()