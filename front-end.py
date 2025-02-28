#Step 1: Setup UI with Streamlit (model provider, model, system prompt, query)
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI",layout="centered")
st.title("AI Chapbot Agents")
st.write("Create and Interact with the AI Agents...")

system_prompt = st.text_area("Define your AI Agents: ",height=70,placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama3-70b-8192","llama-3.3-70b-versatile"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider",("Groq","OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model : ",MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model : ",MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query: ",height=150, placeholder="Ask Anything...")

API_URL="http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step 2: Connect with backend via URL
        import requests

        payload={
            "model_name":selected_model,
            "model_provider":provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        response = requests.post(API_URL,json=payload)
        if response.status_code==200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

        










