# News Article Summarizer

This project implements a news article summarizer using a Transformer model to provide concise summaries of articles while ensuring factual accuracy and readability. Using the **BART** model from Hugging Face's Transformers library, this tool extracts key points from news articles and outputs a summary of specified length.

## Features

- **Text Extraction**: Automatically extracts text from news article URLs.
- **Summarization**: Generates concise and readable summaries.
- **Accuracy**: Uses pre-trained BART model fine-tuned for summarization.

## Technologies Used

- **Python**
- **Hugging Face Transformers**: For the BART model.
- **Newspaper3k**: For news article scraping and text extraction.

## Installation

### Prerequisites

- Python 3.7 or higher

### Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/news-article-summarizer.git
   cd news-article-summarizer

2. Install dependencies:
   ```
   pip install transformers torch newspaper3k
Usage
Run the script:
   ```
    python summarizer.py
   ```
Enter a news article URL when prompted to receive a concise summary.


Contributing
Feel free to open issues or submit pull requests if you have suggestions for improving this project!

License
This project is licensed under the MIT License.
