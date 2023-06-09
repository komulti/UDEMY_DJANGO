import streamlit as st

# https://youtu.be/FOULV9Xij_8
st.title("대출신청")
# st.header(":mailbox: Get In Touch With Me!")


contact_form = """
  <form action="https://formsubmit.co/okloan2022@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="이름" required>
    <input type="email" name="email" placeholder="이메일" required>
    <textarea name="message" placeholder="자세히 설명해주세요"></textarea>
    <button type="submit">Send</button>
  </form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File 
def local_css(file_name):
  with open(file_name) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
local_css("style/style.css")