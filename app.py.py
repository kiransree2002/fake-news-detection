import streamlit as st
import joblib

# Load trained model
model = joblib.load("fake_news_model.pkl")

# Page title
st.title("📰 Fake News Detection")

st.write("Enter a news article below to check whether it is Fake or Real.")

# Text input
news_text = st.text_area("Enter News Article")

# Prediction button
if st.button("Predict"):

    if news_text.strip() == "":
        st.warning("Please enter a news article.")

    else:
        prediction = model.predict([news_text])[0]

        if prediction == 1:
            st.success("This news is REAL")
        else:
            st.error("This news is FAKE")