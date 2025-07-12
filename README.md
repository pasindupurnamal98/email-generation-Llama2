# 📧 Email Generator with LLaMA2 + Langchain

Generate **personalized, context-aware emails** from job descriptions using [LLaMA2](https://huggingface.co/meta-llama) (via Groq API), LangChain, and ChromaDB. Ideal for **business outreach**, especially in roles like Business Development or Recruitment.

---

## 🧠 What It Does

💡 Uses job descriptions + your project portfolio to create customized cold emails for outreach.

### 🔧 Features

| Feature                | Description                                                                              |
|------------------------|------------------------------------------------------------------------------------------|
| ✍️ Email Generator      | Personalized emails based on job JD and portfolio history.                             |
| 🧠 LLaMA2 + Groq API    | Powerful natural language generation.                                                   |
| 📚 Vector Search        | ChromaDB stores your portfolio and retrieves relevant context.                         |
| 🌐 Web Scraper          | Scrape job descriptions from websites.                                                 |
| 🔗 LangChain Framework  | Chain components like LLMs, retrievers, and prompts seamlessly.                        |

---

## ✅ Technologies Used

- **Python**
- **LLaMA2** via **Groq API**
- **LangChain**
- **ChromaDB**
- **Pandas**
- **Jupyter Notebook**

---

## 📁 Project Structure

```plaintext
email-generation-llama2/
├── app/
│   ├── chains.py
│   ├── main.py
│   ├── portfolio.py
│   ├── utils.py
│   ├── resource/
│   │   └── my_portfolio.csv
│   ├── imgs/
│   │   ├── architecture.png
│   │   ├── Screenshot 1.png
│   │   └── Screenshot 2.png
│   └── vectorstore/
│       └── chroma.sqlite3
├── email_generator.ipynb
├── tutorial_chromadb.ipynb
```

> 🖼️ **Visuals**  
- 📌 Check out the app **architecture** and **demo screenshots** in `/app/imgs`.

---

## 🚶‍♂️ Quick Start - Installation & Setup

```bash
# 1. Clone the repo
git clone https://github.com/your-username/email-generation-llama2.git
cd email-generation-llama2

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate          # (or venv\Scripts\activate on Windows)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup your GROQ API key
export GROQ_API_KEY=your_api_key  # or add this to a .env file
```

🧠 **Note:** Make sure `my_portfolio.csv` includes your past projects.

---

## 🚀 Usage Guide

- 🔹 Run `email_generator.ipynb` to generate emails from job descriptions.
- 🔹 Use `tutorial_chromadb.ipynb` to explore vector store functionality.
- 🔹 Portfolio used for context lives in `resource/my_portfolio.csv`.

---

## 🔍 Real-World Use Case: Business Development

### 🏢 Problem
Nike needs a **Principal Software Engineer**. Their traditional hiring is slow and resource-heavy.

### 💡 Solution
Kevin, a **Business Development Executive** at AtliQ, uses this tool to:

- Scrape Nike's job description.
- Match it with AtliQ's portfolio from ChromaDB.
- Auto-generate a pitch email showcasing relevant expertise.

📬 Email is tailored, persuasive, and **ready to send**.

> Check out **`email_generator.ipynb`** to see this use-case in action!

---

## 🙏 Credits

This project is **inspired** by the amazing tutorials from **[Codebasics](https://www.youtube.com/@codebasics)** 🙌  
> 🌟 Special thanks for clear, practical LLM + business use-case walkthroughs.

---

## ⚖️ License

MIT License – You're free to use, modify, and share.  
Don’t forget to add a proper `LICENSE` file if you haven't yet!

---

## 👀 Want More?

🔧 Try extending this tool to:

- Generate cover letters  
- Create product outreach emails  
- Summarize JDs for quick review

---

If you like this project, don’t forget to ⭐️ the repo and explore other real-world AI solutions!

---

Let me know if you'd like a separate `LICENSE.md`, contribution guidelines, or GitHub actions too!
