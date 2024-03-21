import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from PIL import Image
import numpy as np
import pandas as pd
import io
import matplotlib.pyplot as plt
import os
from datetime import datetime
from st_pages import Page, show_pages, add_page_title, hide_pages

st.set_page_config(layout="wide")  # fluid
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


df = pd.read_csv('../강북강원국사별전력데이터.csv')
df.drop(df.columns[0], axis=1, inplace=True)
df2 = df.drop([df.columns[0], df.columns[1], df.columns[3]], axis=1)
df2 = df2.transpose()
df2.rename(columns=df2.iloc[0], inplace=True)
df2 = df2.drop(df2.index[0])


def main():
    with st.sidebar:
        st.page_link("login.py", label="Logout", icon="🔐")
        choose = option_menu("App menu", ["절감률 대시보드", "실시간 전력량/전력비", "일일 리포트"],
                             icons=['speedometer2', 'lightning-charge-fill',
                                    'file-earmark-text'],
                             menu_icon="app-indicator", default_index=0,
                             styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#02ab21"},
        }  # css 설정
        )
        
    if choose == "절감률 대시보드":
        page1()
    elif choose == "실시간 전력량/전력비":
        page2()
    elif choose == "일일 리포트":
        page3()


def page1():
    with st.container():
        st.header('절감률 대시보드 페이지 입니다.')
        with st.expander("원본 데이터 보기"):
            st.dataframe(df)
        tab1, tab2, tab3 = st.tabs(
            ["bar_chart", "line_chart", "area_chart"])
        with tab1:
            st.bar_chart(df2)
        with tab2:
            st.line_chart(df2)
        with tab3:
            st.area_chart(df2)


def page2():
    st.header('실시간 전력량/전력비 페이지 입니다.')
    with st.expander("원본 데이터 보기"):
        st.dataframe(df)

    st.sidebar.header('선택')
    headquarter = st.sidebar.selectbox('본부 선택', [
                                       '강북/강원', '강남', '서부', '충남/충북', '전남/전북', '대구/경북', '부산/경남'], index=None, placeholder="본부를 선택해주세요.",)
    center = st.sidebar.selectbox('센터 선택', [
                                  'ICT기술담당', '코어', '서울강북액세스', '강원액세스', '경기북부액세스'], index=None, placeholder="센터를 선택해주세요.",)
    affair = st.sidebar.text_input('조회하고 싶은 국사를 입력해주세요.')

    st.header('Check')

    col1, col2, col3 = st.columns(3)

    with col1:
        if headquarter != None:
            st.write(f'✅선택된 **본부**는 "**{headquarter}**" 광역본부 입니다!')
        else:
            st.write('1️⃣  **본부**를 선택해 주세요!')

    with col2:
        if center != None:
            st.write(f'✅선택된 **센터**는 "**{center}**" 운용센터 입니다!')
        else:
            st.write('2️⃣ **센터**를 선택해 주세요!')

    with col3:
        if affair != '':
            st.write(f'✅입력된 **국사**는 "**{affair}**" 국사 입니다!')
        else:
            st.write('3️⃣ **국사**를 입력해 주세요!')


def page3():
    # 파일 업로드 함수
    # 디렉토리 이름, 파일을 주면 해당 디렉토리에 파일을 저장해주는 함수
    def save_uploaded_file(directory, file):
    # 1. 저장할 디렉토리(폴더) 있는지 확인
    #   없다면 디렉토리를 먼저 만든다.
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 2. 디렉토리가 있으니, 파일 저장
        with open(os.path.join(directory, file.name), 'wb') as f:
            f.write(file.getbuffer())
        return st.success('파일 업로드 성공!')
    
    def upload():
        menu = ['이미지 업로드', 'csv 업로드', 'About']

        choice = st.sidebar.selectbox('메뉴', menu)
        
        if choice == menu[0]:
            st.subheader('이미지 파일 업로드')
            img_file = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
            if img_file is not None: # 파일이 없는 경우는 실행 하지 않음
                print(type(img_file))
                print(img_file.name)
                print(img_file.size)
                print(img_file.type)

                # 유저가 올린 파일을,
                # 서버에서 처리하기 위해서(유니크하게) 
                # 파일명을 현재 시간 조합으로 만든다. 
                current_time = datetime.now()
                print(current_time)
                print(current_time.isoformat().replace(':', "_") + '.jpg') #문자열로 만들어 달라
                # 파일 명에 특정 특수문자가 들어가면 만들수 없다.
                filename = current_time.isoformat().replace(':', "_") + '.jpg'
                img_file.name = filename

                save_uploaded_file('image', img_file)

                st.image(f'image/{img_file.name}')


        elif choice == menu[1]:
            st.subheader('csv 파일 업로드 ')

            csv_file = st.file_uploader('CSV 파일 업로드', type=['csv'])

            print(csv_file)
            if csv_file is not None:
                current_time = datetime.now()
                filename = current_time.isoformat().replace(':', '_') + '.csv'

                csv_file.name = filename

                save_uploaded_file('csv', csv_file)

                # csv를 보여주기 위해 pandas 데이터 프레임으로 만들어야한다.
                df = pd.read_csv('csv/'+filename)
                st.dataframe(df)


        else :
            st.subheader('이 대시보드 설명')
    if __name__ == '__main__':
        upload()
main()
