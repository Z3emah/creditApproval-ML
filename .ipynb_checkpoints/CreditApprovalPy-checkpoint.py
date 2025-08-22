import numpy as np
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler 


model = joblib.load("CreditApproval.pkl")


st.title("Model Demo")
st.markdown("<h2 style = 'text-align: left; color: purple;'> Loan Approval Process</h2>", unsafe_allow_html = True)
#st.markdown("<h4 style = 'text-align: left; color: gray;'> </h4>", unsafe_allow_html = True)
#st.subheader(":hotpink[", divider = "green")
st.divider()

with st.sidebar:
    X1 = st.number_input("A1", min_value = 0, max_value = 1)
    X2 = st.number_input("A2", min_value = 0, max_value = 251)
    X3 = st.number_input("A3", min_value = 0, max_value = 161)
    X4 = st.number_input("A4", min_value = 0, max_value = 2)
    X5 = st.number_input("A5", min_value = 0, max_value = 2)
    X6 = st.number_input("A6", min_value = 0, max_value = 19)
    X7 = st.number_input("A7", min_value = 0, max_value = 8)
    X8 = st.number_input("A8", min_value = 0, max_value = 34)
    X9 = st.number_input("A9", min_value = 0, max_value = 1)
    X10 = st.number_input("A10", min_value = 0, max_value = 1)
    X11 = st.number_input("A11", min_value = 0, max_value = 8)
    X12 = st.number_input("A12", min_value = 0, max_value = 1)
    X13 = st.number_input("A13", min_value = 0, max_value = 2)
    X14 = st.number_input("A14", min_value = 0, max_value = 126)
    X15 = st.number_input("A15", min_value = 0, max_value = 179)
   



if st.button("Ask Oracle"):
    input_data = np.array([[X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15]])
    Prediction = model.predict(input_data)
    if Prediction == 1:
        st.success("Approve Loan")
    else:
        st.error("Deny Loan")
   # st.success(f"Decision: {Prediction}")