# Step 1: Setup API Keys for Groq, OpenAI and Tavily
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# print(GROQ_API_KEY)

TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


# Step 2: Setup LLM & Tools
# Step 3: Setup AI Agent with search tool functionality