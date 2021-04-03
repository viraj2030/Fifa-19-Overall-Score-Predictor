# Fifa 19 Overall Score Predictor

### What this project is about
This project analyses Fifa 19 players and allows the user to predict an overall Fifa score by inputting variables. 

Data used in the project is the Fifa 19 dataset, found [here](https://www.kaggle.com/karangadiya/fifa19).

This repositary contains:
  - Exploritory data analysis
  - Regression model
  - Streamlit app to predict an overall Fifa score

### Results and interesting findings 

Out of Linear Regression, Lasso Regression, Ridge Regression and Random Forest Regressor, the Random Forest Regressor performed best achieving:
  - R^2 Score of **97%**
  - Root Mean Squared Error of **1.26**
 
By using Feature Importance, we are able to see that the top 5 most important features in predicting the overall score is Composure, Potential, Ball Control, Interceptions and Age. 
