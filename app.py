import json
import requests
import pandas as pd
import streamlit as st
from utils import categorize_tech
from pdfminer.high_level import extract_text

st.set_page_config(page_title="CV Parser")
st.header("Résumé Parser")

API_ENDPOINT = st.secrets["api_url"]
API_KEY = st.secrets["api_key"]

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made with elan by disruptive.dna@gmail.com </p>
</div>
"""

def format_response(response):
    tech_cats=None
    if "workhistory" in response:
        tech_cats = categorize_tech(response["workhistory"])
    return tech_cats


def display_response(response, cats):
    if cats and len(cats) > 0:
        col1, col2 = st.columns(2)
        with col1:
            st.json(response)
        with col2:
            series=[]
            values=[]
            for key in cats:
                series.append(key)
                values.append(round(cats[key]/365,1))
            d = {"technologies": series, "years": values}
            df = pd.DataFrame(data=d)
            chart_data = pd.DataFrame(df)
            st.bar_chart(chart_data, y="years", x="technologies")
    else:
        st.json(response)


def display_dashboard():
    st.write("The most incisive and insightful CV parser. Powered with low footprint NLP and Streamlit!")
    uploaded_file = st.file_uploader("Choose a résumé to parse(only PDFs for now)")
    if uploaded_file:
        with st.spinner("Please wait"):
            cvtext = extract_text(uploaded_file)
            data = { "api_key": API_KEY, "cv_text": cvtext }
            resp = requests.post(url = API_ENDPOINT,json = data)
            if resp.status_code == 200:
                resp = resp.json()
                cats = format_response(resp)
                display_response(resp,cats)
            #print('data is .....',data)
    st.markdown(footer,unsafe_allow_html=True)

#st.header("CV Parser")
display_dashboard()
