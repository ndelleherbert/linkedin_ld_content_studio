# LinkedIn L&D Content Studio

An AI-powered Streamlit web application that transforms a simple topic idea into a **ready-to-publish LinkedIn post** — built for Learning & Development professionals.

---

## What It Does

Many professionals want to share insights on LinkedIn but struggle with:

- Finding reliable, structured information
- Summarizing research quickly
- Writing engaging posts consistently

This app solves that with a **3-step AI pipeline**:

```
Topic Input
     │
     ▼
Research Agent        →  Structured research (trends, stats, examples)
     │
     ▼
Summary Agent         →  6–8 concise bullet points
     │
     ▼
Post Generator        →  120–180 word LinkedIn post
```

---

## Features

### AI Pipeline (`pipeline.py`)

| Step | Function | Output |
|------|----------|--------|
| 1 | `research_topic()` | Structured research with key trends, statistics, examples, opportunities, and risks |
| 2 | `summarize_research()` | 6–8 bullet point summary, optional counterpoint |
| 3 | `create_linkedin_post()` | 120–180 word post with hook, insight, closing question, and hashtags |

### Streamlit UI (`app.py`)

- **Topic input** with audience and tone selectors
- **Run steps independently** or use Run Full Pipeline
- **Editable output panels** — modify research before summarizing, edit summary before posting
- **Live word count** with 120–180 word range validation
- **Download buttons** — export research, summary, and post as `.txt` files
- **Session history** — sidebar stores last 5 runs, click any topic to restore it

---

## Project Structure

```
linkedin-ld-content-studio/
│
├── app.py               # Streamlit UI, session state, pipeline execution
├── pipeline.py          # AI functions: research, summary, post generation
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/linkedin-ld-content-studio.git
cd linkedin-ld-content-studio
```

### 2. Create a Virtual Environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your Anthropic API Key

**Windows (PowerShell)**
```powershell
setx ANTHROPIC_API_KEY "your_api_key_here"
```
Restart your terminal after setting the variable.

**macOS / Linux**
```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Or create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_api_key_here
```

---

## Running the App

```bash
streamlit run app.py
```

The app opens automatically in your browser at:

```
http://localhost:8501
```

---

## How to Use

1. Enter a **topic** in the input field
2. Select your **target audience** and **tone**
3. Optionally check **Include counterpoint / limitation**
4. Click one of the four action buttons:

| Button | What It Does |
|--------|-------------|
| Run Research | Generates structured research for the topic |
| Run Summary | Summarizes existing research into bullet points |
| Generate Post | Writes a LinkedIn post from the summary |
| Run Full Pipeline | Runs all three steps sequentially |

5. Review and edit outputs in the three panels
6. Download any output as a `.txt` file

---

## Configuration Options

### Target Audience

| Option | Description |
|--------|-------------|
| L&D Professionals | Learning & Development practitioners |
| HR Leaders | Human Resources decision-makers |
| Engineering Leaders | Tech leads and engineering managers |
| Founders | Startup and business founders |
| Students | Early-career learners |

### Tone

| Option | Style |
|--------|-------|
| Helpful | Practical and supportive |
| Analytical | Data-driven and precise |
| Storytelling | Narrative-led and engaging |
| Bold | Direct and provocative |

---

## Validation Rules

| Rule | Behavior |
|------|----------|
| Empty topic | Blocks all steps, shows error |
| No research | Blocks summary step |
| No summary | Blocks post generation |
| Post outside 120–180 words | Shows warning message |

---

## Example Output

**Topic:** How AI is transforming corporate learning

**Summary (bullet points)**
```
• AI enables personalized learning paths based on individual skill gaps
• Intelligent platforms can analyze performance data in real time
• On-demand AI tutors support employees at the moment of need
• Microlearning formats improve knowledge retention significantly
• Companies can automate and scale training content creation
• AI-driven learning must remain transparent and free from bias
```

**LinkedIn Post**
```
AI is quietly transforming corporate learning.

For years, organizations relied on generic training programs
that treated every employee the same.

Today, AI enables personalized learning paths, real-time skill
gap analysis, and on-demand coaching through intelligent assistants.

Instead of static courses, employees can now learn at the exact
moment they need knowledge — on any device, at any pace.

But with this opportunity comes responsibility. AI-driven learning
systems must remain transparent, ethical, and free from bias.

Organizations that combine human expertise with AI-powered tools
will build stronger, more adaptable teams.

How is your company using AI in learning and development?

#AI #LearningAndDevelopment #FutureOfWork
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `anthropic` | Claude API client |
| `streamlit` | Web UI framework |
| `python-dotenv` | Environment variable management |
| `pandas` / `numpy` | Data utilities |

Full list available in `requirements.txt`.

---

## Potential Enhancements

- Regenerate buttons for summary and post individually
- Multiple post variations to choose from
- Post quality checklist before publishing
- Hashtag optimization suggestions
- Export directly to LinkedIn drafts
- Engagement analytics integration

---

## License

This project is open-source and available for educational and learning purposes.

---

## Author

**Ndelle Herbert**  
AI Developer · Python Enthusiast · Building AI-powered tools and applications