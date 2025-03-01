# Step 1: Import necessary libraries and load environment variables
import os
from dotenv import load_dotenv

from langchain_community.tools import TavilySearchResults  # For web searching
from langchain_groq import ChatGroq  # For using the Groq LLM
from langchain.prompts import ChatPromptTemplate  # For creating prompts
from langchain.chains import LLMChain  # For chaining operations

load_dotenv()  # Load environment variables from .env file
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Get the Groq API key
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")  # Get the Tavily API key


# Step 2: Define a function to get a response from the AI agent
def get_response_from_ai_agent(query, selected_model):
    """
    This function takes a user query and a selected LLM model, performs a web search using Tavily,
    and then uses the Groq LLM to generate a final answer based on the search results.
    """

    # Initialize the Tavily search tool
    tool = TavilySearchResults(
        max_results=5,  # Get the top 5 search results
        include_answer=True,  # Include Tavily's own answer (if available)
        include_raw_content=True,  # Include the raw content of the web pages
        include_images=False,  # Include image URLs (if available)
        exclude_domains=[],  # No domains to exclude
        search_depth="advanced",  # Use advanced search settings
    )

    # Execute the search using the provided query
    responses = tool.invoke({"query": query})

    # Extract and combine the content from the search results
    combined_content = "\n\n".join([response.get("content", "") for response in responses])

    # Initialize the Groq LLM with the selected model and a maximum token limit
    groq_llm = ChatGroq(model=selected_model, max_tokens=1000)

    # Create a prompt template that includes the user's query and the combined content
    prompt_template = f"""
    {query}  
    You are an expert AI assistant. Above is the query you need to answer. 
    Use the following information to answer the question:

    {combined_content} 

    Answer concisely and accurately.
    """

    # Create an LLM chain using the prompt template and the Groq LLM
    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=groq_llm, prompt=prompt)

    # Run the LLM chain to generate the final answer
    final_answer = chain.run(context=combined_content)

    # Return both the raw responses and the final answer
    return responses, final_answer


# Example usage (outside the function):
query = "What are the 10 best stocks to buy in 2024?"  # Example query
selected_model = "llama-3.3-70b-versatile"  # Example model (make sure it's available)
responses, final_answer = get_response_from_ai_agent(query, selected_model)

print(final_answer)  # Print the final answer
