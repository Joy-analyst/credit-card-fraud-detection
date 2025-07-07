# 💳 Credit Card Fraud Detection App

This is a machine learning web application that detects fraudulent credit card transactions using an XGBoost model and Streamlit. The model predicts whether a transaction is fraud or not based on selected features.

## 🚀 Live Demo

🔗 [Click here to access the app](https://credit-card-fraud-detection-85kffwmusryfsvqsjedjkv.streamlit.app)

---

## 📁 Project Structure


---


> 📌 Note:  
> - We used `.pkl` for the trained model since XGBoost models are best saved with `joblib`.  
> - `fraud_app_streamlit.py` replaces the traditional `app.py` used in Flask apps.

---

## 📊 Dataset

The dataset used for this project is the popular **Kaggle Credit Card Fraud Detection Dataset**.  


---

## 🧪 Model Details

- Model Type: **XGBoost Classifier**
- Preprocessing: Feature scaling using StandardScaler
- Evaluation Metrics: Accuracy, Precision, Recall, F1-score, AUC-ROC
- Handling Imbalance: Undersampling / SMOTE used during model training

---

## 📝 How to Use

1. Clone this repo:
    ```bash
    git clone https://github.com/Joy-analyst/fraud-detection.git
    cd fraud-detection
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the app locally:
    ```bash
    streamlit run fraud_app_streamlit.py
    ```

4. Enter comma-separated input features into the form and get instant predictions!

---

## 📄 Submission Checklist ✅

- [x] Complete source code (Python + Streamlit)
- [x] Trained model file (.pkl)
- [x] Application file (`fraud_app_streamlit.py`)
- [x] Report (PDF)
- [x] Dataset or download link
- [x] ✅ **Deployed App Link:** [Launch Here](https://credit-card-fraud-detection-85kffwmusryfsvqsjedjkv.streamlit.app)

---

## 👩🏽‍💻 Author

**Joy Uko**  
Data Analyst & Data Scientist  
[LinkedIn](https://www.linkedin.com/in/joy-uko) • [GitHub](https://github.com/Joy-analyst)

---

