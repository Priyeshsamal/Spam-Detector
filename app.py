import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

st.title("📩 Spam Message Detector")

message = st.text_area("Enter your message:")

if st.button("Check"):
    data = cv.transform([message])
    result = model.predict(data)[0]

    if result == "spam":
        st.error("🚫 This is SPAM")
    else:
        st.success("✅ This is NOT SPAM")