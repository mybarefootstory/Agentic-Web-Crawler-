# Step 1: Setup API Keys for Groq, OpenAI and Tavily
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# print(GROQ_API_KEY)


# Step 2: Setup LLM & Tools
from langchain_community.tools import TavilySearchResults
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

def get_response_from_ai_agent(query,selected_model):
    tool = TavilySearchResults(
        max_results=5,
        include_answer=True,
        include_raw_content=True,
        include_images=True,
        exclude_domains=[],
    )

    responses = tool.invoke({"query": query})  # Pass the query variable to invoke

    # for response in responses:
    #     url = response.get("url", "")  # Use .get() to handle missing keys safely
    #     content = response.get("content", "")
    #     print(f"URL: {url}\nContent: {content}\n---") # Print with separator for clarity

    # 1. Extract and combine content
    combined_content = "\n\n".join([response.get("content", "") for response in responses])

    # 2. Set up the Groq LLM
    groq_llm = ChatGroq(model=selected_model,max_tokens = 1000)  # Make sure this model is accessible

    # 3. Create a prompt template
    prompt_template =f"""
    {query}
    You are a expert AI assistant.Above is the query you need to answer. Use the following information to answer the question. : 

    {combined_content}

    Answer concisely and accurately.
    """

    # 4. Create an LLM chain
    prompt = ChatPromptTemplate.from_template(prompt_template)
    chain = LLMChain(llm=groq_llm, prompt=prompt)

    # 5. Run the chain with the combined content
    final_answer = chain.run(context=combined_content)
    return responses,final_answer



    






