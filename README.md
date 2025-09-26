# SMS-Spam-Classifier

This project is an SMS Spam Classifier built using Machine Learning techniques to distinguish between spam and ham (legitimate) SMS messages. The goal is to provide an efficient and accurate model that can be integrated into real-world applications for detecting unwanted spam messages.

## 📂 Dataset

Source: UCI SMS Spam Classifier Dataset on Kaggle

Description: The dataset contains SMS messages labeled as spam or ham (non-spam).

Dataset Distribution: 13.2% Spam Messages and 86.8% ham messages

## 🧠 Model Details

Model Used: Multinomial Naive Bayes (MNB)

Vectorization: TF-IDF Vectorization with 3000 features

Performance: Optimized for precision and recall to ensure minimal false positives.

## 🛠️ Tech Stack

Language: Python

Model Training: Scikit-learn

Visualization & UI: Streamlit for interactive dashboards and message testing

Data Handling: Pandas, NumPy

Visualization: Matplotlib, Seaborn (if used)

## 📊 Features

Data Preprocessing:

Text cleaning

Tokenization

TF-IDF feature extraction

Model Training & Evaluation:

Training using Multinomial Naive Bayes

Accuracy, Precision, Recall, and F1-score evaluation

## Interactive Interface:

Built with Streamlit for real-time spam detection testing

## Visualization:

Dataset statistics

Model performance metrics

###🚀 How to Run
1️⃣ Clone the Repository
git clone https://github.com/yourusername/SMS-Spam-Classifier.git
cd SMS-Spam-Classifier

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Streamlit App
streamlit run app.py

## 📦 Project Structure
SMS-Spam-Classifier/
│
├── data/                   # Dataset (if included)
├── app.py                  # Streamlit app for visualization
├── model/                  # Saved model files (if applicable)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── notebooks/              # Jupyter notebooks for exploration & training

## 📈 Results

High classification accuracy achieved using Multinomial Naive Bayes with TF-IDF features.

The model performs well on unseen data, minimizing both false positives and false negatives.

## 📚 References

UCI SMS Spam Collection Dataset

Scikit-learn Documentation

Streamlit Documentation

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the project, feel free to fork the repo and create a pull request.
