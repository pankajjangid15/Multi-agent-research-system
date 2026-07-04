from langchain.tools import tool 
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from dotenv import load_dotenv
from rich import print
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str) -> str:
    """Search the web for recent and reliable information on a topic. Return title, URLs and snippets."""

    result = tavily.search(query=query, max_results=5)

    out = []

    for r in result["results"]:
        out.append(
            f"Title: {r['title']}\n"
            f"URL: {r['url']}\n"
            f"Snippet: {r['content'][:300]}\n"
        )

    return "\n-----\n".join(out)

def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"user-agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["Script","style","nav", "footer"]):
            tag.decompose()
        return soup.get_Text(separator = " ", strip=True)[:3000]
    except Exception as e:
        return f"Could not Scrape URL : {str(e)}"

