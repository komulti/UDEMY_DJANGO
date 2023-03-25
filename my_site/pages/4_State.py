from turtle import onclick
import streamlit as st

st.title("State")
st.sidebar.success("Select a page above.")

if "my_slider" not in st.session_state:
  st.session_state["my_slider"] = 5
if "my_checkbox" not in st.session_state:
  st.session_state["my_checkbox"] = False

def form_callback():
  st.write(st.session_state["my_slider"])
  st.write(st.session_state["my_checkbox"])
    
def reset_callback():
  st.session_state["my_slider"] = 0
  st.session_state["my_checkbox"] = False
  

with st.form(key="my_form", clear_on_submit=False):
  slider_input = st.slider("My slider", 0, 10, 5, key="my_slider")
  checkbox_input = st.checkbox("Yes or No", key="my_checkbox")
  submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
  reset_button = st.form_submit_button(label='Reset',on_click=reset_callback)
