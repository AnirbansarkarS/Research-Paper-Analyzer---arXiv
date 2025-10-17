from transformers import pipeline

# Load summarization model once
summerizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str, max_len: int = 150, min_len: int = 40) -> str:
    if not text:
        return "No abstract available."
    try:
        summary = summerizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error summarizing: {e}"
