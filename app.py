import streamlit as st
from phi.agent import Agent, AgentMemory
from phi.model.groq import Groq
from phi.model.openrouter import OpenRouter
from phi.tools.tavily import TavilyTools
from phi.memory.db.postgres import PgMemoryDb
from phi.storage.agent.postgres import PgAgentStorage
import datetime

# Initialize Streamlit page configuration
st.set_page_config(
    page_title="Quantitative Trading Assistant",
    page_icon="📈",
    layout="centered"
)

# Database setup for chat history - moved to secrets
DATABASE_URL = st.secrets["DATABASE_URL"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
TAVILY_API_KEY = st.secrets["TAVILY_API_KEY"]

# Initialize Agent with PostgreSQL storage
agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview", api_key=GROQ_API_KEY),
    tools=[TavilyTools(api_key=TAVILY_API_KEY)],
    storage=PgAgentStorage(
        db_url=DATABASE_URL,
        table_name="agent_sessions",
    ),
    memory=AgentMemory(
        db=PgMemoryDb(
            db_url=DATABASE_URL,
            table_name="agent_memory"
        ),
    ),
    add_history_to_messages=True,
    num_history_responses=5,
    show_tool_calls=False,
    description="You are an expert Quantitative Trading Supervisor and mentor, specializing in teaching financial trading concepts.", 
    instructions = [
        "Always answer in a well detailed manner, use scenarios, examples and be detailed",                                                                                                                                                                                                                                                                                                                                                          
        "Answer all questions in detail don't be vague and don't leave any concept untoached", 
        "The goal is for you to teach the user everything there is to know about the question asked",
        "When explaining machine learning concepts, explain in a very basic manner and use visual aids becuase the user does not have any background in math                                                                                                           ",
        "For Machine learning concepts, explain the concepts in visual manner",
        "Whenever explaning a concept, use a mix of theory and real-world applications to enhance understanding",
        "When explaining a concept, and the concept requires some prior knowledge explain the prior knowledge first before explaining the concept",
        "Explain complex trading concepts in simple, understandable terms",
        "Provide real-world trading scenarios and examples to illustrate concepts",
        "Break down quantitative trading strategies and methodologies",
        "Use analogies and practical examples to make financial concepts more accessible",
        "Guide users through trading principles with a focus on risk management",
        "Stay current with market trends using the Tavily search tool",
        "Always maintain a teaching-focused approach, ensuring explanations are clear and practical.",
        "When explaining concepts, use a mix of theory and real-world applications to enhance understanding."
    ]
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.session_id = datetime.datetime.now().isoformat()

# Set the session ID for the agent
agent.session_id = st.session_state.session_id

# Streamlit UI
st.title("Quantitative Trading Assistant 📈")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            # Get response from agent
            response = agent.run(prompt)
            st.markdown(response.content)
            
    # Save to session state
    st.session_state.messages.append({"role": "assistant", "content": response.content}) 