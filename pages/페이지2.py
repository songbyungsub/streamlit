from tracemalloc import start
from matplotlib import ticker
import streamlit as st
import yfinance as yf
import pandas as pd
from st_pages import Page, show_pages, add_page_title, hide_pages

show_pages(
    [
        Page("login.py", "Login", "🔐"),
        Page("페이지1.py", "페이지1"),
        Page("페이지2.py", "페이지2"),
        Page("페이지3.py", "페이지3"),
        Page("페이지4.py", "페이지4"),
        Page("ecosaver.py", "main"),
    ]
)
hide_pages(["Login"])

st.title('반도체 주식 데이터 Dashboard')
# tickers =('TSLA','AAPL','MSFT','BTC-USD','ETH-USD','005930.KS')
tickers ={
  'SK hynix':'000660.KS',
  'Samsung Electronics':'005930.KS',
  'NVIDIA Corporation' :'NVDA',
  'QUALCOMM':'QCOM'
}
reversed_ticker = dict(map(reversed,tickers.items()))
dropdown = st.multiselect('select',tickers.keys())
start = st.date_input('Start', value=pd.to_datetime('2024-03-01'))
end = st.date_input('End',value=pd.to_datetime('today'))
if len(dropdown) > 0:
  for i in dropdown:
    df = yf.download(tickers[i],start,end)['Adj Close']
    st.title(reversed_ticker[tickers[i]])
    st.line_chart(df)