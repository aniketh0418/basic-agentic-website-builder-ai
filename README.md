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
git clone https://github.com/aniketh0418/basic-agentic-website-builder-ai.git
cd basic_agentic_website_builder_ai
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
genai.configure(api_key="GEMINI_API_KEY")
```
### 2. Create the output folder
Before running the agent, create the folder where generated files will be stored:
```bash
mkdir generated_site
```

### 3. Install Vercel CLI
```bash
npm install -g vercel
```
Login once:
```bash
vercel login
```
---
## Run the Agent
```bash
python agent.py
```
Example prompt
```bash
Enter website idea: car dealership landing page
```
The generated files will appear in:
```bash
generated_sites/
```
and the site will be deployed automatically using vercel.
