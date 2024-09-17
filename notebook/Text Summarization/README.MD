---

# Interactive Summarization System for News Articles

## Introduction

As more users seek efficient ways to consume information, especially from news articles, summarization tools are becoming essential. Users want concise, high-quality summaries that capture the main points of news articles without reading the full content. Currently, there is a gap in providing summaries tailored to different use cases, like extreme summarization or concise summaries.

## Problem

How can we create an effective system that provides both concise summaries and extreme summaries for news articles, catering to various user needs?

## Solution

We aim to develop an interactive summarization system that offers both extreme and concise summaries of news articles. This involves training and fine-tuning models on different datasets to generate summaries with varying levels of detail.

## Business Metrics

- **User Engagement**: Measures how frequently users interact with the summarization tool and their level of satisfaction with the output.
- **Adoption Rate**: Tracks how many users integrate the summarization tool into their workflow.
- **Retention Rate**: High retention suggests users find the summaries valuable enough to return.

## Machine Learning Metrics

- **ROUGE-1**: Measures unigram (word-level) overlap between the generated summary and the reference summary.
- **ROUGE-2**: Evaluates bigram (two-word sequences) overlap.
- **ROUGE-L**: Looks at the longest common subsequence between the generated and reference summaries.
- **ROUGE-LSum**: A variant of ROUGE-L specifically for summarization tasks.

## Data Understanding & Data Preparation

We used two datasets for training and evaluation of the summarization models:

1. **EdinburghNLP/XSum**: The Extreme Summarization dataset.
   - **Document**: Full news article.
   - **Summary**: A single-sentence summary that captures the essence of the article.
   - **ID**: Unique BBC ID for each article.
   - **Dataset Splits**:
     - **Train**: 204,000 articles.
     - **Validation**: 11,300 articles.
     - **Test**: 11,300 articles.

2. **BBC News Summary**: A concise summarization dataset from Hugging Face.
   - **File_path**: News article category (rubric).
   - **Articles**: Full content of the news article.
   - **Summaries**: Brief summary.
   - **Dataset Size**: 2,220 rows.

### Data Splitting

- **Train**: 80% of the dataset.
- **Validation**: 20% of the dataset.

### Data Preprocessing

The dataset was cleaned and preprocessed to ensure high-quality input for the models:
- Removed URLs, special characters, and redundant whitespaces.
- Tokenized the text and prepared it for transformer models.
  
The XSum dataset was used for **extreme summarization** (single-sentence summary), while the BBC News Summary dataset was used for **concise summarization** (multi-sentence summary).

## Model Development

### AI Model Architectures

Two transformer-based models were trained for the summarization tasks:

1. **T5 (Text-to-Text Transfer Transformer)**: Fine-tuned on the **BBC News Summary** dataset to generate concise summaries.
2. **Bert2Bert**: Fine-tuned on the **EdinburghNLP/XSum** dataset for extreme summarization, utilizing BERT as both the encoder and decoder.

### Specialized Adaptations

- **T5**: Trained on the **BBC News Summary** dataset to generate concise, readable summaries.
- **Bert2Bert**: Optimized for generating high-level, one-sentence abstracts using the **XSum** dataset.

### Training Process

Training was conducted using the **Seq2SeqTrainingArguments** from the Hugging Face Transformers library, saving checkpoints at each epoch and loading the best model for final evaluation.

Key hyperparameters used during training:
- **Learning Rate**: 5e-5 (T5) and 3e-5 (Bert2Bert).
- **Batch Size**: 32 (Bert2Bert) and 8 (T5).
- **Epochs**: 5 (T5) and 10 (Bert2Bert).
- **Weight Decay**: 0.01 (Bert2Bert) and 0.03 (T5).

### Optimization Techniques

- Model checkpoints saved and evaluated at each epoch.
- Best model loaded automatically at the end of training.
- Final model pushed to Hugging Face Hub.

## Evaluation Metrics

Both models were evaluated using ROUGE metrics to determine the quality of the generated summaries:

- **ROUGE-1**: Measures unigram overlap.
- **ROUGE-2**: Measures bigram overlap.
- **ROUGE-L**: Measures the longest common subsequence.
- **ROUGE-LSum**: A variant of ROUGE-L specific for summarization.

## Results

The evaluation results for both models are as follows:

### T5 - **BBC News Summary** (Concise Summarization)

| Metric   | Score   |
|----------|---------|
| ROUGE-1  | 0.1904  |
| ROUGE-2  | 0.1313  |
| ROUGE-L  | 0.1733  |
| ROUGE-LSum | 0.1906  |

### BERT2BERT - **EdinburghNLP/XSum** (Extreme Summarization)

| Metric   | Score   |
|----------|---------|
| ROUGE-1  | 0.3193  |
| ROUGE-2  | 0.1864  |
| ROUGE-L  | 0.2903  |
| ROUGE-LSum | 0.3196  |

### Models Uploaded to Hugging Face

The following models have been uploaded to Hugging Face for broader usage:

1. [andreanstev/t5_small_news_summ](https://huggingface.co/andreanstev/t5_small_news_summ)
2. [anggari/bert2bertnews](https://huggingface.co/anggari/bert2bertnews)

## Conclusion

- The **BERT2BERT** model performed best on the extreme summarization task with **ROUGE-1** of 0.3193 and **ROUGE-LSum** of 0.3196.
- The **T5** model was more suitable for generating concise summaries, with a **ROUGE-1** of 0.1904 and **ROUGE-LSum** of 0.1906.
- Both models have been fine-tuned for their respective tasks and uploaded to the Hugging Face Hub for public use.

--- 