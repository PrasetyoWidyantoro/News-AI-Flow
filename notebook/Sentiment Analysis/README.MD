# Interactive Sentiment Analysis System for News Articles

## Introduction

In the era of rapidly evolving news, manually analyzing the emotional tone (positive, negative, neutral) of articles can be time-consuming. An automated system for **Sentiment Prediction** is essential to classify the sentiment of news articles, enabling users to quickly gauge the tone and react accordingly.

## Problem
How can we automate the process of analyzing the sentiment of news articles (positive, negative, neutral) and provide accurate, real-time predictions to the user?

## Solution

Develop an interactive **Sentiment Analysis** system that automates the process of predicting the sentiment (positive, negative, neutral) of news articles. This involves leveraging pre-trained NLP models, fine-tuned on specific news sentiment datasets, and evaluating the system with metrics like **Accuracy** and **F1 Score**.

## Business Metrics

- **User Engagement**: The frequency with which users interact with the sentiment analysis feature.
- **Sentiment Accuracy**: The precision with which the system classifies news sentiment (positive, negative, neutral).
- **User Retention**: Indicates whether users continue using the sentiment feature over time.

## Machine Learning Metrics

- **Accuracy**: Measures the proportion of correctly classified sentiments.
- **F1 Score**: A weighted average of precision and recall, providing a balanced view of the system's performance in classifying sentiment.

## Data Understanding & Data Preparation

### Dataset 1: [Kaggle News Sentiment Dataset](https://www.kaggle.com/datasets/hoshi7/news-sentiment-dataset)

This dataset contains over 300,000 rows of news articles with the following features:
- **News Title**: Titles of the news articles.
- **Reddit Title**: Reddit title when sourced from Reddit.
- **Sentiment**: Binary indicator of sentiment (0 = negative, 1 = positive).
- **Text**: Full text of the news articles.
- **URL**: Links to the full articles for further analysis.

### Dataset 2: [Sehyun News Sentiment Dataset](https://huggingface.co/datasets/sehyun66/News-sentiments)

This dataset focuses on financial news and includes:
- **Headline**: Title of the news article.
- **Summary**: Overview of the article.
- **Headline Sentiment**: Sentiment score for the headline.
- **Summary Sentiment**: Sentiment score for the summary.

### Data Preprocessing

To prepare the datasets for model training:
- Text is preprocessed to remove unnecessary symbols, links, and special characters.
- Text normalization techniques (lowercasing, tokenization) are applied.
- Datasets are split into **train** (80%) and **validation** (20%) sets for model training and evaluation.

## Model Development

### AI Model Architecture

- **DistilBERT-base-uncased**: A transformer-based model optimized for faster performance while retaining the accuracy of BERT. It is capable of detecting sentiment and emotions like sadness, joy, anger, fear, and surprise in texts.

### Specialized Adaptations

- **Fine-Tuning**: Models were fine-tuned on the **hoshi7** and **sehyun66** sentiment datasets, adjusting for sentiment classification (positive, negative, neutral).
- **Evaluation Metrics**: **F1 Score** and **Accuracy** were used to measure model performance.

## Training Process

The models were trained using the **TrainingArguments** from the **Transformers** library, saving checkpoints at each epoch, and loading the best-performing model at the end.

### Key Hyperparameters:
- **Learning Rate**: 2e-5
- **Batch Size**: 16 (training and evaluation)
- **Epochs**: 5
- **Weight Decay**: 0.01

### Optimization Techniques:
- Save and evaluate model performance at the end of each epoch.
- Automatically load the best-performing model for final evaluation.
- Models were pushed to Hugging Face for broader usage and sharing.

## Evaluation Metrics

Models were evaluated on the validation sets from both datasets using **Accuracy** and **F1 Score**.

## Results

The performance of the **DistilBERT-base-uncased** model on the two datasets is as follows:

| Model                           | Dataset                               | Accuracy (%)        | F1 Score (%)       |
|----------------------------------|---------------------------------------|---------------------|--------------------|
| **DistilBERT-base-uncased**      | hoshi_sentiment_dataset.csv           | 94.49               | 96.97              |
| **DistilBERT-base-uncased**      | sehyun66/News-sentiments              | 99.97               | 66.52              |
| **DistilBERT-base-uncased**      | sehyun66/News-sentiments              | 82.70               | 82.67              |

- On the **hoshi7 dataset**, the model achieved **94.49% accuracy** and an **F1 Score** of **96.97%**.
- On the **sehyun66 dataset**, the model performed well with **99.97% accuracy**, but the F1 score was lower at **66.52%**, indicating some room for improvement in handling the varied nature of financial news sentiment.

### Models Uploaded to Hugging Face

The following models have been uploaded to Hugging Face for broader use and future fine-tuning:

1. [anggari/distil_news_finetune](https://huggingface.co/anggari/distil_news_finetune)
2. [anggari/distil_news_finetune2](https://huggingface.co/anggari/distil_news_finetune2)
3. [ishaq101/headlines_news_sentiment_distil](https://huggingface.co/ishaq101/headlines_news_sentiment_distil)

## Conclusion

- **DistilBERT-base-uncased** demonstrated strong performance, especially on the **hoshi7 dataset**, with an F1 score of **96.97%**.
- While accuracy on the **sehyun66 dataset** was high, further fine-tuning may be necessary to improve the model's performance on financial news sentiment analysis.
- The uploaded models provide a solid foundation for sentiment analysis tasks and can be easily adapted for use in real-world applications.

---