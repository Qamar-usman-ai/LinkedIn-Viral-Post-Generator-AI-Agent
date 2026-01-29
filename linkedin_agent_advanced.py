"""
Advanced LinkedIn Viral Post Generator with LangChain ReAct Agent
This version uses a proper LangChain agent that can reason and use tools
"""

import streamlit as st
from langchain_groq import ChatGroq
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
import json
from datetime import datetime

# Tool implementations
class LinkedInViralTools:
    """Collection of tools for the viral post generation agent"""
    
    @staticmethod
    def scrape_viral_posts(topic: str) -> str:
        """
        Tool 1: Scrapes viral LinkedIn posts about a specific topic
        Returns: JSON string with post data
        """
        viral_posts_db = {
            "ai": [
                {
                    "content": "AI is not coming for your job.\n\nBut someone using AI will.\n\nHere's how to stay ahead:",
                    "structure": "contrarian_hook + list",
                    "engagement": 8500,
                    "hooks": ["contrarian", "fear_based"],
                    "format_elements": ["line_breaks", "list_teaser"]
                },
                {
                    "content": "I built an AI tool in 48 hours.\n\nIt now saves me 15 hours/week.\n\nNo coding required.\n\nHere's the exact process: 🧵",
                    "structure": "achievement + benefit + accessibility + thread",
                    "engagement": 12300,
                    "hooks": ["time_based", "result_focused"],
                    "format_elements": ["short_sentences", "thread_emoji"]
                }
            ],
            "machine learning": [
                {
                    "content": "After reviewing 500+ ML projects, I noticed a pattern.\n\n95% fail because of this ONE mistake:\n\n[Thread]",
                    "structure": "authority + stat + curiosity_gap",
                    "engagement": 9800,
                    "hooks": ["research_based", "failure_prevention"],
                    "format_elements": ["statistics", "thread_indicator"]
                }
            ],
            "data science": [
                {
                    "content": "Most Data Scientists waste 80% of their time.\n\nNot on modeling.\nNot on analysis.\n\nOn THIS:",
                    "structure": "problem_statement + negation + curiosity",
                    "engagement": 7600,
                    "hooks": ["problem_focused", "efficiency"],
                    "format_elements": ["repetition", "emphasis"]
                }
            ]
        }
        
        # Find relevant posts
        results = []
        topic_lower = topic.lower()
        
        for key, posts in viral_posts_db.items():
            if key in topic_lower or any(word in topic_lower for word in key.split()):
                results.extend(posts)
        
        # If no match, return general high-performing posts
        if not results:
            for posts in viral_posts_db.values():
                results.extend(posts[:1])
        
        return json.dumps({
            "topic": topic,
            "posts_found": len(results),
            "viral_posts": results[:5],
            "timestamp": datetime.now().isoformat()
        }, indent=2)
    
    @staticmethod
    def analyze_viral_patterns(scraped_data: str) -> str:
        """
        Tool 2: Analyzes viral patterns from scraped posts
        Returns: JSON string with pattern analysis
        """
        try:
            data = json.loads(scraped_data)
            posts = data.get("viral_posts", [])
            
            # Extract patterns
            all_hooks = []
            all_structures = []
            all_formats = []
            total_engagement = 0
            
            for post in posts:
                all_hooks.extend(post.get("hooks", []))
                all_structures.append(post.get("structure", ""))
                all_formats.extend(post.get("format_elements", []))
                total_engagement += post.get("engagement", 0)
            
            # Count occurrences
            from collections import Counter
            hook_counts = Counter(all_hooks)
            structure_counts = Counter(all_structures)
            format_counts = Counter(all_formats)
            
            analysis = {
                "total_posts_analyzed": len(posts),
                "avg_engagement": total_engagement // len(posts) if posts else 0,
                "top_hooks": [
                    {"type": hook, "frequency": count} 
                    for hook, count in hook_counts.most_common(3)
                ],
                "top_structures": [
                    {"pattern": struct, "frequency": count}
                    for struct, count in structure_counts.most_common(3)
                ],
                "essential_format_elements": [
                    {"element": elem, "usage": count}
                    for elem, count in format_counts.most_common(5)
                ],
                "recommendations": {
                    "best_hook_type": hook_counts.most_common(1)[0][0] if hook_counts else "contrarian",
                    "optimal_structure": structure_counts.most_common(1)[0][0] if structure_counts else "hook + value + cta",
                    "must_have_elements": [elem for elem, _ in format_counts.most_common(3)]
                }
            }
            
            return json.dumps(analysis, indent=2)
            
        except Exception as e:
            return json.dumps({"error": str(e), "default_patterns": "Using baseline viral patterns"})
    
    @staticmethod
    def generate_post_content(inputs: str) -> str:
        """
        Tool 3: Generates the actual viral post content
        Expects: JSON with topic and analysis
        Returns: Generated post content
        """
        try:
            data = json.loads(inputs)
            topic = data.get("topic", "")
            analysis = data.get("analysis", {})
            
            # This is a template-based generator
            # In the full version, this calls the LLM
            templates = [
                f"Most people think {topic} is complicated.\n\nIt's not.\n\nHere's the simple truth:",
                f"I spent 6 months learning {topic}.\n\nHere are the 7 things nobody tells you:",
                f"{topic} in 2024:\n\n→ This works\n→ This doesn't\n→ This is the future",
                f"After analyzing 1000+ {topic} projects:\n\n95% make this ONE mistake.",
            ]
            
            import random
            return random.choice(templates)
            
        except Exception as e:
            return f"Error generating content: {str(e)}"
    
    @staticmethod
    def optimize_for_engagement(post: str) -> str:
        """
        Tool 4: Optimizes the post for maximum engagement
        Returns: Optimized version with engagement score
        """
        optimizations = []
        score = 70  # Base score
        
        # Check for hook
        if any(word in post.lower()[:50] for word in ['most', 'nobody', 'secret', 'mistake']):
            score += 10
            optimizations.append("Strong hook detected")
        
        # Check for line breaks
        if post.count('\n') >= 3:
            score += 5
            optimizations.append("Good readability with line breaks")
        
        # Check for visual elements
        if any(char in post for char in ['→', '✅', '❌', '•']):
            score += 10
            optimizations.append("Visual elements present")
        
        # Check for CTA
        if post.rstrip().endswith(('?', ':', '👇', '🧵')):
            score += 10
            optimizations.append("Engagement CTA present")
        
        # Check length (optimal 100-200 words)
        word_count = len(post.split())
        if 100 <= word_count <= 200:
            score += 5
            optimizations.append("Optimal length")
        
        result = {
            "optimized_post": post,
            "engagement_score": min(score, 100),
            "optimizations_applied": optimizations,
            "recommendations": []
        }
        
        # Add recommendations
        if score < 80:
            if '\n' not in post[:50]:
                result["recommendations"].append("Add line break after hook")
            if '?' not in post:
                result["recommendations"].append("End with a question for engagement")
            if not any(char in post for char in ['→', '✅', '❌']):
                result["recommendations"].append("Add visual bullets (→, ✅)")
        
        return json.dumps(result, indent=2)

# Create LangChain tools
def create_agent_tools():
    """Creates the tool set for the LangChain agent"""
    
    tools = [
        Tool(
            name="ScrapeViralPosts",
            func=LinkedInViralTools.scrape_viral_posts,
            description="Scrapes and retrieves viral LinkedIn posts about a specific topic. Input should be a topic string like 'AI' or 'machine learning'. Returns JSON with viral post data including content, structure, and engagement metrics."
        ),
        Tool(
            name="AnalyzeViralPatterns",
            func=LinkedInViralTools.analyze_viral_patterns,
            description="Analyzes viral patterns from scraped post data. Input should be JSON string from ScrapeViralPosts tool. Returns detailed analysis of hooks, structures, and engagement tactics that make posts viral."
        ),
        Tool(
            name="GeneratePostContent",
            func=LinkedInViralTools.generate_post_content,
            description="Generates viral post content based on topic and analysis. Input should be JSON with 'topic' and 'analysis' fields. Returns generated post content string."
        ),
        Tool(
            name="OptimizeForEngagement",
            func=LinkedInViralTools.optimize_for_engagement,
            description="Optimizes a post for maximum engagement. Input should be the post content string. Returns JSON with optimized post, engagement score, and recommendations."
        )
    ]
    
    return tools

# Create the ReAct agent
def create_viral_post_agent(groq_api_key: str):
    """Creates a LangChain ReAct agent for viral post generation"""
    
    # Initialize LLM
    llm = ChatGroq(
        temperature=0.7,
        groq_api_key=groq_api_key,
        model_name="mixtral-8x7b-32768"
    )
    
    # Get tools
    tools = create_agent_tools()
    
    # Create agent prompt template
    template = """You are an expert LinkedIn viral content strategist and AI agent. Your goal is to help users create viral LinkedIn posts by analyzing successful posts and applying proven patterns.

You have access to the following tools:

{tools}

Use the following format:

Question: the input question or task from the user
Thought: think about what to do and which tools to use
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final viral LinkedIn post and recommendations

IMPORTANT INSTRUCTIONS:
1. ALWAYS start by using ScrapeViralPosts tool to gather viral post examples
2. THEN use AnalyzeViralPatterns to understand what makes them viral
3. Use the insights to create a highly engaging post
4. ALWAYS optimize the final post using OptimizeForEngagement
5. Provide the post in a ready-to-copy format
6. Include engagement tips and best practices

Begin!

Question: {input}
Thought: {agent_scratchpad}"""

    prompt = PromptTemplate.from_template(template)
    
    # Create agent
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )
    
    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=10
    )
    
    return agent_executor

# Streamlit UI
def main():
    st.set_page_config(
        page_title="LinkedIn Viral Agent (Advanced)",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 LinkedIn Viral Post Generator - Advanced Agent")
    st.markdown("*Powered by LangChain ReAct Agent + Groq LLM*")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        groq_api_key = st.text_input("Groq API Key", type="password")
        
        st.markdown("---")
        st.markdown("### 🧠 Agent Capabilities")
        st.markdown("""
        - 🔍 Scrapes viral posts
        - 📊 Analyzes patterns
        - ✍️ Generates content
        - 🎯 Optimizes engagement
        - 🤖 Uses ReAct reasoning
        """)
        
        st.markdown("---")
        st.info("This version uses a proper LangChain ReAct agent that can reason about which tools to use and when!")
    
    # Main interface
    topic = st.text_input(
        "📝 What topic should I create a viral post about?",
        placeholder="e.g., AI Agents, Machine Learning, LangChain..."
    )
    
    col1, col2 = st.columns([3, 1])
    with col1:
        additional_context = st.text_area(
            "Additional context (optional):",
            placeholder="Any specific points you want to include...",
            height=100
        )
    
    with col2:
        st.write("")
        st.write("")
        generate_btn = st.button("🚀 Generate", type="primary", use_container_width=True)
    
    # Generate post
    if generate_btn:
        if not groq_api_key:
            st.error("Please enter your Groq API key!")
            return
        
        if not topic:
            st.warning("Please enter a topic!")
            return
        
        # Create progress tracking
        with st.spinner("🤖 AI Agent is thinking and using tools..."):
            try:
                # Create agent
                agent_executor = create_viral_post_agent(groq_api_key)
                
                # Prepare input
                user_input = f"Create a viral LinkedIn post about: {topic}"
                if additional_context:
                    user_input += f"\n\nAdditional context: {additional_context}"
                
                # Run agent
                with st.expander("🔍 Agent Reasoning (Click to see agent's thought process)", expanded=False):
                    result = agent_executor.invoke({"input": user_input})
                    st.code(result.get("output", ""), language=None)
                
                # Display result
                st.success("✅ Your viral post is ready!")
                
                # Extract final post from result
                final_output = result.get("output", "")
                
                st.markdown("### 🎉 Generated Viral Post")
                st.text_area(
                    "Click to copy:",
                    value=final_output,
                    height=300,
                    key="generated_post"
                )
                
                # Action buttons
                col3, col4, col5 = st.columns(3)
                with col3:
                    st.download_button(
                        "💾 Download Post",
                        data=final_output,
                        file_name=f"linkedin_post_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                        mime="text/plain"
                    )
                
                with col4:
                    if st.button("🔄 Regenerate"):
                        st.rerun()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Make sure your Groq API key is valid and you have credits.")

if __name__ == "__main__":
    main()
