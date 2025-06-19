import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score    

def train_salary_predictor(data_path):
    # Load the dataset
    data = pd.read_csv(data_path)   
    # Check if the necessary columns are present
    if 'YearsExperience' not in data.columns or 'Salary' not in data.columns:
        raise ValueError("Dataset must contain 'YearsExperience' and 'Salary' columns.")
    
    # Prepare the features and target variable
    X = data[['YearsExperience']]
    y = data['Salary']
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Squared Error: {mse}")
    print(f"R-squared: {r2}")
    return model

def predict_salary(model, years_experience):
    # Predict the salary based on years of experience   
    if not isinstance(years_experience, (int, float)):
        raise ValueError("Years of experience must be a numeric value.")
    return model.predict([[years_experience]])[0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python salarypredictor.py Salary_Data.cs>")   
        sys.exit(1)
    data_path = sys.argv[1]
    model = train_salary_predictor(data_path)
    # Example usage
    years_experience = 5
    predicted_salary = predict_salary(model, years_experience)
    print(f"Predicted salary for {years_experience} years of experience: ${predicted_salary:.2f}")
    # Save the model for future use
    import joblib
    joblib.dump(model, 'salary_predictor_model.pkl')
    print("Model saved as 'salary_predictor_model.pkl'")

# Note: Ensure you have the necessary libraries installed:
# pip install pandas scikit-learn joblib
# The dataset should be a CSV file with 'YearsExperience' and 'Salary' columns.
# Example dataset format:
# YearsExperience,Salary
# 1,40000
# 2,50000
# 3,60000
# 4,70000
# 5,80000
# 6,90000
# 7,100000
# 8,110000
# 9,120000
# 10,130000
# The model can be trained using the command:
# python salarypredictor.py path_to_your_dataset.csv
# The model can be used to predict salaries based on years of experience.
# The model will be saved as 'salary_predictor_model.pkl' for future use.
# The model can be loaded later using joblib.load('salary_predictor_model.pkl')
# and used to make predictions without retraining.

# Example usage after loading the model:
# model = joblib.load('salary_predictor_model.pkl')
# years_experience = 5
# predicted_salary = predict_salary(model, years_experience)
# print(f"Predicted salary for {years_experience} years of experience: ${predicted_salary:.2f}")
# The code above defines a simple salary predictor based on years of experience using linear regression.
# It includes functions to train the model, make predictions, and evaluate performance.
# The model is trained on a dataset with 'YearsExperience' and 'Salary' columns.
# The model can be saved and loaded for future predictions.
# The code is designed to be run from the command line with a specified dataset path.
# The model can be used to predict salaries based on years of experience.
# The code is structured to handle errors and ensure the dataset is in the correct format.
# It provides a clear usage example and instructions for running the script.
# The model can be extended or modified to include more features or different algorithms as needed.
# The code is modular and can be easily integrated into larger applications or systems.
# It serves as a basic example of how to implement a machine learning model for salary prediction.
# The code is designed to be simple and easy to understand, making it suitable for educational purposes.


# The model can be further improved by adding more features or using different algorithms.

# The current implementation uses a linear regression model, which is suitable for this type of problem.
# The model can be extended to include more features such as education level, industry, or location.
# This would require additional data preprocessing and feature engineering.
# The model can also be evaluated using different metrics or cross-validation techniques.
# The current implementation uses a simple train-test split for evaluation.
# The model can be saved and loaded using joblib, which is a common practice in machine learning.
# This allows for easy reuse of the trained model without needing to retrain it.

# The code is structured to handle errors and ensure the dataset is in the correct format.
# It checks for the presence of necessary columns and raises an error if they are missing.
# The code also includes a usage example and instructions for running the script.
# This makes it easy for users to understand how to use the model and make predictions.
# The model can be integrated into larger applications or systems as needed.
# Overall, the code provides a solid foundation for building a salary prediction model using machine learning techniques.