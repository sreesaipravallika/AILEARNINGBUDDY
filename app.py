import streamlit as st

st.set_page_config(
    page_title="AI Learning Buddy Pravallika",
    page_icon="🎓",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        background: linear-gradient(90deg, #7F5AF0, #2CB67D);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        color: #9CA3AF;
        font-size: 1.05rem;
        margin-top: 0px;
        margin-bottom: 2rem;
    }
    .result-card {
        background-color: #1E1F26;
        border-left: 5px solid #7F5AF0;
        padding: 1.4rem 1.6rem;
        border-radius: 12px;
        margin-top: 1.2rem;
        line-height: 1.6;
    }
    div.stButton > button {
        background: linear-gradient(90deg, #7F5AF0, #2CB67D);
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        transition: 0.2s ease;
    }
    div.stButton > button:hover {
        opacity: 0.85;
        transform: scale(1.02);
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("ℹ️ About")
    st.write(
        "**AI Learning Buddy** helps you quickly explore any topic with "
        "explanations, real-life examples, and quizzes."
    )
    st.write("---")
    st.write("Built by **Pravallika** 🎓")
    st.write("Powered by Streamlit")

# ---------- Header ----------
st.markdown('<div class="main-title">🎓 AI Learning Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal study companion — explain, explore, and quiz yourself instantly</div>', unsafe_allow_html=True)

# ---------- Input Section ----------
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("📌 Enter a Topic", placeholder="e.g., Photosynthesis, Newton's Laws")
with col2:
    option = st.selectbox(
        "🎯 Choose Activity",
        ["Explain Concept", "Real-Life Example", "Generate Quiz", "Ask Anything"]
    )

generate = st.button("✨ Generate", use_container_width=True)

# ---------- Content Generators ----------
def explain_concept(topic):
    return (
        f"### 📖 {topic} — Explained Simply\n\n"
        f"**1. What it is:** {topic} refers to a specific process, idea, or principle "
        f"studied in this subject area.\n\n"
        f"**2. Why it matters:** Understanding {topic} builds a foundation for more "
        f"advanced topics that build on it.\n\n"
        f"**3. Key idea:** Focus on *how* {topic} works step-by-step rather than "
        f"memorizing it — that makes it far easier to recall later.\n\n"
        f"💡 **Tip:** Try explaining {topic} out loud in your own words — if you can teach it, "
        f"you understand it!"
    )

def real_life_example(topic):
    return (
        f"### 🌍 Real-Life Example of {topic}\n\n"
        f"Think of an everyday situation where **{topic}** shows up naturally — "
        f"at home, school, or in nature.\n\n"
        f"👉 **Try this:** Look around you right now — can you spot something connected "
        f"to {topic}? Write it down. Connecting concepts to real objects is one of the "
        f"fastest ways to remember them long-term."
    )

def generate_quiz(topic):
    items = [
        f"**1.** What is the main idea behind {topic}?\n&nbsp;&nbsp;&nbsp;a) Option A &nbsp; b) Option B &nbsp; c) Option C &nbsp; d) Option D\n&nbsp;&nbsp;&nbsp;*Answer: a*",
        f"**2.** Which of the following best relates to {topic}?\n&nbsp;&nbsp;&nbsp;a) Option 1 &nbsp; b) Option 2 &nbsp; c) Option 3 &nbsp; d) Option 4\n&nbsp;&nbsp;&nbsp;*Answer: b*",
        f"**3.** True or False: {topic} only applies in one specific situation.\n&nbsp;&nbsp;&nbsp;*Answer: False*",
        f"**4.** Fill in the blank: {topic} is most closely related to ______.\n&nbsp;&nbsp;&nbsp;*Answer: (fill in from your notes)*",
        f"**5.** Explain in your own words why {topic} is important to learn.\n&nbsp;&nbsp;&nbsp;*Answer: (open-ended)*",
    ]
    return f"### 📝 Quiz on {topic}\n\n" + "\n\n".join(items)

def ask_anything(topic):
    return (
        f"### 💬 Exploring: {topic}\n\n"
        f"- Break **{topic}** into smaller parts and examine each one separately.\n"
        f"- Ask: what problem does {topic} solve, or what does it describe?\n"
        f"- Find one example and one non-example of {topic} to sharpen your understanding.\n\n"
        f"Keep asking *why* and *how* — that's the fastest way to really learn **{topic}**!"
    )

# ---------- Output ----------
if generate:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Generating response..."):
            if option == "Explain Concept":
                result = explain_concept(topic)
            elif option == "Real-Life Example":
                result = real_life_example(topic)
            elif option == "Generate Quiz":
                result = generate_quiz(topic)
            else:
                result = ask_anything(topic)

        st.markdown(f'<div class="result-card">{result}</div>', unsafe_allow_html=True)
