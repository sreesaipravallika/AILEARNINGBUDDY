import streamlit as st
import streamlit.components.v1 as components
import re
from datetime import datetime

st.set_page_config(
    page_title="AI Learning Buddy Pravallika",
    page_icon="🎓",
    layout="centered"
)

# ---------- Session State Setup ----------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "history" not in st.session_state:
    st.session_state.history = []
if "counts" not in st.session_state:
    st.session_state.counts = {"Explain Concept": 0, "Real-Life Example": 0, "Generate Quiz": 0, "Ask Anything": 0}
if "pending_topic" not in st.session_state:
    st.session_state.pending_topic = ""
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "last_option" not in st.session_state:
    st.session_state.last_option = None

# ---------- Theme Colors ----------
if st.session_state.dark_mode:
    bg = "radial-gradient(ellipse at top left, #1a0f2e 0%, #0d0a16 45%, #08060d 100%)"
    card_bg = "linear-gradient(145deg, #15151fcc, #1a0a2ecc)"
    text_color = "#F5F5F5"
    subtitle_color = "#9AA0B4"
else:
    bg = "linear-gradient(180deg, #FFFFFF 0%, #F4F3FB 100%)"
    card_bg = "#F4F3FB"
    text_color = "#1E1F26"
    subtitle_color = "#6B7280"

# ---------- Custom CSS ----------
st.markdown(f"""
    <style>
    .stApp {{
        background: {bg};
    }}
    .main-title {{
        font-size: 2.6rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0px;
        background: linear-gradient(90deg, #FF2CDF, #00E0FF, #7F5AF0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}
    .subtitle {{
        text-align: center;
        color: {subtitle_color};
        font-size: 1.05rem;
        margin-bottom: 1.5rem;
    }}
    .result-card {{
        background: {card_bg};
        border: 1px solid #7F5AF055;
        padding: 1.5rem 1.7rem;
        border-radius: 16px;
        margin-top: 1.2rem;
        line-height: 1.7;
        color: {text_color};
    }}
    div.stButton > button {{
        background: linear-gradient(90deg, #FF2CDF, #7F5AF0, #00E0FF);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.4rem;
    }}
    .metric-box {{
        background: #7F5AF022;
        border-radius: 10px;
        padding: 10px 14px;
        text-align: center;
    }}
    </style>
""", unsafe_allow_html=True)

# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    toggle = st.toggle("🌙 Dark mode", value=st.session_state.dark_mode)
    if toggle != st.session_state.dark_mode:
        st.session_state.dark_mode = toggle
        st.rerun()

    st.markdown("---")
    st.markdown("### 📈 Your Progress")
    total = sum(st.session_state.counts.values())
    st.write(f"**Total generations:** {total}")
    for act, c in st.session_state.counts.items():
        st.write(f"- {act}: {c}")

    st.markdown("---")
    st.markdown("### 📚 Recent Topics")
    if st.session_state.history:
        for i, h in enumerate(reversed(st.session_state.history[-8:])):
            if st.button(f"🔁 {h['topic']} ({h['activity']})", key=f"hist_{i}"):
                st.session_state.pending_topic = h["topic"]
                st.rerun()
    else:
        st.caption("No topics yet — generate one to see it here!")

# ---------- Header ----------
st.markdown('<div class="main-title">🎓 AI Learning Buddy</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your personal study companion</div>', unsafe_allow_html=True)

# ---------- Preset Topic Buttons ----------
st.markdown("**Quick try:**")
preset_cols = st.columns(4)
presets = ["Photosynthesis", "Gravity", "Fractions", "The Water Cycle"]
for col, preset in zip(preset_cols, presets):
    if col.button(preset):
        st.session_state.pending_topic = preset
        st.rerun()

# ---------- Input Section ----------
default_topic = st.session_state.pending_topic if st.session_state.pending_topic else ""
col1, col2 = st.columns([2, 1])
with col1:
    topic = st.text_input("📌 Enter a Topic", value=default_topic, placeholder="e.g., Photosynthesis, Newton's Laws")
with col2:
    option = st.selectbox("🎯 Choose Activity", ["Explain Concept", "Real-Life Example", "Generate Quiz", "Ask Anything"])

st.session_state.pending_topic = ""  # clear after using
generate = st.button("✨ Generate", use_container_width=True)

# ---------- Content Generators ----------
def explain_concept(topic):
    return (
        f"### 📖 {topic} — Explained Simply\n\n"
        f"**1. What it is:** {topic} refers to a specific process, idea, or principle studied in this subject area.\n\n"
        f"**2. Why it matters:** Understanding {topic} builds a foundation for more advanced topics.\n\n"
        f"**3. Key idea:** Focus on *how* {topic} works step-by-step rather than memorizing it.\n\n"
        f"💡 **Tip:** Try explaining {topic} out loud in your own words!"
    )

def real_life_example(topic):
    return (
        f"### 🌍 Real-Life Example of {topic}\n\n"
        f"Think of an everyday situation where **{topic}** shows up naturally — at home, school, or in nature.\n\n"
        f"👉 **Try this:** Look around you right now — can you spot something connected to {topic}?"
    )

def ask_anything(topic):
    return (
        f"### 💬 Exploring: {topic}\n\n"
        f"- Break **{topic}** into smaller parts and examine each one separately.\n"
        f"- Ask: what problem does {topic} solve?\n"
        f"- Find one example and one non-example of {topic}.\n\n"
        f"Keep asking *why* and *how*!"
    )

def build_quiz(topic):
    return [
        {
            "q": f"What is the main idea behind {topic}?",
            "options": ["A core definition related to it", "An unrelated random fact", "A historical date only", "A person's name"],
            "correct": 0
        },
        {
            "q": f"True or False: {topic} only applies in one very specific situation.",
            "options": ["True", "False"],
            "correct": 1
        },
        {
            "q": f"Which approach helps you learn {topic} best?",
            "options": ["Memorizing without understanding", "Breaking it into smaller parts and asking why", "Ignoring examples", "Skipping practice"],
            "correct": 1
        },
    ]

def plain_text(md_text):
    text = re.sub(r"[#*_`]", "", md_text)
    return text

# ---------- Output ----------
if generate:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        st.session_state.counts[option] += 1
        st.session_state.history.append({
            "topic": topic, "activity": option,
            "time": datetime.now().strftime("%H:%M")
        })

        if option == "Explain Concept":
            result = explain_concept(topic)
            st.session_state.quiz_answers = {}
        elif option == "Real-Life Example":
            result = real_life_example(topic)
            st.session_state.quiz_answers = {}
        elif option == "Generate Quiz":
            quiz_items = build_quiz(topic)
            st.session_state.quiz_answers = {"topic": topic, "items": quiz_items, "submitted": False}
            result = f"### 📝 Quiz on {topic}"
        else:
            result = ask_anything(topic)
            st.session_state.quiz_answers = {}

        st.session_state.last_result = result
        st.session_state.last_option = option

# ---------- Render last result (persists across reruns for quiz interaction) ----------
if st.session_state.last_option == "Generate Quiz" and st.session_state.quiz_answers:
    qa = st.session_state.quiz_answers
    st.markdown(f'<div class="result-card">### 📝 Quiz on {qa["topic"]}</div>', unsafe_allow_html=True)
    user_choices = []
    for i, item in enumerate(qa["items"]):
        choice = st.radio(item["q"], item["options"], key=f"quiz_{i}", index=None)
        user_choices.append(choice)

    if st.button("✅ Check my score"):
        score = 0
        for i, item in enumerate(qa["items"]):
            if user_choices[i] == item["options"][item["correct"]]:
                score += 1
        st.success(f"You scored {score} / {len(qa['items'])}")

elif st.session_state.last_result:
    st.markdown(f'<div class="result-card">{st.session_state.last_result}</div>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.download_button(
            "📥 Download as text",
            data=plain_text(st.session_state.last_result),
            file_name=f"{st.session_state.last_option.replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True
        )
    with col_b:
        if st.button("🔊 Read aloud", use_container_width=True):
            spoken_text = plain_text(st.session_state.last_result).replace('"', "'")
            components.html(f"""
                <script>
                var msg = new SpeechSynthesisUtterance("{spoken_text}");
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(msg);
                </script>
            """, height=0)
