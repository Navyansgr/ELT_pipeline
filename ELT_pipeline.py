import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Step 1: Extract - Load Data (Change URL/path as needed)
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Step 2: Transform - Handle Missing Values & Encode Data
num_features = ['Age', 'Fare']
cat_features = ['Sex', 'Embarked']

# Pipelines for numerical and categorical features
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')), 
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')), 
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

# Combine transformations
preprocessor = ColumnTransformer([
    ('num', num_pipeline, num_features),
    ('cat', cat_pipeline, cat_features)
])

# Apply transformations
processed_data = preprocessor.fit_transform(df)

# Convert back to DataFrame
processed_df = pd.DataFrame(processed_data)

# Step 3: Load - Save the Processed Data
processed_df.to_csv("processed_data.csv", index=False)

print("✅ ETL Pipeline Completed! Cleaned Data Saved.")