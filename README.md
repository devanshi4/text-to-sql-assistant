# 🎬 AI-Powered SQL Database Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-orange)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-green)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)

### 🚀 Project Overview
This application bridges the gap between non-technical business stakeholders and complex SQL databases. By leveraging **Generative AI (OpenAI GPT-3.5)** and **LangChain**, it allows users to ask questions in plain English (e.g., *"Which movie category generated the highest revenue?"*) and receive accurate, data-backed answers immediately.

The system automatically translates natural language into SQL queries, executes them against a live **PostgreSQL** database (DVD Rental Schema), and presents the results in an interactive dashboard.

### 📸 Application Demo
![App Demo](demo.png)
*(The AI Agent successfully navigating a complex Join across 3 tables: Payment → Rental → Inventory → Film)*

---

### 💼 Business Value & Problem Solved
**The Problem:**
Business analysts and managers often need quick insights from databases but lack the SQL expertise to query complex schemas. This leads to a dependency on data teams for basic reports, creating bottlenecks.

**The Solution:**
This Self-Service AI Tool empowers stakeholders to:
* **Reduce Ad-Hoc Requests:** Answer 80% of routine data questions instantly without engineering support.
* **Accelerate Decision Making:** Cut down "time-to-insight" from hours to seconds.
* **Democratize Data:** Make the 15-table DVD Rental dataset accessible to anyone on the team.

---

### 🛠️ Technical Architecture
The application uses a **Retrieve-Then-Generate** architecture:
1.  **User Input:** Natural language query via Streamlit.
2.  **Schema Retrieval:** LangChain inspects the PostgreSQL table definitions.
3.  **SQL Generation:** OpenAI GPT-3.5 translates the prompt + schema into a valid SQL query.
4.  **Execution:** The query is run against the local PostgreSQL database using `psycopg2`.
5.  **Response:** The raw data is formatted into a natural language summary and displayed.

**Key Features:**
* **Complex Query Handling:** Capable of generating `JOINs`, `GROUP BY`, and aggregations.
* **Error Correction:** If the LLM generates invalid SQL, the agent catches the database error, feeds it back to the LLM, and retries automatically.
* **Secure Connection:** Uses environment variables to manage database credentials and API keys securely.

---

### 💻 How to Run Locally

**1. Clone the Repository**
```bash
git clone [https://github.com/devanshi4/sql-ai-assistant.git](https://github.com/devanshi4/sql-ai-assistant.git)
cd sql-ai-assistant

2 Create Virtual Environment

Bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install Dependencies

Bash
pip install -r requirements.txt

4. Set Up Database Ensure you have a local PostgreSQL instance running with the DVD Rental sample database restored.

5. Run the Application

Bash
streamlit run app.py

📂 Project Structure

Plaintext

├── app.py                  # Main application logic (Streamlit + LangChain)
├── requirements.txt        # List of Python dependencies
├── .gitignore              # Files excluded from Git (passwords, venv)
├── README.md               # Project documentation
└── demo.png                # Screenshot for documentation

🔮 Future Improvements

* Visualization: Add automatic charting (Bar/Line graphs) for numerical results.

* Containerization: Dockerize the application for easy cloud deployment (AWS EC2).

* Open Source LLM: Experiment with Llama-2 or Mistral to run entirely offline.