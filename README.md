
# Iris Flower Classification Project

This project is a comprehensive walkthrough of a classic machine learning classification problem using the Iris dataset. The goal is to predict the species of an Iris flower based on its sepal and petal measurements. It is designed to be a clear and educational example, covering everything from initial data exploration to model comparison and hyperparameter tuning.

---

## Project Summary & Key Findings

We explored several machine learning models to solve this problem. Our key finding was that for this dataset, the **K-Nearest Neighbors (KNN)** model achieved a perfect **100% accuracy** with its default settings. This outperformed other models, including a Decision Tree (93%), a Support Vector Machine (97%), and a Random Forest (90%).

This highlights a crucial lesson in machine learning: the most complex model is not always the best. The clear, dense clustering of the Iris data makes it particularly well-suited for a distance-based algorithm like KNN.

---

## How to Use This Project

### 1. Installation

First, clone this repository to your local machine. Then, install the necessary Python libraries using the `requirements.txt` file. It is recommended to do this within a virtual environment.

```bash
pip install -r requirements.txt
```

*(Note: We will create the `requirements.txt` file in a later step.)*

### 2. Running the Analysis

The project is organized into a series of Jupyter Notebooks in the `/notebooks` directory. It is recommended to run them in the following order:

1.  **`01_Data_Acquisition.ipynb`**: (Previously `src/get_data.py`) This notebook downloads the Iris dataset and saves it to the `/data` directory.
2.  **`02_Exploratory_Data_Analysis.ipynb`**: (Previously `eda.ipynb`) This notebook explores the dataset, visualizing the relationships between features and the different species.
3.  **`03_Training_and_Evaluation.ipynb`**: (Previously `training.ipynb`) This notebook trains our first model, a Decision Tree, and evaluates its performance.
4.  **`04_Model_Comparison.ipynb`**: (Previously `model_comparison.ipynb`) This is where we test multiple models (KNN, SVM, Random Forest) to find the best performer.
5.  **`05_Hyperparameter_Tuning.ipynb`**: (Previously `hyperparameter_tuning.ipynb`) This notebook provides an educational example of how to tune a model's settings, demonstrating why it isn't always necessary if a simpler model already performs perfectly.

---

## Project Structure

```
├── data/
│   └── iris.csv              # The dataset file
├── models/
│   └── iris_knn_model.joblib # Our final, best-performing model
├── notebooks/
│   ├── 01_Data_Acquisition.ipynb
│   ├── 02_Exploratory_Data_Analysis.ipynb
│   ├── 03_Training_and_Evaluation.ipynb
│   ├── 04_Model_Comparison.ipynb
│   └── 05_Hyperparameter_Tuning.ipynb
├── src/
│   └── predict.py            # A script to make predictions with our model
├── README.md                 # This guide
└── requirements.txt          # Project dependencies
```

- **`/data`**: Contains the raw dataset.
- **`/models`**: Stores saved, trained machine learning models.
- **`/notebooks`**: Contains the step-by-step Jupyter Notebooks for analysis.
- **`/src`**: Holds source code, such as the prediction script.

