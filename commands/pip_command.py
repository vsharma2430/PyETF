with open('commands\pip.txt', 'r') as f:
    print(' && '.join([line.strip() for line in f.readlines()]))
    
'''
pip install "yfinance[nospam,repair]" && pip install requests-cache && pip install requests-ratelimiter && pip install pyrate-limiter && pip install jugaad-data && pip install nselib && pip install PyQt5 && pip install matplotlib && pip install sklearn-model && pip install rocketry && pip install "fastapi[standard]" && pip install uvicorn && pip install plotly
'''