import streamlit as st
import pandas as pd
from utils.fetch_papers import fetch_papers
from utils.summarizer import summarize_text

st.set_page_config(page_title="Research Paper Analyzer", layout="wide")

st.title("🧠 Research Paper Analyzer")
st.caption("Search and summarize latest papers from arXiv instantly!")

query = st.text_input("🔍 Enter your research topic:", "Artificial Intelligence")
max_results = st.slider("Number of papers to fetch:", 5, 20, 10)

if st.button("Fetch Papers"):
    with st.spinner("Fetching papers..."):
        df = fetch_papers(query, max_results)

    if df.empty:
        st.warning("No results found. Try a different keyword.")
    else:
        st.success(f"✅ Found {len(df)} papers!")
        for i, row in df.iterrows():
            st.markdown(f"### 📄 {row['Title']}")
            st.markdown(f"👨‍🔬 **Authors:** {row['Authors']}")
            st.markdown(f"📅 **Published:** {row['Published']}")
            st.markdown(f"[🔗 View Paper PDF]({row['PDF Link']})")

            with st.expander("🧩 Abstract"):
                st.write(row['Summary'])

            if st.button(f"Summarize #{i+1}", key=i):
                with st.spinner("Summarizing..."):
                    summary = summarize_text(row['Summary'])
                st.markdown("#### ✨ Summary")
                st.info(summary)

            st.divider()
