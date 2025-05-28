
import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Community Crisis Resource Map - Decatur, IL")

df = pd.read_csv("resources.csv")

# Filter
resource_type = st.selectbox("Select Resource Type", options=["All"] + df["Type"].unique().tolist())
if resource_type != "All":
    df = df[df["Type"] == resource_type]

st.map(df[["Latitude", "Longitude"]])
st.dataframe(df)
