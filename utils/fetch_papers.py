import arxiv
import pandas as pd

def fetch_papers(query: str, max_results: int = 10):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for result in search.results():
        papers.append({
            "Title": result.title.strip(),
            "Authors": ", ".join([author.name for author in result.authors]),
            "Published": result.published.strftime("%Y-%m-%d"),
            "Summary": result.summary.strip(),
            "PDF Link": result.pdf_url
        })

    return pd.DataFrame(papers)
