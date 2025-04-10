Hate Speech Detection

This project is a Hate Speech Detection model that classifies text into three categories:
- Hate Speech
- Offensive Language
- Neither

It uses machine learning techniques to identify harmful comments online.

Model Performance

- Accuracy: 89%
- F1-Scores: 
  - Hate Speech: 30%
  - Offensive Language: 94%
  - Neither: 84%

Files Included

- 'app.py': Streamlit app for real-time predictions.
- 'hate_speech_model.pkl': The trained model.
- 'vectorizer.pkl': Text vectorizer for data processing.
- 'requirements.txt': List of dependencies.

How to Run Locally

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at `http://localhost:8501`.

How to Use

1. Enter a comment in the input box.
2. Click “Classify” to see the result (Hate Speech, Offensive Language, or Neither).

Technologies Used

- Python
- Streamlit for building the web app.
- scikit-learn for machine learning.
- joblib for saving/loading models.

 Future Improvements

- Upgrade the model with more advanced techniques (e.g., BERT, GPT).
- Add multilingual support.
- Improve text preprocessing.
