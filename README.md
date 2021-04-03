# Fifa 19 Overall Score Predictor

### What this project is about
This project analyses Fifa 19 players and allows the user to predict an overall Fifa score by inputting variables. 

Data used in the project is the Fifa 19 dataset, found [here](https://www.kaggle.com/karangadiya/fifa19).

This repositary contains:
  - Exploritory data analysis
  - Regression model
  - Streamlit app to deploy the model and predict an overall Fifa score

### Results and interesting findings 

Out of Linear Regression, Lasso Regression, Ridge Regression and Random Forest Regressor, the Random Forest Regressor performed best achieving:
  - R^2 Score of **97%**
  - Root Mean Squared Error of **1.26**
 
By using Feature Importance, we are able to see that the top 5 most important features in predicting the overall score is Composure, Potential, Ball Control, Interceptions and Age. 

<img width="741" alt="Screenshot 2021-04-03 at 18 58 20" src="https://user-images.githubusercontent.com/76878856/113488175-4ce48180-94b4-11eb-9b00-b666ba6be6b9.png">

Additionally, from the EDA we saw that the player positions with the highest overall scores where the wingers (RF & LF)
<img width="800" alt="Screenshot 2021-04-03 at 18 58 45" src="https://user-images.githubusercontent.com/76878856/113488207-7dc4b680-94b4-11eb-88f2-8b0ba10f6a60.png">


![deployed-model](https://user-images.githubusercontent.com/76878856/113489477-6b4e7b00-94bc-11eb-9dc6-c777203b5e8b.gif)
