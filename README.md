# AI Website Builder Agent

An agentic AI system that converts a natural language prompt into a deployable frontend website using **Python, Gemini API, and LangGraph**.

The agent plans the website structure, generates frontend code, writes files to disk, and deploys the site automatically using **Vercel CLI**.

---

## Features

- Natural language → website generation
- Agentic workflow using **LangGraph**
- Code generation powered by **Google Gemini**
- Automatic file creation
- Deployment using **Vercel CLI**
- Detailed pipeline logs

---

## Tech Stack

- Python
- Google Gemini API
- LangGraph
- Filesystem tools
- Vercel CLI

---

## Project Structure


---

## Installation

Clone the repository
```bash
git clone
cd
```
Install dependencies
```bash
pip install requirements.txt
```


---

## Setup

### 1. Create a Gemini API key

Get your key from:

https://aistudio.google.com/app/apikey

Add it in `gemini.py`

```python
genai.configure(api_key="YOUR_API_KEY")
