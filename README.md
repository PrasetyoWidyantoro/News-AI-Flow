# News AI Flow: An Integrated AI Pipeline for News Analysis

 --- 

**Introduction**

In today's information-driven world, the sheer volume of news can overwhelm both individuals and businesses, making it challenging to extract meaningful insights. Traditional methods of news analysis often rely on manual effort, consuming valuable time and resources. **News AI Flow** addresses these challenges by providing an AI-powered solution that automates the process of news ingestion, sentiment analysis, content summarization, and interactive Q&A. By leveraging AI, this pipeline helps users efficiently navigate the flood of information, delivering real-time, actionable insights from news articles.

---
News analysis in field of News QnA, Sentiment, and Summary using Streamlit as user interface

**Clone git** \
`$ git clone https://github.com/Ishaq101/News-Analysis-Toolkit-Using-Streamlit.git` \
`$ cd News-Analysis-Toolkit-Using-Streamlit` 

**Create conda env** \
`$ conda create -n venv python=3.10` \
`$ activate venv`

**Install Requirements** \
`$ pip install -r requirements.txt`

**Get Models** \
`$ python save_models.py`

**Run program** \
`$ streamlit run app_inferencing.py`
<br><br>

----
<h3>How to use News Analysis Toolkit?</h3>

<caption><b>Question and Answer</b></caption>

Input: Text or News URL\
Steps:\
1. Enter text/URL in input box
2. Click on `Submit` button
3. Begin your conversation with submitted news in chat box on below of page

Check the video here
[![QnA](./images/qna.jpeg)](./videos/QnA.mp4)

---

<caption><b>Sentiment Analysis</b></caption>

Input: Text or News URL\
Steps: 
1. Enter text/URL in input box
2. Click on `Submit` button
3. News Info and Sentiment will be provided

[![Sentiment Analysis](./images/sentiment.jpeg)](./videos/Sentiment_Analysis.mp4)

---

<caption><b>Summarization</b></caption>

Input: Text or News URL\
Steps: 
1. Enter text/URL in input box
2. Click on `Submit` button
3. News Info and News Summary will be provided

[![Summarization](./images/summarization.jpeg)](./videos/Summarization.mp4)

---

## Future Improvement
Models \
Using model that support multi language.

News Toolkit \
Equipped with ASR (Automatic Speech Recognition) feature as input method options.
