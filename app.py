import streamlit as st
import joblib
import numpy as np

model = joblib.load('artifacts/ipo_model.pkl')

st.title('IPO Listing Gain Predictor')
st.subheader('Indian Markets — 2010 to 2025')
st.write('Enter IPO details after subscription closes to predict listing gain')

st.divider()

issue_size = st.number_input('Issue Size (crores)', min_value=1.0, value=500.0)
offer_price = st.number_input('Offer Price (₹)', min_value=1.0, value=200.0)
qib = st.number_input('QIB Subscription (x)', min_value=0.0, value=10.0)
hni = st.number_input('HNI Subscription (x)', min_value=0.0, value=10.0)
rii = st.number_input('RII Subscription (x)', min_value=0.0, value=10.0)
nifty_return = st.number_input('Nifty 14-day Return (%)', min_value=-20.0, max_value=20.0, value=1.0)
month = st.slider('Listing Month', 1, 12, 6)
year = st.slider('Listing Year', 2010, 2025, 2024)

st.divider()

if st.button('Predict Listing Gain'):
    features = np.array([[issue_size, qib, hni, rii, offer_price, month, year, nifty_return]])
    prediction = model.predict(features)[0]
    
    st.metric('Predicted Listing Gain', f'{prediction:.2f}%')
    
    if prediction > 30:
        st.success('Strong listing expected — worth applying')
    elif prediction > 10:
        st.info('Moderate listing expected — apply if funds available')
    elif prediction > 0:
        st.warning('Weak listing expected — consider skipping')
    else:
        st.error('Listing loss expected — skip this IPO')