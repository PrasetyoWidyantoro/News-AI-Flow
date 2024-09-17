import time
import streamlit as st
from models import get_news_from_url, news_info_template, cleaning_multiline, prepare_qa

# session
if "news" not in st.session_state:
    st.session_state["news"] = ""

if "messages" not in st.session_state:
    st.session_state["messages"] = []


st.title("🗨️ News QA")
txt_input = st.text_area('**Enter News Text/URL**','', height=60)

if len(txt_input)!='':
    submit = st.button("Submit")
    if submit:
        news = get_news_from_url(txt_input)
        news_info = cleaning_multiline(news_info_template.format(title=news['title'],pub_date=news['pub_date'],text=news['text']))
        
        if (news['text'] not in ['-','',None]):
            st.session_state["news"] = news_info
            
        else:
            st.warning("Failed to fetch news from URL, **please check your URL or enter news text**")
            
# Display
for k,v in st.session_state.items():
    if k=='news':
        txt_input = st.text_area('**News Info**', st.session_state["news"], height=60, disabled=True)
    if k=='messages':
        for message in st.session_state["messages"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask something"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    start_time = time.time()
    answer = prepare_qa(st.session_state["news"], prompt)
    runtime = round(time.time()-start_time,2)
    response = f"**Answer:** {answer}\n[runtime: {runtime}s]"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

                