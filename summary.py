import streamlit as st
from models import summarizer, get_news_from_url


def get_model_desc(model_name):
    if model_name=="Summarizer-1":
        desc = "andreanstev/t5_small_news_summ"
    elif model_name=="Summarizer-2":
        desc = "anggari/bert2bertnews"
    else:
        desc = "no selected model"     
    return desc

# session
if "news" not in st.session_state:
    st.session_state["news"] = ""
if "summary" not in st.session_state:
    st.session_state["summary"] = ""


st.title("🗒️ Text Summarization")
option = st.selectbox("Select your model",
                    ("-","Summarizer-1", "Summarizer-2", ))
desc = get_model_desc(option)

if option!='-':
    st.write("🎯 Model description:", desc)

    txt_input = st.text_area('**Enter News Text/URL**', '', height=90)
    submit = st.button("Submit")

    if submit:
        news = get_news_from_url(txt_input)
        st.session_state["news"] = news["text"]
        summary = summarizer(st.session_state["news"], option)

        st.session_state["summary"] = summary["result"]
        
        for k,v in st.session_state.items():
            if k=='news':
                txt_input = st.text_area('**News Info**', st.session_state["news"], height=60, disabled=True)
            if k=="summary" and st.session_state["summary"]!='':
                st.write("**Summary**")
                display_result = f"""{st.session_state["summary"]}\nruntime: {summary["runtime"]}s"""
                st.info(display_result)