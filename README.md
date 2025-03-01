```markdown
# Agentic Web Crawler

This project demonstrates an AI-powered agentic web crawler that answers user queries by combining web search results with a large language model (LLM).  It uses Tavily for web searching, Groq's LLMs for answer generation, and Streamlit for a user-friendly interface.

## Key Features

* **Web Search with Tavily:**  Uses the Tavily API to retrieve relevant web pages based on user queries.
* **Groq LLM Integration:** Leverages Groq's large language models (like `llama-3.3-70b-versatile`) to generate comprehensive answers.
* **LangChain Framework:** Employs LangChain for managing the LLM interaction, prompting, and chaining operations.
* **LangGraph Framework:** Utilizes LangGraph for creating and managing the agent's workflow.
* **Streamlit UI:** Provides an interactive Streamlit web application for easy user interaction.
* **Dynamic Prompting:**  Constructs prompts dynamically, incorporating the user's query and relevant search results.
* **Content Truncation:**  Truncates lengthy content from search results for better display in the UI.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mybarefootstory/Agentic-Web-Crawler-.git
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API keys:**
   - Create a `.env` file in the project's root directory.
   - Add your Groq and Tavily API keys to the `.env` file:
     ```
     GROQ_API_KEY=your_groq_api_key
     TAVILY_API_KEY=your_tavily_api_key
     ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run front-end.py
   ```

2. **Enter your query:** Type your question in the text area provided.

3. **Click "Ask Agent!":** The app will perform a web search using Tavily, process the results, and generate an answer using the selected Groq LLM.  The search results (URLs and truncated content) and the final answer will be displayed in the app.

## Example

**Query:** "What are the 10 best stocks to buy in 2024?"

The app will display the top 5 search URL based results from Tavily that best relates to this query, followed by a concise answer generated by the Groq LLM based on the combined content of those search results.

## Dependencies

The project relies on the following key libraries:

* `python-dotenv`: For managing environment variables.
* `langchain_groq`: For interacting with Groq's LLMs.
* `langchain_community`: For additional LangChain tools and integrations.
* `langgraph`: For building and managing the AI agent's workflow.
* `streamlit`: For creating the interactive web application.
* `ipykernel`: For running Python code in Jupyter environments (if needed).
* `tavily-python`: For using the Tavily search API.









