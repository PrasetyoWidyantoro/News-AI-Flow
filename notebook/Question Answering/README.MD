---

# Interactive Q&A System for News Articles

## Introduction

In today's fast-paced world, users seek direct answers to their questions from news articles without sifting through vast amounts of text. However, current platforms don’t offer an efficient way to ask questions and get direct answers based on the content of news articles.

## Problem

How can we create an interactive system that allows users to ask questions about news articles and receive accurate, relevant answers based on the content?

## Solution

Develop an interactive Q&A feature that allows users to ask questions about news articles and get relevant, article-based answers. This involves preprocessing the text, structuring the data for question-answering (QA) tasks, and using pre-trained NLP models for generating answers.

## Business Metrics

- **User Engagement**: Indicates how often users interact with the Q&A feature and their satisfaction levels.
- **Adoption Rate**: Measures how widely the Q&A feature is being used among its target audience.
- **Retention Rate**: High retention implies that users find the Q&A feature useful and continue to engage with it over time.

## Machine Learning Metrics

- **Exact Match (EM)**: Measures how many answers exactly match the ground truth answer. Higher scores indicate more precise answers.
- **F1 Score**: A weighted average of precision and recall, indicating how well the model balances between correctness and completeness in its answers.

## Data Understanding & Data Preparation

The dataset used is the CNN DailyMail dataset at the overlap between the NewsQA question-answering dataset and CNN DailyMail summarization dataset. The dataset consists of **10,400 rows** and **4 columns**.

### Dataset Structure

- **Story**: Full text of the news article.
- **Questions**: List of questions related to the story, aimed at extracting specific information.
- **Answers**: Corresponding answers to the questions, providing details extracted from the story.
- **Summary**: Concise overview of the main points of the story.

### Data Splitting

- **Train**: 80%
- **Validation**: 20%

### Data Preprocessing

The dataset is preprocessed to clean and normalize text data:
- Remove URLs
- Remove Hashtags
- Remove Headers
- Remove Video Mentions
- Remove Double Spaces

Finally, the dataset is **reformatted to the SQuAD format** for question-answering tasks, which includes the story, the questions, and the corresponding answers.

## Model Development

Three transformer-based models were used for question answering (QA) tasks:

### AI Model Architectures

- **BERT-base-uncased**: Transformer-based model with 12 layers, designed for deep contextual understanding.
- **DistilBERT-base-uncased**: A lighter and faster version of BERT, balancing performance with efficiency.
- **google/flan-t5-small**: A variant of the T5 (Text-To-Text Transfer Transformer) model, designed specifically for text generation and understanding.

### Specialized Adaptations

- **Fine-Tuning**: The models were fine-tuned on the NewsQA dataset using the **glnmario/news-qa-summarization** datasets for training.
- **Evaluation Metrics**: Model performance was evaluated using **Exact Match (EM)** and **F1 Score** to measure the accuracy and quality of answers.

### Training & Optimization

Key hyperparameters used during training:
- **Learning Rate**: 2e-5 (BERT and DistilBERT), 5e-5 (T5)
- **Epochs**: 3 (BERT and DistilBERT), 5 (T5)
- **Weight Decay**: 0.01 (BERT and DistilBERT), 0.03 (T5)
- **FP16 Training**: Enabled for faster computation.

### Optimization Techniques

- **Regularization** with weight decay.
- **FP16 Precision** for efficiency.

## Evaluation Metrics

The models were evaluated on the validation set using the following metrics:

- **Exact Match (EM)**: Measures the proportion of answers that exactly match the ground truth.
- **F1 Score**: Measures the balance between precision and recall, giving a more comprehensive view of the model's performance.

## Results

| Model                           | Exact Match (%) | F1 Score (%)     |
|----------------------------------|-----------------|------------------|
| **BERT-base-uncased**            | 48.84           | 63.79            |
| **DistilBERT-base-uncased**      | 41.49           | 55.77            |
| **google/flan-t5-small**         | 13.11           | -                |

The **BERT-base-uncased** model achieved the highest scores with an **Exact Match** of 48.84% and an **F1 Score** of 63.79%.

### Models Uploaded to Hugging Face

In addition to the models evaluated, the following models have been uploaded to Hugging Face for broader usage and further fine-tuning:

1. [Prasetyow12/bert-base-uncased-newsqa-squad-finetuned](https://huggingface.co/Prasetyow12/bert-base-uncased-newsqa-squad-finetuned)
2. [Prasetyow12/distilbert-uncased-newsqa-squad](https://huggingface.co/Prasetyow12/distilbert-uncased-newsqa-squad)
3. [andreanstev/t5_news_qa](https://huggingface.co/andreanstev/t5_news_qa)

## Conclusion

- The **BERT-base-uncased** model performed best for question-answering tasks with an Exact Match of 48.84% and an F1 Score of 63.79%.
- The **DistilBERT** model, while faster, had slightly lower performance but maintained a reasonable balance between efficiency and accuracy.
- The **T5** model, specialized for text generation, yielded lower Exact Match scores, but it could be further fine-tuned for better performance in QA tasks.

---