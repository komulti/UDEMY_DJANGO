import streamlit as st

st.title("Contact")
st.sidebar.warning("Select a page above.")

if "my_slider" not in st.session_state:
  st.session_state["my_slider"] = 0
if "my_checkbox" not in st.session_state:
  st.session_state["my_checkbox"] = False

st.write("You have entered", st.session_state["my_slider"])
st.write(st.session_state["my_checkbox"])