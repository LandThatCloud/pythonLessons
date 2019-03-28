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

Sckit-learn

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
