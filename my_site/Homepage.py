import streamlit as st

st.set_page_config(
  page_title="Multipage App",
  page_icon=":house:",
  initial_sidebar_state="expanded",
  layout="centered"
)

st.title("Main Page")
st.sidebar.success("Select a page above.")

st.sidebar.multiselect("Select the emtitles you want to extract", ["PERSON", "ORG", "GPE"])