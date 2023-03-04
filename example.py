import streamlit as st
from sympy import sin, cos, log, exp
from sympy.abc import x
st.title('Counter Example')

# Streamlit runs from top to bottom on every iteraction so
# we check if `count` has already been initialized in st.session_state.

# If no, then initialize count to 0
# If count is already initialized, don't do anything
if 'count' not in st.session_state:
	st.session_state.count = 0

# Create a button which will increment the counter
increment = st.button('Increment')
if increment:
    st.session_state.count += x

# A button to decrement the counter
decrement = st.button('Decrement')
if decrement:
    st.session_state.count -= cos(x)

st.write('Count = ', st.session_state.count)
