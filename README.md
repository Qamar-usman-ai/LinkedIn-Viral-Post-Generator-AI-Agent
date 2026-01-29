# 🚀 LinkedIn Viral Post Generator AI Agent

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/frontend-streamlit-ff4b4b.svg)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/framework-langchain-12d4a6.svg)](https://python.langchain.com/)
[![CI/CD Status](https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent/actions/workflows/main.yml/badge.svg)](https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent/actions)

An intelligent AI agent that researches live viral trends and generates high-engagement LinkedIn content using **LangChain ReAct Agents**, **Groq (Llama 3.3)**, and **Tavily Search**.



---

## ✨ Features

- 🔍 **Viral Post Analysis**: Scrapes and analyzes top-performing LinkedIn posts via live web search.
- 📊 **Pattern Recognition**: Identifies high-converting hooks and content structures.
- ✍️ **AI Generation**: Creates optimized posts using Groq's ultra-fast Llama 3.3 model.
- 🎯 **ReAct Agent Pipeline**: Uses a "Reasoning + Acting" framework to verify trends before writing.
- 🖥️ **Beautiful UI**: Professional Streamlit interface with "Click to Copy" and "Regenerate" features.
- 🧪 **Automated CI/CD**: Integrated GitHub Actions for automated code quality and unit testing.

---

## 🏗️ Modular Architecture

This project follows a professional modular design to ensure scalability and ease of testing.

```text
root/
├── .github/workflows/   # 🤖 CI/CD: Automated Testing (GitHub Actions)
├── app/                 # 🖥️ UI Layer: Streamlit Dashboard
├── src/                 # 🧠 Logic Layer: The AI "Brain"
│   ├── agent.py        # ReAct Agent Core Initialization
│   ├── tools.py        # Specialized Search & Scraping Tools
│   └── prompts.py      # Strategic System Personas
├── tests/               # 🧪 Quality Control: Pytest Unit Tests
├── .env.example         # 🔐 Security: API Key Template
├── requirements.txt     # 📦 Dependencies: Required Libraries
└── README.md            # 📖 Documentation
**in:** Groq (Llama 3.3 70B)  
**Orchestration:** LangChain  
**Search Engine:** Tavily AI  
**UI Framework:** Streamlit  
**Automation:** GitHub Actions (Ruff & Pytest)  

---

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11 or higher.
- Groq API Key (Free).
- Tavily API Key (Free).

### 2. Installation
# Clone the repository
git clone https://github.com/Qamar-usman-ai/LinkedIn-Viral-Post-Generator-AI-Agent.git
cd LinkedIn-Viral-Post-Generator-AI-Agent

# Install dependencies
pip install -r requirements.txt

### 3. Configuration
# Create a .env file in the root directory
cp .env.example .env

# Edit .env and add your GROQ_API_KEY and TAVILY_API_KEY

### 4. Run Application
streamlit run app/streamlit_app.py

---

## 🎯 How It Works

The agent uses a **4-step pipeline** to ensure quality:

1. **Scrape Viral Posts:** Analyzes top-performing posts in your niche using live search.
2. **Pattern Analysis:** Identifies common hooks, structures, and engagement tactics.
3. **Content Generation:** Applies proven viral structures using the Groq LLM.
4. **Optimization:** Refines the Hook and CTA for maximum readability and reach.

---

## 🧪 Testing & Quality Control
We maintain a "Green Checkmark" standard for code quality.

Run tests locally:
pytest tests/

Check code style:
ruff check .

---

## 🔐 Security & Ethics
- **No Hardcoded Keys:** Never commit your API keys. Use environment variables.
- **Rate Limiting:** Be mindful of API limits when scraping/searching.
- **Respect Terms:** Adhere to LinkedIn’s Terms of Service regarding automation and authenticity.
- **Be Authentic:** Always review and edit AI-generated content to match your personal voice.

---

## 🐛 Troubleshooting
- `"Module not found"` error: Run `pip install -r requirements.txt`.
- `"Invalid API key"` error: Verify your keys in the `.env` file or sidebar.
- **Red X on GitHub:** Check the "Actions" tab to see if your code passed the Ruff linter or Pytest.
