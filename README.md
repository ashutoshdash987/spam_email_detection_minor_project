## Features

- Utilizes a stacking classifier combining Support Vector Machine (SVM), Random Forest, and Naive Bayes models to enhance spam detection accuracy.
- Provides an intuitive and interactive web interface for users to input email data, view detection results, and analyze model performance.
- Uses Term Frequency-Inverse Document Frequency (TF-IDF) to transform text data into meaningful numerical features for the machine learning models.
- Uses login facilities for secure access to the system, ensuring that only authorized users can utilize the application and view their search history.

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, Scikit-learn
- **Database:** MySQL
- **Other Libraries:** Pandas, Numpy, NLTK (for text processing)

## Steps to run the application

1. Open the `model.ipynb` file and run the notebook:
   - This will preprocess the data, train the models, and create two joblib files: one for the model and another for the text-to-numeric transformation.

2. Open the terminal and run the Streamlit application by typing the command:
   ```bash
   streamlit run main.py

3. The main.py script will serve the frontend using Streamlit and automatically use `db.py` to perform all database-related tasks.
