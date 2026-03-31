import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import LabelEncoder
import os

def perform_imputation(file_path, output_path):
    print(f"Starting imputation on {file_path}...")
    df = pd.read_csv(file_path)
    
    # 1. Identify column types
    # Exclude ID from imputation logic (it has no missing values anyway)
    cols_to_impute = [col for col in df.columns if col != 'ID']
    
    # 2. Separate numerical and categorical
    num_cols = df[cols_to_impute].select_dtypes(include=[np.number]).columns.tolist()
    cat_cols = df[cols_to_impute].select_dtypes(include=['object']).columns.tolist()
    
    print(f"Numerical columns: {len(num_cols)}")
    print(f"Categorical columns: {len(cat_cols)}")

    # 3. Handle Categorical Columns (Simple Mode Imputation)
    # We also need to encode them to help the numerical imputer
    encoded_df = df.copy()
    label_encoders = {}
    
    for col in cat_cols:
        # Fill missing with mode first
        if df[col].isnull().any():
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
        
        # Encode for the iterative imputer
        le = LabelEncoder()
        # We need to handle strings vs NA if any still exist (shouldn't after fillna)
        encoded_df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

    # 4. Iterative Imputation (MICE) for Numerical Columns
    # We include encoded categorical columns to improve the prediction quality
    imputer = IterativeImputer(random_state=42, max_iter=10)
    
    # Select columns for imputer (exclude ID)
    impute_data = encoded_df[num_cols + cat_cols]
    
    print("Running IterativeImputer (MICE)... this may take a moment.")
    imputed_values = imputer.fit_transform(impute_data)
    
    # Create a temporary dataframe with imputed values
    imputed_df = pd.DataFrame(imputed_values, columns=num_cols + cat_cols)
    
    # 5. Restore the original format
    final_df = df.copy()
    
    # Update numerical columns with imputed values
    for col in num_cols:
        final_df[col] = imputed_df[col]
    
    # Categorical columns were already mode-imputed but we can 
    # check if we should keep the MICE 'encoded' version or original.
    # Usually, for categorical, mode is safer than MICE-rounded-floats.
    # So we stick with the mode-imputed strings in final_df.
    
    # 6. Save to CSV
    final_df.to_csv(output_path, index=False)
    print(f"Imputation complete. Cleaned data saved to {output_path}")
    
    # Final check
    null_count = final_df.isnull().sum().sum()
    print(f"Total null values in clean.csv: {null_count}")

if __name__ == "__main__":
    if os.path.exists('data.csv'):
        perform_imputation('data.csv', 'clean.csv')
    else:
        print("data.csv not found!")
