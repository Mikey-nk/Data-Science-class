import streamlit as st
import pandas as pd

st.title("MICHAEL")

st.subheader("MICHAEL")

st.write("Hello World")
st.write("Michael")

st.caption("MICHAEL")

st.code("""
import streamlit as st

st.title("MICHAEL")

st.subheader("MICHAEL")

st.write("Hello World")
st.write("Michael")

st.caption("MICHAEL")

""")

with st.echo():
    st.write("this is a st.echo() implementation")

st.divider()
st.write("something")
st.write("-------------")

df = pd.read_csv("data.csv")
st.dataframe(df.head())

st.subheader("Editable Dataframe")
edited_df = st.data_editor(df)

st.dataframe(edited_df.head())

st.metric("Temperature", "25°C", "1°C")
st.metric("Humidity", "80%", "-10%")

submit_button = st.button("Submit")
if submit_button:
    st.write("Submitted")