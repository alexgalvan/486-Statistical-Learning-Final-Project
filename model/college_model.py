import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler
import os
import warnings

# Ignore minor warnings
warnings.simplefilter("ignore")

# Modern plot style
sns.set_theme(style="whitegrid", palette="flare")

def run_model():
    print("Starting Logistic Regression with Lasso analysis...")
    
    # 1. Load Cleaned Data
    data_path = os.path.join(os.path.dirname(__file__), '../clean.csv')
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found! Please run imputation script first.")
        return
        
    df = pd.read_csv(data_path)
    
    # 2. Define Features (First 23 columns)
    # The first 23 columns are characteristics at or before age 17.
    # We exclude ID, DOB, and the target itself.
    target = 'compcoll_age25'
    ignored = ['ID', 'DOB']
    
    # Take columns up to index 22 (the first 23 columns)
    potential_features = df.columns[:23].tolist()
    features = [col for col in potential_features if col not in [target] + ignored]
    
    X = df[features]
    y = df[target]
    
    print(f"Using {len(features)} base features.")

    # 3. Preprocessing
    # One-hot encoding for categorical variables
    X_encoded = pd.get_dummies(X, drop_first=True)
    feature_names = X_encoded.columns.tolist()
    
    # Standardize features (Crucial for Lasso)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded)
    
    # 4. Logistic Regression with Lasso (L1 penalty)
    # Cs specifies the inverse of regularization strength (tries 10 values by default)
    print("Fitting Lasso model via Cross-Validation...")
    model = LogisticRegressionCV(penalty='l1', solver='liblinear', cv=5, random_state=42, max_iter=1000)
    model.fit(X_scaled, y)
    
    # 5. Extract Results
    coefs = pd.Series(model.coef_[0], index=feature_names)
    important_coefs = coefs[coefs != 0].sort_values()
    
    print(f"Lasso reduced feature space from {len(feature_names)} to {len(important_coefs)} non-zero coefficients.")
    print("\nTop Characteristics Linked to College Completion:")
    print(important_coefs.tail(5).sort_values(ascending=False).to_string())
    
    # 6. Visualization
    plt.figure(figsize=(12, 10))
    # Use a horizontal bar chart for better readability of names
    color_map = ['#e74c3c' if x < 0 else '#2ecc71' for x in important_coefs]
    important_coefs.plot(kind='barh', color=color_map)
    
    plt.title('Characteristics of College Completion (Lasso Coefficients)', fontsize=16)
    plt.xlabel('Log-Odds Magnitude (Standardized)', fontsize=12)
    plt.axvline(0, color='black', linestyle='-', linewidth=1)
    plt.tight_layout()
    
    # Ensure plots directory exists
    plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
    if not os.path.exists(plots_dir):
        os.makedirs(plots_dir)
        
    plot_path = os.path.join(plots_dir, 'college_characteristics_lasso.png')
    plt.savefig(plot_path, dpi=300)
    plt.close()
    
    print(f"Analysis complete. Plot saved to {plot_path}")

if __name__ == "__main__":
    run_model()
