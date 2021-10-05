import streamlit as st
import info
import plotly as po
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Analytics",layout='wide')

PAGES = {
        "Info":info,
}

st.sidebar.title('Navigator')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
