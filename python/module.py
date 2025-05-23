import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from datetime import datetime


def prediction(file, date, hour):
    # Load the dataset
    df = pd.read_csv(file)

    # Convert Date to numerical format (ordinal encoding)
    df['Date'] = pd.to_datetime(df['Date']).map(datetime.toordinal)

    # Independent variables (Date and Hour)
    X = df[['Date', 'Hour']]

    # Apply feature scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, df.iloc[:, 2:], test_size=0.2, random_state=42)

    # Perform Random Forest regression for each energy consumption column
    regression_results = {}
    models = {}
    for column in y_train.columns:
        y_train_col = y_train[column]
        y_test_col = y_test[column]

        model = RandomForestRegressor(n_estimators=100, max_depth=5, min_samples_split=10, min_samples_leaf=5,
                                      random_state=42)
        model.fit(X_train, y_train_col)
        models[column] = model  # Store the model for prediction

        # Store results
        regression_results[column] = {
            'train_r_squared': model.score(X_train, y_train_col),
            'test_r_squared': model.score(X_test, y_test_col)
        }

    # Function for prediction
    def predict_energy_consumption(date, hour):
        date_ordinal = datetime.strptime(date, "%Y-%m-%d").toordinal()
        input_data = scaler.transform([[date_ordinal, hour]])  # Apply scaling
        predictions = {column: models[column].predict(input_data)[0] for column in models}
        return predictions

    # # Print regression results
    # for key, value in regression_results.items():
    #     print(f"{key}:")
    #     print(f"  Train R-squared: {value['train_r_squared']:.4f}")
    #     print(f"  Test R-squared: {value['test_r_squared']:.4f}\n")

    # # Print accuracy rates
    # print("Model Accuracy (Train & Test R-squared values):")
    # for key, value in regression_results.items():
    #     print(f"{key}: Train: {value['train_r_squared']:.4f}, Test: {value['test_r_squared']:.4f}")

    # Example prediction
    example_prediction = predict_energy_consumption(date, hour)
    # print("Example Prediction for 2024-03-10 at 14:00:")
    # print(example_prediction)
    return example_prediction
