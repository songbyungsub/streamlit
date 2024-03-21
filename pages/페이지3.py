import streamlit as st
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

messages = st.container(height=300)
if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {prompt}")