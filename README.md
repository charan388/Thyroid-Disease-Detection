# Detecting Thyroid Diseases

Thyroid diseases are a prevalent health concern in India, affecting millions of individuals annually. These conditions can either accelerate or decelerate the body's metabolic processes. The primary aim of this project is to predict whether an individual has compensated hypothyroid, primary hypothyroid, secondary hypothyroid, or no thyroid disorder using Machine Learning techniques.

## Classification Models

Various classification algorithms, including Random Forest, XGBoost, and K-Nearest Neighbors (KNN), have been trained on the thyroid dataset obtained from the UCI Machine Learning Repository. After fine-tuning hyperparameters, the KNN model achieved superior accuracy. The application has been deployed on Heroku, powered by the Flask framework.

## Technical Aspects

- Python 3.7 or higher
- Key Libraries: scikit-learn, pandas, numpy, matplotlib, and seaborn
- Front-end: HTML and CSS
- Back-end: Flask framework
- Integrated Development Environments: Jupyter Notebook, PyCharm, and VSCode
- Database: Cassandra
- Deployment: AWS EC2

## Running the Application

To run the application, follow these steps:

1. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

2. Create a virtual environment: `conda create -n myenv python=3.7`

3. Activate the environment: `conda activate myenv`

4. Install the necessary packages: `pip install -r requirements.txt`

5. Run the app: `python run app.py`

## Project Workflow

### Data Collection

The project utilizes the Thyroid Disease Data Set from the UCI Machine Learning Repository. You can access the dataset [here](https://archive.ics.uci.edu/ml/datasets/thyroid+disease).

### Data Pre-processing

- Addressing missing values using Simple Imputation (KNN Imputer)
- Detecting and removing outliers through boxplots and percentile-based methods
- Handling categorical features via ordinal and label encoding
- Applying feature scaling using the Standard Scaler method
- Handling imbalanced datasets using SMOTE
- Eliminating unnecessary columns

### Model Development and Evaluation

- Testing various classification algorithms, including Random Forest, XGBoost, and KNN
- All three models (Random Forest, XGBoost, and KNN) performed well
- Hyperparameter tuning using RandomizedSearchCV
- Model performance assessment based on accuracy, confusion matrix, and classification report

### Database Integration

A Cassandra database is employed for this project.

### Model Deployment

The final model is deployed on AWS EC2 using the Flask framework.
