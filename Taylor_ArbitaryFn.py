import streamlit as st
import matplotlib.pyplot as plt
import jax.numpy as jnp
from jax import grad
# Store the initial value of widgets in session state
from sympy import *
from sympy.abc import X,x
from sympy.parsing.sympy_parser import parse_expr
from math import factorial
st.title("Taylor Approximation")
st.write(
    "This app shows the taylor approximation of a function with varying degrees")
with st.sidebar:
    z = parse_expr(st.text_input('Give an expession', 'sin(x)'))
    z = lambdify(x,z,"jax")
def f(a):
    global z
    return z(a)
def taylor(fun, degree, x_plot, a=0.):
    y = fun(a)
    #st.write(y)
    gradient = grad(fun)
    for i in range(1,degree+1):
        y += (gradient(a)*(x_plot-a)**i)/factorial(i)
        gradient = grad(gradient)
    return y

with st.sidebar:
    # Create a slider for degree
    degree = st.slider("Degree", 1, 15, 1)
    a = st.text_input("about a","0")
a = float(a)
x_plot = jnp.linspace(a-2,a+2, 100)
approximation = taylor(f,degree,x_plot,a)
#st.write(approximation)
x = jnp.linspace(a-2, a+2, 100)
fig, ax = plt.subplots()
ax.plot(x,approximation,label='Approximated Curve')
ax.plot(x,z(x_plot),label='Actual curve')

st.pyplot(fig)