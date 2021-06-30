import streamlit as st
st.title('CALCULATOR ')
a=st.text_input('enter first number')
b=st.text_input('enter second number')
select=st.selectbox("options",("ADDITION","SUBTRACTION","MULTIPLICATION","DIVISION"))
if select=="ADDITION":
  calc=int(a)+int(b)
if select=="SUBTRACTION":
  calc=int(a)-int(b)
if select=="MULTIPLICATION":
  calc=int(a)*int(b)
if select=="DIVISION":
  calc=int(a)/int(b)
if st.button("RESULT"):
  st.title(f'result of {select} of {a} and {b} is {calc}')
