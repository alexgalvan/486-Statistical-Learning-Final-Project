import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.preprocessing import StandardScaler
import os
import warnings

# Modern aesthetics
sns.set_theme(style="whitegrid", palette="muted")
warnings.simplefilter("ignore")

def perform_causal_analysis():
    print("Starting Doubly Robust Estimation for Goal 2...")
    
    # 1. Load Data (ensure path is correct relative to script in models/)
    data_path = os.path.join(os.path.dirname(__file__), '../clean.csv')
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found!")
        return
    df = pd.read_csv(data_path)
    
    # 2. Define Variables
    T_col = 'compcoll_age25'
    # Outcome: Total weeks employed
    Y_col = 'weeks_Employed'
    ignored = ['ID', 'DOB', T_col]
    feature_cols = [col for col in df.columns[:23] if col not in ignored]
    
    X = df[feature_cols]
    T = df[T_col]
    Y = df[Y_col]
    
    # One-hot encoding & Scaling
    X_encoded = pd.get_dummies(X, drop_first=True)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded)
    
    # 3. Propensity Score Model
    pi_model = LogisticRegression(max_iter=1000)
    pi_model.fit(X_scaled, T)
    e_hat = pi_model.predict_proba(X_scaled)[:, 1]
    e_hat = np.clip(e_hat, 0.01, 0.99)
    
    # 4. Outcome Models
    mu1_model = LinearRegression()
    mu0_model = LinearRegression()
    
    mu1_model.fit(X_scaled[T == 1], Y[T == 1])
    mu0_model.fit(X_scaled[T == 0], Y[T == 0])
    
    mu1_hat = mu1_model.predict(X_scaled)
    mu0_hat = mu0_model.predict(X_scaled)
    
    # 5. Doubly Robust Estimator
    dr_treated = mu1_hat + (T * (Y - mu1_hat) / e_hat)
    dr_control = mu0_hat + ((1 - T) * (Y - mu0_hat) / (1 - e_hat))
    ate_dr = np.mean(dr_treated - dr_control)
    
    # Simple (Biased) Comparison
    naive_ate = Y[T == 1].mean() - Y[T == 0].mean()
    
    # 6. RESULTS & VISUALIZATION
    plots_dir = os.path.join(os.path.dirname(__file__), 'plots')
    os.makedirs(plots_dir, exist_ok=True)
    
    # --- Plot A: Propensity Score Overlap ---
    # This plot verifies the "Overlap Assumption"
    plt.figure(figsize=(10, 6))
    sns.kdeplot(e_hat[T == 1], fill=True, color='teal', label='College (Treated)', alpha=0.5)
    sns.kdeplot(e_hat[T == 0], fill=True, color='coral', label='No College (Control)', alpha=0.5)
    plt.title('Propensity Score Distributions (Overlap Check)', fontsize=16)
    plt.xlabel('Probability of Finishing College', fontsize=12)
    plt.ylabel('Density', fontsize=12)
    plt.legend()
    plt.savefig(os.path.join(plots_dir, 'propensity_overlap.png'), dpi=300)
    plt.close()
    
    # --- Plot B: ATE Comparison ---
    plt.figure(figsize=(8, 6))
    results_df = pd.DataFrame({
        'Method': ['Naive difference', 'Doubly Robust (ATE)'],
        'Effect (Weeks)': [naive_ate, ate_dr]
    })
    sns.barplot(x='Method', y='Effect (Weeks)', data=results_df, palette=['#95a5a6', '#2ecc71'])
    plt.title('Causal Effect of College on Employment Weeks', fontsize=16)
    plt.ylabel('Increase in Total Weeks Employed', fontsize=12)
    plt.savefig(os.path.join(plots_dir, 'causal_effect_comparison.png'), dpi=300)
    plt.close()
    
    # 7. Save RESULTS back to plots directory as requested
    results_path = os.path.join(plots_dir, 'causal_results.txt')
    with open(results_path, 'w') as f:
        f.write(f"--- Causal Analysis (Doubly Robust) Results ---\n")
        f.write(f"Naive Difference: {naive_ate:.2f} weeks\n")
        f.write(f"Doubly Robust ATE: {ate_dr:.2f} weeks\n")
        f.write(f"Findings: College increases employment duration by {ate_dr:.2f} weeks.\n")

    print(f"Analysis complete. Plots and results saved to {plots_dir}")

if __name__ == "__main__":
    perform_causal_analysis()
