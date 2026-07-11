import streamlit as st
import random

st.set_page_config(page_title="AI Learning Buddy Pravallika", page_icon="🎓")
st.title("🎓 AI Learning Buddy Pravallika")

st.write("Enter any topic, choose what you'd like, and get an instant response!")

topic = st.text_input("Enter a Topic", placeholder="e.g., Photosynthesis, Newton's Laws, Fractions")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

def explain_concept(topic):
    return (
        f"**{topic} — Explained Simply**\n\n"
        f"{topic} is a concept that can be broken down into a few key ideas:\n\n"
        f"1. **What it is:** {topic} refers to a specific process, idea, or principle "
        f"studied in this subject area.\n"
        f"2. **Why it matters:** Understanding {topic} helps build a foundation for "
        f"more advanced topics that build on it.\n"
        f"3. **Key idea to remember:** Focus on *how* {topic} works step-by-step, "
        f"rather than memorizing it — that makes it much easier to recall later.\n\n"
        f"💡 Tip: Try explaining {topic} out loud in your own words — if you can teach it, "
        f"you understand it!"
    )

def real_life_example(topic):
    return (
        f"**Real-Life Example of {topic}**\n\n"
        f"Imagine a everyday situation where {topic} shows up naturally. "
        f"For example, think of a scenario at home, school, or in nature where you might "
        f"observe {topic} in action.\n\n"
        f"👉 Try this: Look around you right now — can you spot something that connects to "
        f"**{topic}**? Write down what you notice. Connecting concepts to real objects around "
        f"you is one of the fastest ways to remember them long-term."
    )

def generate_quiz(topic):
    templates = [
        f"1. What is the main idea behind {topic}?\n   a) Definition A\n   b) Definition B\n   c) Definition C\n   d) Definition D\n   **Answer: a**",
        f"2. Which of the following best relates to {topic}?\n   a) Option 1\n   b) Option 2\n   c) Option 3\n   d) Option 4\n   **Answer: b**",
        f"3. True or False: {topic} only applies in one specific situation.\n   **Answer: False**",
        f"4. Fill in the blank: {topic} is most closely related to ______.\n   **Answer: (student to research and fill in)**",
        f"5. Explain in your own words why {topic} is important to learn.\n   **Answer: (open-ended — check understanding, not a fixed answer)**",
    ]
    return f"**Quiz on {topic}**\n\n" + "\n\n".join(templates) + (
        "\n\n📝 Note: This is a starter quiz template — fill in the specific facts about "
        f"**{topic}** from your notes or textbook to complete it fully."
    )

def ask_anything(topic):
    return (
        f"You asked about: **{topic}**\n\n"
        f"Here's a starting point to explore this:\n"
        f"- Break {topic} into smaller parts and look at each one separately.\n"
        f"- Ask: what problem does {topic} solve, or what does it describe?\n"
        f"- Look for one example and one non-example of {topic} to sharpen your understanding.\n\n"
        f"Keep digging — the best way to really learn **{topic}** is to ask 'why' and 'how' "
        f"at every step!"
    )

if st.button("Generate"):
    if not topic.strip():
        st.warning("Please enter a topic.")
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
            st.markdown(result)
