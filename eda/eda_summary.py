import pandas as pd
import os

def generate_summary(file_path):
    # Load data
    df = pd.read_csv(file_path)
    
    # Basic info
    output = []
    output.append("## Dataset Overview")
    output.append(f"Number of rows: {df.shape[0]}")
    output.append(f"Number of columns: {df.shape[1]}")
    output.append("\n## Data Types and Missing Values")
    
    summary_df = pd.DataFrame({
        'Dtype': df.dtypes,
        'Non-Null Count': df.count(),
        'Null Count': df.isnull().sum(),
        'Null Percentage': (df.isnull().sum() / len(df) * 100).round(2)
    })
    output.append(summary_df.to_string())
    
    # Descriptive Statistics for Numerical Columns
    output.append("\n## Descriptive Statistics (Numerical)")
    desc = df.describe().transpose()
    output.append(desc.to_string())
    
    # Descriptive Statistics for Categorical Columns
    cat_cols = df.select_dtypes(include=['object']).columns
    if not cat_cols.empty:
        output.append("\n## Categorical Column Summaries")
        for col in cat_cols:
            output.append(f"\n### {col}")
            counts = df[col].value_counts().head(10)
            output.append(counts.to_string())
            
    # Save to file
    with open('eda/plots/eda_summary.md', 'w') as f:
        f.write("\n".join(output))
    
    print("Summary generated successfully in eda/plots/eda_summary.md")

if __name__ == "__main__":
    if os.path.exists('data.csv'):
        generate_summary('data.csv')
    else:
        print("data.csv not found!")
