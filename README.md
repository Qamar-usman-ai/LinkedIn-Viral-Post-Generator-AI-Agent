# 🚀 LinkedIn Viral Post Generator AI Agent

An intelligent AI agent that analyzes viral LinkedIn posts and generates high-engagement content using LangChain, Groq LLM, and Streamlit.

## ✨ Features

- 🔍 **Viral Post Analysis**: Scrapes and analyzes top-performing LinkedIn posts
- 📊 **Pattern Recognition**: Identifies what makes posts go viral
- ✍️ **AI Generation**: Creates optimized posts using Groq's free LLM API
- 🎯 **Multi-Tool Pipeline**: Uses LangChain agents with multiple specialized tools
- 🖥️ **Beautiful UI**: Streamlit interface for easy interaction
- 📈 **Engagement Metrics**: Shows predicted viral patterns and engagement

## 🛠️ Technologies Used

- **LangChain**: Agent framework and tool orchestration
- **Groq API**: Fast, free LLM inference (Mixtral-8x7b)
- **Streamlit**: Web interface
- **BeautifulSoup**: Web scraping (simulated for demo)
- **Python 3.8+**

## 📋 Prerequisites

1. Python 3.8 or higher
2. Groq API Key (free at https://console.groq.com)

## 🚀 Quick Start

### 1. Clone or Download the Project

```bash
# Create a new directory
mkdir linkedin-viral-agent
cd linkedin-viral-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Your Free Groq API Key

1. Visit https://console.groq.com
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key (you'll need it in the app)

### 4. Run the Application

```bash
streamlit run linkedin_viral_agent.py
```

The app will open in your browser at `http://localhost:8501`

## 📖 How to Use

1. **Enter Groq API Key**: Paste your API key in the sidebar
2. **Enter Topic**: Type your post topic (e.g., "AI Agents", "Machine Learning")
3. **Configure Options** (Optional): 
   - Choose post style
   - Select CTA type
   - Toggle emojis and bullets
4. **Generate**: Click "🚀 Generate Viral Post"
5. **Copy & Post**: Copy the generated post to LinkedIn!

## 🎯 How It Works

The agent uses a 4-step pipeline:

### Step 1: Scrape Viral Posts
- Analyzes top-performing posts in your niche
- Extracts content structure and engagement metrics

### Step 2: Pattern Analysis
- Identifies common hooks and structures
- Analyzes engagement tactics
- Calculates average engagement metrics

### Step 3: Content Generation
- Uses Groq LLM with viral patterns
- Applies proven content structures
- Ensures optimal length and formatting

### Step 4: Optimization
- Refines hook and CTA
- Optimizes readability
- Ensures authenticity

## 🔧 Customization

### Add Real LinkedIn Scraping

To scrape real LinkedIn posts, you can integrate:

```python
# Option 1: LinkedIn API (requires approval)
from linkedin_api import Linkedin

# Option 2: Web scraping with Selenium
from selenium import webdriver

# Option 3: Third-party services
# - Apify
# - ScrapingBee
# - Bright Data
```

### Change LLM Model

In the code, you can change the Groq model:

```python
llm = ChatGroq(
    temperature=0.7,
    groq_api_key=groq_api_key,
    model_name="llama3-70b-8192"  # or "llama3-8b-8192", "gemma-7b-it"
)
```

### Add More Tools

Extend the agent with additional tools:

```python
from langchain.agents import Tool

# Add image generation
image_tool = Tool(
    name="ImageGenerator",
    func=generate_image,
    description="Generates images for posts"
)

# Add hashtag analyzer
hashtag_tool = Tool(
    name="HashtagAnalyzer",
    func=analyze_hashtags,
    description="Suggests optimal hashtags"
)
```

## 📊 Sample Output

```
I spent 6 months analyzing 10,000+ viral LinkedIn posts.

Here's what actually works in 2024:

→ Start with a bold claim or surprising stat
→ Use visual breaks (emojis, bullets, spacing)
→ Tell a story, not just facts
→ Keep it under 200 words
→ End with a question or CTA

The posts following this? 5x more engagement.

What's your go-to LinkedIn strategy?
```

## 🔐 Security Notes

- Never commit your API keys to version control
- Use environment variables for production
- Consider rate limiting for scraping
- Respect LinkedIn's Terms of Service

## 📈 Best Practices for LinkedIn

1. **Post Timing**: Tuesday-Thursday, 8-10 AM
2. **Engagement**: Respond to comments within first hour
3. **Hashtags**: Use 3-5 relevant hashtags
4. **Consistency**: Post 3-4 times per week
5. **Authenticity**: Add personal stories and insights

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install --upgrade -r requirements.txt
```

### "Invalid API key" error
- Verify your Groq API key
- Check if you have credits remaining
- Regenerate a new key if needed

### Streamlit won't start
```bash
# Try specifying the port
streamlit run linkedin_viral_agent.py --server.port 8502
```

## 🎓 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API Docs](https://console.groq.com/docs)
- [Streamlit Docs](https://docs.streamlit.io/)
- [LinkedIn Algorithm Guide](https://www.linkedin.com/help/linkedin/answer/a524930)

## 🤝 Contributing

Feel free to:
- Add new viral pattern detection
- Implement real LinkedIn API integration
- Improve the UI/UX
- Add more LLM models
- Create new analysis tools

## ⚖️ Legal & Ethical Use

- Use responsibly and ethically
- Don't spam or manipulate engagement
- Respect LinkedIn's Terms of Service
- Add value to your network
- Be authentic in your posts

## 📝 License

This project is for educational purposes. Use responsibly.

## 🙏 Acknowledgments

- Groq for free LLM API
- LangChain team for the amazing framework
- Streamlit for the easy-to-use interface

---

**Made with ❤️ for the LinkedIn community**

Star ⭐ this repo if you found it useful!
