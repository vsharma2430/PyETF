import datetime as dt
from base.misc import *
from base.stock_base import *
    
def getHistoricalData(STK:str,start_date:dt.date = (dt.datetime.now()-dt.timedelta(days=30)).date(),end_date:dt.date=dt.datetime.now().date()):
    stk_ticker= get_ticker(STK)
    stk_historical_df = stk_ticker.history(start=start_date, end=end_date)
    return stk_historical_df