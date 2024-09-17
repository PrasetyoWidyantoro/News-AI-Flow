import streamlit as st
from models import get_news_from_url, news_info_template, sentiment

 
def get_model_desc(model_name):
    if model_name=="Sentiment-1":
        desc = "ishaq101/headlines_news_sentiment_distil - F1: 0.84; Accuracy: 0.84"
    elif model_name=="Sentiment-2":
        desc = "anggari/distil_news_finetune - F1: 0.67; Accuracy: 0.99"
    elif model_name=="Sentiment-3":
        desc = "anggari/distil_news_finetune2 - F1: 0.96; Accuracy: 0.94"
    # elif model_name=="Sentiment-4":
    #     desc = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    else:
        desc = "no selected model"     
    return desc

# session
if "news" not in st.session_state:
    st.session_state["news"] = ""
if "sentiment" not in st.session_state:
    st.session_state["sentiment"] = {"result":"","score":0.00}


st.title("😐 Sentiment Analysis")

option = st.selectbox("Select your model",
                    ("-","Sentiment-1", "Sentiment-2", "Sentiment-3",))

desc = get_model_desc(option)
if option!='-':
    st.write("🎯 Model description:", desc)
    
    txt_input = st.text_area('**Enter News Text/URL**', '', height=90)
    submit = st.button("Submit")
    
    if submit:
        news = get_news_from_url(txt_input)
        st.session_state["news"] = news["text"]
        sentiment_result = sentiment(news["title"],model_name=option)
        st.session_state["sentiment"]["result"] = sentiment_result["sentiment"]
        st.session_state["sentiment"]["score"] = sentiment_result["score"]
        
        for k,v in st.session_state.items():
            if k=='news':
                txt_input = st.text_area('**News Info**', st.session_state["news"], height=60, disabled=True)
            if k=="sentiment" and st.session_state["sentiment"]["result"]!='':
                sentiment_ = st.session_state["sentiment"]["result"]
                score_ = st.session_state["sentiment"]["score"]
                result = f"{sentiment_} ({score_})\nruntime: {sentiment_result['runtime']}s"
                st.write("**Sentiment**")
                st.info(result)
else:
    st.write("No model selected")





    