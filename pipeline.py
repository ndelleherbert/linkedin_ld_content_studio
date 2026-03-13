from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# -------------------------
# 1. Research Step
# -------------------------
def research_topic(topic):

    prompt = f"""
    Conduct structured research on the topic below.

    Topic: {topic}

    Provide sections:
    1. Key Trends
    2. Important Statistics
    3. Real World Examples
    4. Opportunities
    5. Risks or Limitations
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


# -------------------------
# 2. Summary Step
# -------------------------
def summarize_research(research_text, include_counterpoint=False):

    counter = "Include one limitation or counterpoint." if include_counterpoint else ""

    prompt = f"""
    Summarize the research below into 6–8 crisp bullet points.

    {counter}

    Research:
    {research_text}
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text


# -------------------------
# 3. LinkedIn Post Step
# -------------------------
def create_linkedin_post(topic, summary_text, audience, tone):

    prompt = f"""
    Write a LinkedIn post about: {topic}

    Audience: {audience}
    Tone: {tone}

    Use this summary:
    {summary_text}

    Requirements:
    - 120 to 180 words
    - Clear hook at the start
    - Practical insight
    - End with a question
    - Include 3 relevant hashtags
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text