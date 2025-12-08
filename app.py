import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI

# ==========================================
# 1. SETUP PAGE
# ==========================================
st.set_page_config(page_title="DVD Rental Analytics", page_icon="🎬")
st.title("🎬 AI Database Assistant: DVD Rental Store")

st.markdown("""
**Connected to:** Local PostgreSQL Database (DVD Rental Schema)
**Tables available:** Customer, Payment, Rental, Inventory, Film, Actor, etc.
""")

# ==========================================
# 2. CONFIGURATION (SIDEBAR)
# ==========================================
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

st.sidebar.subheader("Database Connection")
# Defaulting to common local settings
db_user = st.sidebar.text_input("DB User", value="postgres")
db_password = st.sidebar.text_input("DB Password", type="password")
db_host = st.sidebar.text_input("Host", value="localhost")
db_name = st.sidebar.text_input("Database Name", value="dvdrental")

if not api_key or not db_password:
    st.info("👈 Please enter your OpenAI Key and DB Password in the sidebar.")
    st.stop()

# ==========================================
# 3. CONNECT TO POSTGRESQL
# ==========================================
# URI Format: postgresql+psycopg2://user:password@host:5432/dbname
db_uri = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}"

try:
    db = SQLDatabase.from_uri(db_uri)
    st.sidebar.success("✅ Connected to Database")
except Exception as e:
    st.sidebar.error(f"❌ Connection Failed: {e}")
    st.stop()

# ==========================================
# 4. LANGCHAIN AGENT
# ==========================================
try:
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, api_key=api_key)
    
    # The Agent is the "Brain" that writes SQL
    agent_executor = create_sql_agent(
        llm, 
        db=db, 
        agent_type="openai-tools", 
        verbose=True
    )

    # ==========================================
    # 5. CHAT INTERFACE
    # ==========================================
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