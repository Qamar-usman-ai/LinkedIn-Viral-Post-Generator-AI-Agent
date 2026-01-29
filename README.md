# 🚀 LinkedIn Viral Post Generator AI Agent

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/frontend-streamlit-ff4b4b.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/framework-langchain-12d4a6.svg)](https://python.langchain.com/)
[![CI/CD Status](https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent/actions/workflows/main.yml/badge.svg)](https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent AI agent that analyzes live viral LinkedIn posts and generates high-engagement content using **LangChain ReAct Agents**, **Groq (Llama 3.3)**, and **Tavily Search**.



---

## ✨ Features

- 🔍 **Viral Post Analysis**: Scrapes and analyzes top-performing LinkedIn posts via real-time web search.
- 📊 **Pattern Recognition**: Identifies high-converting hooks, spacing, and CTA structures.
- ✍️ **AI Generation**: Creates optimized posts using Groq's ultra-fast Llama-3.3-70b model.
- 🎯 **Multi-Tool Pipeline**: Uses a "Reasoning + Acting" (ReAct) framework to verify trends before writing.
- 🖥️ **Professional UI**: Clean Streamlit dashboard with advanced configuration options.
- 📈 **CI/CD Integrated**: Automated quality checks using Ruff (linting) and Pytest (testing).

---

## 🏗️ Modular Architecture

This project follows an industrial-grade modular design to separate reasoning logic from the user interface.

```text
linkedin-agent-pro/
├── .github/workflows/       # 🤖 CI/CD: Automated testing & style checks
├── app/                     # 🖥️ Interface: The Streamlit Web Dashboard
├── src/                     # 🧠 The Brain: Core AI Logic & Tools
│   ├── agent.py            # Agent initialization & ReAct logic
│   ├── tools.py            # Custom skills (Tavily Search)
│   └── prompts.py          # Expert personas & system instructions
├── tests/                   # 🧪 Quality: Automated unit tests
├── .env.example             # 🔐 Security: Template for API keys
├── requirements.txt         # 📦 Dependencies: Required libraries
└── README.md                # 📖 Documentation

🛠️ Tech Stack
Brain: Groq (Llama 3.3 70B)

Orchestration: LangChain

Search Engine: Tavily AI

UI Framework: Streamlit

Automation: GitHub Actions (Ruff & Pytest)

🚀 Quick Start
1. Prerequisites
Python 3.11 or higher.

Groq API Key (Free).

Tavily API Key (Free).

2. Installation
Bash
# Clone the repository
git clone [https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent.git](https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent.git)
cd LinkedIn-Viral-Post-Generator-AI-Agent

# Install dependencies
pip install -r requirements.txt
3. Configuration
Create a .env file in the root directory:

Bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY and TAVILY_API_KEY
4. Run Application
Bash
streamlit run app/streamlit_app.py
🎯 How It Works
The agent uses a 4-step pipeline to ensure quality:

Step 1: Scrape Viral Posts: Analyzes top-performing posts in your niche using live search.

Step 2: Pattern Analysis: Identifies common hooks, structures, and engagement tactics.

Step 3: Content Generation: Applies proven viral structures using the Groq LLM.

Step 4: Optimization: Refines the Hook and CTA for maximum readability and reach.

🧪 Testing & Quality Control
We maintain a "Green Checkmark" standard for code quality.

Run tests locally:

Bash
pytest tests/
Check code style:

Bash
ruff check .
🔐 Security & Ethics
No Hardcoded Keys: Never commit your API keys. Use environment variables.

Rate Limiting: Be mindful of API limits when scraping/searching.

Respect Terms: Adhere to LinkedIn’s Terms of Service regarding automation and authenticity.

Be Authentic: Always review and edit AI-generated content to match your personal voice.

🐛 Troubleshooting
"Module not found" error: Run pip install -r requirements.txt.

"Invalid API key" error: Verify your keys in the .env file or sidebar.

Red X on GitHub: Check the "Actions" tab to see if your code passed the Ruff linter or Pytest.
