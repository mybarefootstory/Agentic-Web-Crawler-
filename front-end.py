# Step 1: Set up the Streamlit UI
import streamlit as st
from ai_agent import get_response_from_ai_agent  # Import the agent function

# Configure the Streamlit page
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")  # Set the title of the app
st.write("Create and Interact with the AI Agents...")  # Display a description

# Define the available Groq model names
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "llama3-8b-8192"]

# Create a checkbox for the Groq provider
provider = st.checkbox("Groq")  # User selects if they want to use Groq
if provider:
    # Display a dropdown to select the Groq model
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

# Create a text area for the user's query
user_query = st.text_area("Enter your query:", height=150, placeholder="Ask Anything...")

# Create a button to trigger the agent
if st.button("Ask Agent!"):
    # Check if the user has entered a query
    if user_query.strip():  # Ignore empty queries
        # Step 2: Get the response from the AI agent
        responses, final_answer = get_response_from_ai_agent(user_query, selected_model)

        # Display the search results
        for response in responses:
            url = response.get("url", "")  # Get the URL, handle missing keys
            content = response.get("content", "")  # Get the content, handle missing keys
            final_content = content[:100] + "............" if len(content) > 400 else content  # Truncate content for display
            st.write(f"URL: {url}\n\nContent: {final_content}\n\n---")  # Display URL and truncated content

        # Display the final answer from the LLM
        st.markdown(f"**Final Response:** {final_answer}")

    else:
        st.error("Please enter a query.")