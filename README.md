# Salary Predictor using Linear Regression

This project is a simple **Salary Predictor** that uses Linear Regression to estimate salaries based on years of experience. It is implemented in Python using `pandas` and `scikit-learn`.

## Features

- Trains a linear regression model on a CSV dataset.
- Predicts salary for a given number of years of experience.
- Evaluates model performance (MSE, R²).
- Saves and loads the trained model for future use.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- joblib

Install dependencies with:

```
pip install pandas scikit-learn joblib
```

## Dataset Format

The dataset should be a CSV file with the following columns:

```
YearsExperience,Salary
1,40000
2,50000
...
```

## Usage

### Train the Model

Run the script from the command line:

```
python salarypredictor.py path_to_your_dataset.csv
```

### Predict Salary

After training, the model is saved as `salary_predictor_model.pkl`. You can load and use it as follows:

```python
import joblib
from salarypredictor import predict_salary

model = joblib.load('salary_predictor_model.pkl')
years_experience = 5
predicted_salary = predict_salary(model, years_experience)
print(f"Predicted salary for {years_experience} years of experience: ${predicted_salary:.2f}")
```

## Example Output

```
Mean Squared Error: 35000000.0
R-squared: 0.95
Predicted salary for 5 years of experience: $80000.00
Model saved as 'salary_predictor_model.pkl'
```

## Notes

- Ensure your dataset contains the required columns: `YearsExperience` and `Salary`.
- The model can be extended to include more features (e.g., education, industry).
- For any issues, ensure all dependencies are installed and the dataset path is correct.

---
```<!-- filepath: c:\Users\tinku\PyCharm\README.md -->
# Salary Predictor using Linear Regression

This project is a simple **Salary Predictor** that uses Linear Regression to estimate salaries based on years of experience. It is implemented in Python using `pandas` and `scikit-learn`.

## Features

- Trains a linear regression model on a CSV dataset.
- Predicts salary for a given number of years of experience.
- Evaluates model performance (MSE, R²).
- Saves and loads the trained model for future use.

## Requirements

- Python 3.x
- pandas
- scikit-learn
- joblib

Install dependencies with:

```
pip install pandas scikit-learn joblib
```

## Dataset Format

The dataset should be a CSV file with the following columns:

```
YearsExperience,Salary
1,40000
2,50000
...
```

## Usage

### Train the Model

Run the script from the command line:

```
python salarypredictor.py path_to_your_dataset.csv
```

### Predict Salary

After training, the model is saved as `salary_predictor_model.pkl`. You can load and use it as follows:

```python
import joblib
from salarypredictor import predict_salary

model = joblib.load('salary_predictor_model.pkl')
years_experience = 5
predicted_salary = predict_salary(model, years_experience)
print(f"Predicted salary for {years_experience} years of experience: ${predicted_salary:.2f}")
```

## Example Output

```
Mean Squared Error: 35000000.0
R-squared: 0.95
Predicted salary for 5 years of experience: $80000.00
Model saved as 'salary_predictor_model.pkl'
```

## Notes

- Ensure your dataset contains the required columns: `YearsExperience` and `Salary`.
- The model can be extended to include more features (e.g., education, industry).
- For any issues, ensure all dependencies are installed and the dataset path is correct.