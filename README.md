### Introduction 

PyETF is a web application built to help the user make informed trading decisions.

#### Features
- Buy/Sell recommendations for custom stock lists
- Live stock/ETF prices using PyPrice
- Detailed candle charts
- Candle Pattern identification
- Detailed charts with candle patterns and scores

#### Dependencies
- Fastapi
- Yfinance
- Yfinance-cache
- Plotly
- Uvicorn

### Installation Instructions

- Install Python 3.12+ from [Official Python website](https://www.python.org/downloads/)
- Create a folder in your system 'PyETF'.
- Open terminal/command prompt in the folder location.
- Clone this Git Repository to a desired folder.

```custom_prefix(E:\PyETF>)
git clone https://github.com/vsharma2430/PyETF
```
- Create virtual environment for this project.

```custom_prefix(E:\PyETF>)
python -m venv .venv
```
- Activate virtual environment.
```custom_prefix(E:\PyETF>)
E:\PyETF\.venv\Scripts\Activate.ps1
```
- Install dependencies.
```custom_prefix((.venv) E:\PyETF>)
pip install -r requirements.txt
```
- Run client.py
```custom_prefix((.venv) E:\PyETF>)
python client.py
```
- Go to link to access the webapp (http://localhost:8005/).

### Portfolio Management
- Go to Portfolio folder -> (invest/portfolio) in the installed location.
- Edit the CSV file for stocks and etf.

### Stock/ETF Lists
- Go to Stock List Folder -> (invest/stock_list) in the installed location.
- Edit the CSV file for stocks and etf.
- Copy and rename any existing list and edit it to your preferences.