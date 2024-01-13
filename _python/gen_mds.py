import FinanceDataReader as fdr
import pandas as pd
import bt
from tqdm import tqdm
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')

stock_df = fdr.StockListing('KRX')

def fstr(template):
    return eval(f"f'{template}'").strip()


_BASE_PATH = '../_posts/'
_MD_TMPL = '''
---
title: {name}({ticker}) 주가 정보
categories:
- 개별 종목
---
{name}는 시가({open_price}원), 고가({high_price}), 저가({low_price}), 종가({close_price})였습니다.
'''
_MD_TMPL = _MD_TMPL.replace('\n', '{_NEW_LINE}')
_NEW_LINE = '\n'

tickers = ['005930', '000660']

for ticker in tqdm(tickers):
  name = stock_df[stock_df.Code == ticker].Name.iloc[0]
  df = fdr.DataReader(ticker)
  open_price, high_price, low_price, close_price = df[['Open', 'High', 'Low', 'Close']].iloc[-1]
  _FILE_PATH = f'{_BASE_PATH}/2024-01-01-{ticker}.md'
  with open(_FILE_PATH, 'w') as f:
    f.write(fstr(_MD_TMPL))
