import re
import time
import nltk
import torch
import logging
import pandas as pd
import streamlit as st
from newspaper import Article
from nltk.tokenize import sent_tokenize
from transformers import pipeline, EncoderDecoderModel, BertTokenizer

nltk.download('punkt_tab')
nltk.download('punkt')



if torch.cuda.is_available():
    device = 'cuda'
    logging.info("GPU enabled")
else:
    device = 'cpu'
    logging.info("GPU disabled, use CPU instead")

### SESSION ###
def clear_session():
    if len(list(st.session_state.keys()))>0:
        for key in st.session_state.keys():
            del st.session_state[key]
    logging.info("Session cleared!")
    return True

### NEWS SCRAPER ###
def is_url(input_text):
    # Regular expression for detecting a valid URL
    url_regex = re.compile(
        r'^(https?:\/\/)?'  # Optional http or https scheme
        r'([\da-z\.-]+)\.'  # Domain name and extension
        r'([a-z\.]{2,6})'   # Top-level domain (TLD)
        # r'([\/\w \.-]*)*\/?$'  # Path
    )
    return re.match(url_regex, input_text) is not None

def cleaning_multiline(input_text):
    multiline_regex = r'\n+'
    return re.sub(multiline_regex,"\n",input_text)
    

def get_news_from_url(input_text):
    is_url_check = is_url(input_text)
    
    if is_url_check: # input is URL
        logging.info("Input text is an URL")
        try:
            article = Article(input_text)
            article.download()
            article.parse()
            title = article.title
            text = article.text
            pub_date = article.publish_date
            return {
                "title":title,
                "text":text,
                "pub_date":pub_date,
            }
        except Exception as E:
            logging.info("Exception: "+str(E))
            return {
                "title":'-',
                "text":'-',
                "pub_date":'-',
            } 
    else: # input is non URL
        logging.info("Input text is not an URL")
        return {
            "title":'-',
            "text":input_text,
            "pub_date":'-',
        }

news_info_template = """
{title} \n
{pub_date} \n
{text}
""".strip()


def clean_text(text):
    # Definisikan pola regex untuk berbagai pembersihan
    url_pattern = re.compile(r'https?://\S+|www\.\S+', re.IGNORECASE)
    hashtag_pattern = re.compile(r'#\w+', re.IGNORECASE)
    double_space_pattern = re.compile(r'\s\s+')
    header_pattern = re.compile(r'^.*?--\s?', re.IGNORECASE)
    video_pattern = re.compile(r'VIDEO:.*?(?:\.\s|$)', re.IGNORECASE)
    text = url_pattern.sub('', text)
    text = hashtag_pattern.sub('', text)
    if '--' in text[:40]:
        text = header_pattern.sub('', text).strip()
    text = video_pattern.sub('', text)
    text = double_space_pattern.sub(' ', text)
    text = text.strip()

    return text

### QA ###
qa = pipeline("question-answering", model="./model/question_answering", device = device)
def prepare_qa(input_text,user_question):
    res = qa(question=user_question, context=clean_text(input_text))
    logging.info(str(res['answer']))
    return res['answer']

### SENTIMENT ###
classifier1 = pipeline("text-classification", model="./model/text_classification/Sentiment-1", device = device)
classifier2 = pipeline("text-classification", model="./model/text_classification/Sentiment-2", device = device)
classifier3 = pipeline("text-classification", model="./model/text_classification/Sentiment-3", device = device)
# classifier4 = pipeline("text-classification", model="./model/text_classification/Sentiment-4", device = device)
def sentiment(input_text,model_name):
    start_time = time.time()
    if model_name=='Sentiment-1':
        mapper_label = {"LABEL_0":"Negative","LABEL_1":"Positive"}
        output = classifier1(input_text)[0]
        output_label = output['label']
        print(f"output: {output}")
        sentiment_result = mapper_label[output_label]
        score = output['score']
        runtime = time.time() - start_time
        return {'sentiment': sentiment_result.capitalize(), 'score': score, 'runtime':runtime}
    elif model_name=='Sentiment-2':
        mapper_label = {"LABEL_0":"Neutral","LABEL_1":"Positive","LABEL_2":"Negative"}
        output = classifier2(input_text)[0]
        output_label = output['label']
        print(f"output: {output}")
        sentiment_result = mapper_label[output_label]
        score = output['score']
        runtime = time.time() - start_time
        return {'sentiment': sentiment_result.capitalize(), 'score': score, 'runtime':runtime}
    elif model_name=='Sentiment-3':
        mapper_label = {"LABEL_0":"Negative","LABEL_1":"Positive"}
        output = classifier3(input_text)[0]
        output_label = output['label']
        print(f"output: {output}")
        sentiment_result = mapper_label[output_label]
        score = output['score']
        runtime = time.time() - start_time
        return {'sentiment': sentiment_result.capitalize(), 'score': score, 'runtime':runtime}
    # elif model_name=='Sentiment-4':
    #     output = classifier4(input_text)[0]
    #     print(f"output: {output}")
    #     sentiment_result = output['label']
    #     score = output['score']
    #     runtime = time.time() - start_time
    #     return {'sentiment': sentiment_result.capitalize(), 'score': score, 'runtime':runtime}

### SUMMARIZATION ###
model = EncoderDecoderModel.from_pretrained("anggari/bert2bertnews")
tokenizer = BertTokenizer.from_pretrained("cahya/bert2bert-indonesian-summarization")
def x_summarizer2(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    if len(input_ids[0])>512:
        input_ids = torch.Tensor(input_ids[0][:512])
        input_ids = torch.reshape(input_ids, (1, 512))
    summary_ids = model.generate(input_ids,
                min_length=20,
                max_length=128*2,
                num_beams=10,
                repetition_penalty=2.5,
                length_penalty=1.0,
                early_stopping=True,
                no_repeat_ngram_size=2,
                use_cache=True,
                do_sample = True,
                temperature = 0.8,
                top_k = 50,
                top_p = 0.95)
    summary_text = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary_text

summ = pipeline("text2text-generation", model="./model/text_summarization/summarization-1", max_length=512, device = device)
def summarizer(input_text, model_name):
    start_time = time.time()
    if model_name=='Summarizer-1':
        res = summ(clean_text(input_text))
        res = res[0]['generated_text']
        logging.info("length input "+str(len(input_text)))
        logging.info("length summarized "+str(len(res)))
        runtime = time.time() - start_time
        return {"result":res, "runtime":runtime}
    elif model_name=='Summarizer-2':
        res = x_summarizer2(input_text)        
        logging.info("length input "+str(len(input_text)))
        logging.info("length summarized "+str(len(res)))
        runtime = time.time() - start_time
        return {"result":res, "runtime":runtime}
