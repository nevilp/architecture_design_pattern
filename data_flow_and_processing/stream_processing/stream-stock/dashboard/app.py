import streamlit as st 
import pandas as pd
import sqlite3
import time

st.set_page_config(layout="wide")
st.title(" REAL TIME STOCK PRICE DASHBORD")

conn = sqlite3.connect("stocks.db",check_same_thread=False)

def load_data():
    query = "SELECT * FROM stocks_symbol ORDER BY timestamp DESC limit 100"
    df = pd.read_sql(query,conn)
    return df

while True:
    df = load_data()
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
    time.sleep(1)
    st.rerun()
