import plotly.graph_objects as go
import pandas as pd
import streamlit as st
import yfinance as yf #야후 파이낸스에서 크롤링한 데이터를 제공하는 라이브러리
import matplotlib.pyplot as plt
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

def main():
    st.title("주식 데이터")
    st.sidebar.title("Stock Chart")
    ticker = st.sidebar.text_input("Enter a ticker (e. g. SSNLF)", value = "SSNLF")
    st.sidebar.markdown('Tickers Link : [All Stock Symbols](https://stockanalysis.com/stocks/)')
    start_date = st.sidebar.date_input("시작 날짜: ", value = pd.to_datetime("2023-01-01"))
    end_date = st.sidebar.date_input("종료 날짜: ", value = pd.to_datetime("2023-03-28"))

	#ticker 종목의 시작~종료 날짜 사이의 가격변화를 데이터로 보여줌
    data = yf.download(ticker, start= start_date, end= end_date)
    st.dataframe(data)
    #Line Chart, Candle Stick 선택형으로 만들기
    chart_type = st.sidebar.radio("Select Chart Type", ("Candle_Stick", "Line"))
    candlestick = go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'])
    line = go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close')
    

    if chart_type == "Candle_Stick":
        fig = go.Figure(candlestick)
    elif chart_type == "Line":
        fig = go.Figure(line)
    else:
        st.error("error")

    fig.update_layout(title=f"{ticker} Stock {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)
    
    
if __name__ == "__main__":
    main()