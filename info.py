import streamlit as st
import pandas as pd
from collections import defaultdict

mycols = ['name','age','height']

# Helper function to load data    
@st.cache(persist=True, allow_output_mutation=True)
def load_data(filename,date = False):
    df = pd.read_csv(filename)
    return df

def app():
    st.title('Info tracker')
    try:
        pd.read_csv('info.csv')
    except:
        pd.DataFrame(columns = mycols).to_csv\
            ('info.csv',index=False)
    st.session_state.df = pd.read_csv('info.csv') 

    col1,col2,col3 = st.columns([1,1,1])
    info = defaultdict(int)
    info['name'] = col1.text_input('What is your name?')
    info['age'] = col2.text_input('What is your age?')
    info['height'] = col3.text_input('What is your height?')
    add = st.button('Add')
    if add:
        st.session_state.df.append(pd.DataFrame(info,index=range(0,1))).to_csv('info.csv',index=False)
        # st.session_state.df = st.session_state.df.append(pd.DataFrame(info,index=range(0,1)))

    delete_entry = st.button('Delete')
    index_selector = st.columns([1,1,1])[0].text_input('Enter row number to delete')

    if delete_entry:
        st.session_state.df.drop(int(index_selector),inplace=True)
        st.session_state.df.to_csv('info.csv',index=False)
    with st.expander('See data'):
        st.write('Collected data')
        st.table(pd.read_csv('info.csv'))

