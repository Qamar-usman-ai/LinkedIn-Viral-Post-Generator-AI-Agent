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
