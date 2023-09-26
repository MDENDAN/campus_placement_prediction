# Campus Recruitment Prediction Web App

This is a simple web application built with Streamlit that predicts campus recruitment status and salary based on user-provided features. The project includes a machine learning model for predicting recruitment status and a Random Forest regression model for predicting salary.

## Getting Started

### Prerequisites

- Python 3.x
- Streamlit
- scikit-learn
- joblib (for model loading)
- pandas (for data manipulation)

You can install the required Python libraries using pip:

```bash
pip install streamlit scikit-learn joblib pandas
```

The app will open in your default web browser, allowing you to input data and make predictions.

**Click [here](https://campusplacementrecruitment.streamlit.app/) to use the web application**

## Using the Web Application

1. Select various features such as gender, academic percentages, board, work experience, etc.
2. Click the "Make Prediction" button.
3. The app will predict the campus recruitment status and, if placed, will predict the salary based on the input features.

## Files and Structure

  - `app.py`: The Streamlit app that handles user input and displays predictions.
  - `model.py`: Contains functions to load the machine learning models and make predictions.
  - `data`: This folder contains csv file use for trainig model.
  - `models`: This folder contains two joblib files. One is Decision Tree for predicting status of placement and another is approximate salary if **'Placed'**


## About Streamlit

[Streamlit](https://streamlit.io/) is an open-source Python library that allows you to create web applications for machine learning and data science projects with minimal effort. It simplifies the process of turning data scripts into shareable web apps.

## Acknowledgments

- This project uses Streamlit for creating the web interface.
- The machine learning models are built using scikit-learn.
- The Random Forest regression model is used for salary prediction.
