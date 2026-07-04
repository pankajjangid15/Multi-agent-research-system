# 🔬 ResearchMind – Multi-Agent AI Research Assistant

ResearchMind is an AI-powered research assistant that uses multiple AI agents to automate the research process. It searches the web, extracts detailed information, generates a structured research report, and reviews the report for quality.

## ✨ Features

- 🔍 Web search using Tavily API
- 📄 Web scraping with BeautifulSoup
- ✍️ AI-generated research reports
- 🧐 AI report reviewer with scoring
- 🎨 Modern Streamlit interface
- 📥 Download generated reports

## 🛠️ Tech Stack

- Python
- LangChain
- Mistral AI
- Tavily Search API
- BeautifulSoup
- Streamlit

## 🚀 Installation

```bash
git clone https://github.com/yourusername/ResearchMind.git
cd ResearchMind
pip install -r requirements.txt
```

Create a `.env` file:

```env
MISTRAL_API_KEY=your_api_key
TAVILY_API_KEY=your_api_key
```

Run the app:

```bash
streamlit run app.py
```

## 📂 Project Workflow

```
User Query
     │
     ▼
🔍 Search Agent
     │
     ▼
📄 Reader Agent
     │
     ▼
✍️ Writer Chain
     │
     ▼
🧐 Critic Chain
     │
     ▼
Final Research Report
```

## 👨‍💻 Author

**Pankaj Jangid**
