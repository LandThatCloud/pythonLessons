# Python Lessons coupled with Machine Learning & Data Science
Data Science

Topic: Data Models
Course: Decision Trees
Date:
Professor:

Pandas

Import pandas as pd

* Data Frame
    * File_path, read_csv, describe

Sckit-learn - Building a Model

* Selecting Data for Modelling
    * Data_frame.columns
* Choosing Prediction target (price)
    * y = Data_frame.target_column
* Choosing Features
    * X = Data_frame[“Column Name1", "Column Name2"…, "Column Name N"]
    * X.describe() —> Read & X.head() —> Top few rows
* Scikit-learn
    * sklearn library
        * Define: Defining the type of model (eg: Decision Tree)
        * Fit: Capture patterns. Heart of modelling.
        * Predict: An assumption
        * Evaluate: The validity of the model
    * From sklearn.tree import DecisionTreeRegressor
        * Model = DecisionTreeRegressor(random_state = n)
            * Random_state: Ensuring same results in each run
        * Model.fit(X,y)
            * X is the Data_Frame with featured columns
            * Y is the data_frame filtered with the prediction target
        * Model.predict(X)
Model Validation

* Sklearn.tree import train_test_split
    * Splitting data into training data & validation data
        * train_X, train_y, val_X, val_y = train_test_split(X,y,random_state=1)
        * Define Decision Tree Regressor
        * Fit model with training values
    * Predict both and calculate MAE (Mean Absolute Error with validation data)
        * Predict with training value (Train_X)
        * Calculate MAE by: mean_absolute_error(predictions_using_training_values, actual_training_value_y)

Overfitting and Underfitting

* Overfitting
    * capturing spurious patterns that won't recur in the future, leading to less accurate predictions
    * More total leaaves — lesser MAEs — Not a reliable model as predictions are from a very small subset of data
* Underfitting
    * failing to capture relevant patterns, again leading to less accurate predictions.
    * Less total leaves — higher MAEs — Not reliable model as predications does not capture minute patterns leading to data which is not that useful
* Find a spot between Over and Underfitting
    * Define a method that calculates MAEs
    * Calculate MAEs for a list of max_leaf_nodes and find the lowest MAE which will give you the best max leaf node config.
    * Model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes_no, random_state=0)

Random Forests

* Sklearn.ensemble : import RandomForestRegressor
* Sklearn.metrics: import mean_absolute_error
* Model  —> RandomForestRegressor(random_state=1)
* Fit the model with train_X and train_y
* Predict with this model
* Calculate mean absolute error with Val_X and predictions.
