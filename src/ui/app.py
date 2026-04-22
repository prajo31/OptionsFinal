import streamlit as st
from src.core.black_scholes import OptionParams, black_scholes_call, black_scholes_put
from src.core.greeks import call_delta, put_delta, gamma, vega, call_theta, put_theta, call_rho, put_rho

st.set_page_config(page_title="Option Pricing App", layout="wide")

st.title("Option Pricing App")
st.caption("Black–Scholes • Greeks • Teaching Mode")

with st.sidebar:
    st.header("Inputs")
    S = st.number_input("Spot price (S)", value=100.0)
    K = st.number_input("Strike price (K)", value=100.0)
    r = st.number_input("Risk-free rate (r)", value=0.05)
    sigma = st.number_input("Volatility (σ)", value=0.2)
    T = st.number_input("Time to maturity (T, years)", value=1.0)
    q = st.number_input("Dividend yield (q)", value=0.0)
    option_type = st.radio("Option type", ["Call", "Put"])
    teaching_mode = st.checkbox("Teaching Mode", value=True)

params = OptionParams(S=S, K=K, r=r, sigma=sigma, T=T, q=q)

col_price, col_greeks = st.columns(2)

with col_price:
    st.subheader("Price")
    if option_type == "Call":
        price = black_scholes_call(params)
    else:
        price = black_scholes_put(params)
    st.metric(label=f"{option_type} price", value=f"{price:,.4f}")

with col_greeks:
    st.subheader("Greeks")
    if option_type == "Call":
        delta = call_delta(params)
        theta = call_theta(params)
        rho = call_rho(params)
    else:
        delta = put_delta(params)
        theta = put_theta(params)
        rho = put_rho(params)
    g = gamma(params)
    v = vega(params)

    st.write(f"**Delta:** {delta:.4f}")
    st.write(f"**Gamma:** {g:.4f}")
    st.write(f"**Vega:** {v:.4f}")
    st.write(f"**Theta:** {theta:.4f}")
    st.write(f"**Rho:** {rho:.4f}")

if teaching_mode:
    st.markdown("---")
    st.subheader("Teaching Mode: Black–Scholes Intuition")
    st.markdown("""
**What is this model doing?**  
Black–Scholes gives a theoretical fair value for a European option.

**Inputs you chose:**
- **S**: current stock price  
- **K**: strike price  
- **r**: risk‑free rate  
- **σ**: volatility  
- **T**: time to maturity  
- **q**: dividend yield  
""")
