# ELT_pipeline
Data Preprocessing Pipeline (ETL) using Pandas & Scikit-Learn

📌 Overview

This project implements a data preprocessing pipeline using Pandas and Scikit-Learn to automate the ETL (Extract, Transform, Load) process.
It processes the Titanic dataset, applies missing value imputation, scaling, and encoding, and saves the cleaned data as a CSV file.

📂 Project Structure

📁 Data-Preprocessing-Pipeline  
│── your_notebook.ipynb      # Jupyter Notebook with complete ETL pipeline  
│── processed_data.csv       # Cleaned & processed dataset  
│── README.md                # Project documentation


⚙️ Installation

Make sure you have Jupyter Notebook installed in VS Code and required dependencies.

1️⃣ Install Jupyter in VS Code (if not installed)

pip install notebook

2️⃣ Install Required Libraries

pip install pandas scikit-learn-

📊 Dataset Used

The dataset used in this project is the Titanic dataset, which is loaded directly from GitHub.

Source: Titanic Dataset - Data Science Dojo

Attributes:

Age, Fare → Numerical features (scaled)

Sex, Embarked → Categorical features (one-hot encoded)

🛠️ Features of the Pipeline

✅ Extract: Reads data from GitHub
✅ Transform:

Handles missing values using SimpleImputer

Applies StandardScaler to numerical data

Uses OneHotEncoder for categorical variables
✅ Load: Saves processed data as processed_data.csv

🚀 How to Run

1️⃣ Open VS Code and navigate to your project folder.
2️⃣ Open Jupyter Notebook (your_notebook.ipynb).
3️⃣ Run all cells step by step.
4️⃣ The processed CSV file (processed_data.csv) will be saved in the same folder.

📌 Output

After running the notebook, the processed dataset is saved as:
📄 processed_data.csv → Fully cleaned & transformed dataset.

📧 Contact

For any queries, feel free to reach out.@navyashreensgr@gmail.com
