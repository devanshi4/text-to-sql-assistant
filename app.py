"""Ask questions in plain English about the PostgreSQL DVD Rental database.

A LangChain SQL agent turns each question into SQL, runs it, and answers in plain language.
"""
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# Page
st.set_page_config(page_title="DVD Rental Analytics", page_icon="🎬")
st.title("🎬 AI Database Assistant: DVD Rental Store")

st.markdown("""
**Connected to:** Local PostgreSQL Database (DVD Rental Schema)
**Tables available:** Customer, Payment, Rental, Inventory, Film, Actor, etc.
""")

# Sidebar: API key and database connection
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.subheader("Database Connection")
db_user = st.sidebar.text_input("DB User", value="postgres")
db_password = st.sidebar.text_input("DB Password", type="password")
db_host = st.sidebar.text_input("Host", value="localhost")
db_name = st.sidebar.text_input("Database Name", value="dvdrental")

if not api_key or not db_password:
    st.info("👈 Please enter your OpenAI Key and DB Password in the sidebar.")
    st.stop()

# Connect to PostgreSQL
# Credentials are typed into the sidebar each session and never written to disk.
db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}"

try:
    db = SQLDatabase.from_uri(db_uri)
    st.sidebar.success("✅ Connected to Database")
except Exception as e:
    st.sidebar.error(f"❌ Connection Failed: {e}")
    st.stop()

# LangChain SQL agent
try:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key)

    # The agent reads the schema, writes SQL, runs it, and retries with the error
    # message if the query fails. temperature=0 keeps answers repeatable.
    agent_executor = create_sql_agent(
        llm,
        db=db,
        agent_type="openai-tools",
        verbose=True
    )

    # Chat interface
    user_query = st.text_input("Ask a question about your business:")

    if st.button("Run Analysis"):
        if user_query:
            with st.spinner("Analyzing data..."):
                try:
                    response = agent_executor.invoke(user_query)
                    st.success("Result:")
                    st.write(response['output'])
                except Exception as e:
                    st.error(f"Error: {e}")

except Exception as e:
    st.error(f"Agent Error: {e}")