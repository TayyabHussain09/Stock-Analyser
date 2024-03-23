import streamlit as st
import pandas as pd
from binance.client import Client

# Initialize Binance client with your API key
api_key = 'ayqeoFUYjYdivkl3KWqPyXRzzidVPDHqorZC39LDcfU4Cs9LT6QQ5kucNvZNzllh'
client = Client(api_key, '')

st.markdown('''# **Binance Price App**
A simple cryptocurrency price app pulling price data from *Binance API*.
''')

st.header('**Selected Price**')

# Get ticker data from Binance API
tickers = client.get_all_tickers()
tickers_df = pd.DataFrame(tickers)

# Custom function for rounding values
def round_value(input_value):
    if input_value > 1:
        return round(input_value, 2)
    else:
        return round(input_value, 8)

col1, col2, col3 = st.columns(3)

# Widget (Cryptocurrency selection box)
col1_selection = st.sidebar.selectbox('Price 1', tickers_df.symbol, index=0)
col2_selection = st.sidebar.selectbox('Price 2', tickers_df.symbol, index=1)
col3_selection = st.sidebar.selectbox('Price 3', tickers_df.symbol, index=2)
col4_selection = st.sidebar.selectbox('Price 4', tickers_df.symbol, index=3)
col5_selection = st.sidebar.selectbox('Price 5', tickers_df.symbol, index=4)
col6_selection = st.sidebar.selectbox('Price 6', tickers_df.symbol, index=5)
col7_selection = st.sidebar.selectbox('Price 7', tickers_df.symbol, index=6)
col8_selection = st.sidebar.selectbox('Price 8', tickers_df.symbol, index=7)
col9_selection = st.sidebar.selectbox('Price 9', tickers_df.symbol, index=8)

# Get the ticker data for the selected cryptocurrencies
col1_data = tickers_df[tickers_df.symbol == col1_selection]
col2_data = tickers_df[tickers_df.symbol == col2_selection]
col3_data = tickers_df[tickers_df.symbol == col3_selection]
col4_data = tickers_df[tickers_df.symbol == col4_selection]
col5_data = tickers_df[tickers_df.symbol == col5_selection]
col6_data = tickers_df[tickers_df.symbol == col6_selection]
col7_data = tickers_df[tickers_df.symbol == col7_selection]
col8_data = tickers_df[tickers_df.symbol == col8_selection]
col9_data = tickers_df[tickers_df.symbol == col9_selection]

# Get the price and percent change for each selected cryptocurrency
col1_price = round_value(float(col1_data.price))
col2_price = round_value(float(col2_data.price))
col3_price = round_value(float(col3_data.price))
col4_price = round_value(float(col4_data.price))
col5_price = round_value(float(col5_data.price))
col6_price = round_value(float(col6_data.price))
col7_price = round_value(float(col7_data.price))
col8_price = round_value(float(col8_data.price))
col9_price = round_value(float(col9_data.price))

# Create a metrics price box
col1.metric(col1_selection, col1_price)
col2.metric(col2_selection, col2_price)
col3.metric(col3_selection, col3_price)
col1.metric(col4_selection, col4_price)
col2.metric(col5_selection, col5_price)
col3.metric(col6_selection, col6_price)
col1.metric(col7_selection, col7_price)
col2.metric(col8_selection, col8_price)
col3.metric(col9_selection, col9_price)

st.header('**All Price**')
st.dataframe(tickers_df)

st.info('Credit: Created by Tayyab Hussain')

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
