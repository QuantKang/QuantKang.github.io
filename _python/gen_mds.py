import FinanceDataReader as fdr
import pandas as pd
import bt
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

sns.set_style('whitegrid')
plt.rc('font', family='NanumBarunGothic')

stock_df = fdr.StockListing('KRX')

def fstr(template):
    return eval(f"f'{template}'").strip()


_BASE_PATH = '../'
_MD_TMPL = '''
---
title: {name}({ticker}) 주가 정보
categories:
- Stock
---

{name}는 시가({open_price}원), 고가({high_price}원), 저가({low_price}원), 종가({close_price}원)였습니다.

전일 종가 대비 {(pct_change * 100):.1f}% {pct_change_label}했습니다.

<!-- more -->

![{ticker}](/assets/stock_images/{ticker}.png)

'''
_MD_TMPL = _MD_TMPL.replace('\n', '{_NEW_LINE}')
_NEW_LINE = '\n'
_N_DAYS = 250

tickers = ['005930', '000660']

for ticker in tqdm(tickers):
  name = stock_df[stock_df.Code == ticker].Name.iloc[0]
  df = fdr.DataReader(ticker)
  open_price, high_price, low_price, close_price = df[['Open', 'High', 'Low', 'Close']].iloc[-1]
  pct_change = df.Close.iloc[-1] / df.Close.iloc[-2] - 1
  pct_change_label = '상승' if pct_change > 0 else '하락'
  _FILE_PATH = f'{_BASE_PATH}/_posts/2024-01-01-{ticker}.md'
  _IMG_PATH = f'{_BASE_PATH}/assets/stock_images/{ticker}.png'
  with open(_FILE_PATH, 'w') as f:
    f.write(fstr(_MD_TMPL))

  window_l = [5, 20, 60]
  for w in window_l:
    df[f'MA {w}'] = df.Close.rolling(w).mean()

  #plt.figure(figsize = (8, 6))
  df = df[-_N_DAYS: ]
  df.Close.plot(label = name)
  for w in window_l:
    df[f'MA {w}'].plot(label = f'{w} MA', lw = 1)
  plt.title(f'{name} 최근 {_N_DAYS} 거래일 주가 흐름')
  plt.ylabel('가격 (원)')
  plt.xlabel('')
  plt.legend()
  plt.savefig(_IMG_PATH)
  plt.close()
