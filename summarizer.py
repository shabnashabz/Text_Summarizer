from newspaper import Article
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def fetch_article_text(url):
    """Fetch and parse article text from a given URL."""
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text):
    """Summarize the text using the BART transformer model."""
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def summarize_article(url):
    """Fetches and summarizes an article from a URL."""
    text = fetch_article_text(url)
    summary = summarize_text(text)
    return summary


if __name__ == "__main__":
    # Replace input() with a hardcoded URL for testing
    url = "https://english.mathrubhumi.com/news/kerala/kerala-amphibious-plane-test-flight-1.10067889"
    summary = summarize_article(url)
    print("Summary:", summary)