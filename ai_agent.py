# Step 1: Setup API Keys for Groq, OpenAI and Tavily
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
# print(GROQ_API_KEY)


# Step 2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_deepseek import ChatDeepSeek
from langchain_community.tools.tavily_search import TavilySearchResults


groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
deepseek_llm = ChatDeepSeek(model="deepseek-r1-distill-qwen-32b")
groq_llm2= ChatGroq(model="mixtral-8x7b-32768",temperature=0.0,
    max_retries=2,)


search_tool = TavilySearchResults(max_results=2)


# Step 3: Setup AI Agent with search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt = "Act as an AI chatbot who is smart and friendly"

agent = create_react_agent(
    model=groq_llm,
    tools=[search_tool],
    state_modifier=system_prompt,
)

query = "Tell me about the trends in crypto markets"
state = {"messages":query}
response = agent.invoke(state)
messages = response.get("messages")
ai_messages = [message.content for message in messages if isinstance(message, AIMessage)] #Picking only AIMessage
print(ai_messages[-1])

# Code to invoke other groq LLM 2
# messages = [
#     ("system", "You are a helpful translator. Translate the user sentence to French."),
#     ("human", "I love programming."),
# ]
# groq_llm2.invoke(messages)






