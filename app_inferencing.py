import streamlit as st

question_answer_page = st.Page("question_answer.py", title="Question-Answer", icon="🗨️")
sentiment_page = st.Page("sentiment.py", title="Sentiment Analysis", icon="😐")
summary_page = st.Page("summary.py", title="Summarization", icon="🗒️")

pg = st.navigation({"Tools":[question_answer_page,sentiment_page,summary_page]})
st.set_page_config(page_title="News-Analysis-Toolkit", page_icon="🔧")
pg.run()


# HOW TO RUN: streamlit run app_inferencing.py