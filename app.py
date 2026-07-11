import streamlit as st
from google import genai

# 1. Set up the page config first
st.set_page_config(
    page_title="AI Learning Buddy Pravallika",
    page_icon="🎓"
)

# 2. Retrieve the secret API key safely from Streamlit's environment
try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
    # Initialize the modern GenAI client
    client = genai.Client(api_key=API_KEY)
except KeyError:
    st.error("Missing Google API Key! Please add it to your Streamlit Secrets.")
    st.stop()
except Exception as e:
    st.error(f"Initialization error: {e}")
    st.stop()

# 3. Build the Streamlit UI
st.title("🎓 AI Learning Buddy Pravallika")

topic = st.text_input("Enter a Topic", placeholder="e.g., Photosynthesis, Quantum Physics")

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
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating response..."):
            if option == "Explain Concept":
                prompt = f"Explain {topic} in simple language for a beginner."
            elif option == "Real-Life Example":
                prompt = f"Give one simple real-life example of {topic}."
            elif option == "Generate Quiz":
                prompt = f"Create 5 MCQs on {topic} with answers."
            else:
                prompt = topic

            try:
                # Call the recommended gemini-2.5-flash model
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred while generating content: {e}")
