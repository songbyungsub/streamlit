import streamlit as st

import pandas as pd
import numpy as np

from datetime import datetime
from time import time

import os # 경로 탐색

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


st.title('st.cache')

@st.cache_data()
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df


# 캐시 사용
a0 = time()
st.subheader('st.cache 사용')

# 여기에 load_data_a 함수 삽입

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# 캐시 미사용
b0 = time()
st.subheader('st.cache 미사용')

# 여기에 load_data_b 함수 삽입

st.write(load_data_b())
b1 = time()
st.info(b1-b0)