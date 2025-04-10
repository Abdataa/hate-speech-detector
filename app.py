import streamlit as st
import joblib
import re

# Load model + vectorizer
model = joblib.load("hate_speech_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Label mapping 
    0: "Hate Speech",
    1: "Offensive Language",
    2: "Neither"
}

def clean_text(text):
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text.lower()

st.title("💬 Multi-Class Hate Speech Detector")
st.write("Enter a comment and classify it as Hate Speech, Offensive, or Neither.")

user_input = st.text_area("📝 Your Text:")

if st.button("🔍 Classify"):
    cleaned = clean_text(user_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]
    label = label_map.get(prediction, "Unknown")

    if prediction == 0:
        st.error(f"⚠️ {label}")
    elif prediction == 1:
        st.warning(f"🚫 {label}")
    else:
        st.success(f"✅ {label}")
