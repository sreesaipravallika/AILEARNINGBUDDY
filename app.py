

import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AQ.Ab8RN6IiwRHcKAYdJk4t2VnJuT3ZIcEM31KPeEQ8-g_NpW1H1g")

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy Pallavi",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy Pallavi")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):
    if topic == "":
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."
        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."
        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."
        else:
            prompt = topic

        response = model.generate_content(prompt)
        st.write(response.text)
