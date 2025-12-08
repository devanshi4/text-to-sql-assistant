# 🤖 AI-Powered SQL Database Assistant

### 🚀 Project Overview
This application bridges the gap between non-technical business stakeholders and complex SQL databases. By leveraging **Generative AI (OpenAI GPT-3.5)** and **LangChain**, it allows users to ask questions in plain English (e.g., *"What is the total revenue from payments?"*) and receive accurate, data-backed answers immediately.

The system automatically translates natural language into SQL queries, executes them against a live **PostgreSQL** database, and presents the results in an interactive interface.

### 🎥 Demo
*(Place your GIF or screenshot here. For now, you can delete this line or add: "Screenshots coming soon")*

### 🛠️ Tech Stack
* **Core Logic:** Python, LangChain (SQL Database Chain)
* **LLM:** OpenAI GPT-3.5 Turbo
* **Database:** PostgreSQL (DVD Rental Schema)
* **Frontend:** Streamlit
* **Data Engineering:** Psycopg2, SQLAlchemy

### 🔑 Key Features
* **Text-to-SQL Conversion:** Automatically generates complex SQL queries (Joins, Aggregations, Group By) from natural language prompts.
* **Schema Awareness:** The agent dynamically reads table schemas (`film`, `customer`, `payment`) to understand relationships.
* **Error Handling:** Self-correction capabilities if the generated SQL syntax is invalid.
* **Security:** Runs locally with environment-variable based API key management.

### 💻 How to Run Locally

**1. Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/ai-sql-assistant.git](https://github.com/YOUR_USERNAME/ai-sql-assistant.git)
cd ai-sql-assistant