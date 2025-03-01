#Step 1: Setup UI with Streamlit (model provider, model, system prompt, query)
from ai_agent import get_response_from_ai_agent
import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI",layout="centered")
st.title("AI Chapbot Agents")
st.write("Create and Interact with the AI Agents...")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","llama3-8b-8192"]

provider = st.checkbox("Groq")
if provider:
    selected_model = st.selectbox("Select Groq Model : ",MODEL_NAMES_GROQ)


allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query: ",height=150, placeholder="Ask Anything...")

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step 2: Connect with backend via URL
        responses,final_answer = get_response_from_ai_agent(user_query,selected_model)

        for response in responses:
            url = response.get("url", "")  # Use .get() to handle missing keys safely
            content = response.get("content", "")
            final_content = content[:400] + "............" if len(content) > 40 else content
            # print(f"URL: {url}\nContent: {content}\n---") # Print with separator for clarity
            st.write(f"URL: {url}\nContent: {final_content}\n\n---")

        st.markdown(f"**Final Response:** {final_answer}")

        # payload={
        #     "model_name":selected_model,
        #     "model_provider":provider,
        #     "system_prompt": system_prompt,
        #     "messages": [user_query],
        #     "allow_search": allow_web_search
        # }
        # response = requests.post(API_URL,json=payload)
        # if response.status_code==200:
        #     response_data = response.json()
        #     if "error" in response_data:
        #         st.error(response_data["error"])
        #     else:
        #         st.subheader("Agent Response")
        #         st.markdown(f"**Final Response:** {response_data}")

        










