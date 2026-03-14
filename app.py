
import streamlit as st
from pipeline import research_topic, summarize_research, create_linkedin_post
import datetime

st.set_page_config(page_title="LinkedIn L&D Content Studio", layout="wide")

st.title("LinkedIn L&D Content Studio")

# -------------------------
# SESSION STATE
# -------------------------

if "research_text" not in st.session_state:
    st.session_state.research_text = ""

if "summary_text" not in st.session_state:
    st.session_state.summary_text = ""

if "post_text" not in st.session_state:
    st.session_state.post_text = ""

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------
# SIDEBAR HISTORY
# -------------------------

st.sidebar.title("History")

for item in st.session_state.history[-5:]:
    if st.sidebar.button(item["topic"]):
        st.session_state.research_text = item["research"]
        st.session_state.summary_text = item["summary"]
        st.session_state.post_text = item["post"]

# -------------------------
# INPUT PANEL
# -------------------------

st.subheader("Topic Input")

topic = st.text_input("Topic")

audience = st.selectbox(
    "Target Audience",
    ["L&D", "HR", "Engineering Leaders", "Founders", "Students"]
)

tone = st.selectbox(
    "Tone",
    ["Helpful", "Analytical", "Storytelling", "Bold"]
)

include_counter = st.checkbox("Include counterpoint / limitation")

col1, col2, col3, col4 = st.columns(4)

run_research = col1.button("Run Research")
run_summary = col2.button("Run Summary")
run_post = col3.button("Generate Post")
run_all = col4.button("Run Full Pipeline")

# -------------------------
# PIPELINE EXECUTION
# -------------------------

if run_research or run_all:

    if topic == "":
        st.error("Topic cannot be empty")
    else:
        with st.spinner("Running research..."):
            st.session_state.research_text = research_topic(topic)

if run_summary or run_all:

    if st.session_state.research_text == "":
        st.error("Run research first")
    else:
        with st.spinner("Creating summary..."):
            st.session_state.summary_text = summarize_research(
                st.session_state.research_text,
                include_counter
            )

if run_post or run_all:

    if st.session_state.summary_text == "":
        st.error("Run summary first")
    else:
        with st.spinner("Writing LinkedIn post..."):
            st.session_state.post_text = create_linkedin_post(
                topic,
                st.session_state.summary_text,
                audience,
                tone
            )

        # Save history
        st.session_state.history.append({
            "topic": topic,
            "time": str(datetime.datetime.now()),
            "research": st.session_state.research_text,
            "summary": st.session_state.summary_text,
            "post": st.session_state.post_text
        })

# -------------------------
# OUTPUT SECTION
# -------------------------

col1, col2, col3 = st.columns(3)

# Research
with col1:
    st.subheader("Research Output")

    research = st.text_area(
        "Research",
        st.session_state.research_text,
        height=300
    )

    st.download_button(
        "Download Research",
        research,
        file_name="research.txt"
    )

# Summary
with col2:
    st.subheader("Summary Output")

    summary = st.text_area(
        "Summary",
        st.session_state.summary_text,
        height=300
    )

    st.download_button(
        "Download Summary",
        summary,
        file_name="summary.txt"
    )
# Post
with col3:
    st.subheader("LinkedIn Post")

    post = st.text_area(
        "Post",
        st.session_state.post_text,
        height=300
    )

    word_count = len(post.split())

    st.write(f"Word Count: {word_count}")

    if word_count < 120 or word_count > 180:
        st.warning("Post should be between 120–180 words")

    st.download_button(
        "Download Post",
        post,
        file_name="linkedin_post.txt"
    )