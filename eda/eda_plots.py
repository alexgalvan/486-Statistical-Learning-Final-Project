import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plots style
sns.set(style="whitegrid")

def generate_plots(file_path):
    # Load data
    df = pd.read_csv(file_path)
    
    # Create plots directory if it doesn't exist
    if not os.path.exists('eda/plots'):
        os.makedirs('eda/plots')
    
    # 1. Missing Values Heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title('Missing Values Heatmap')
    plt.savefig('eda/plots/missing_values_heatmap.png')
    plt.close()
    
    # 2. Histograms for Numerical Columns
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in num_cols:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[col].dropna(), kde=True, color='skyblue')
        plt.title(f'Distribution of {col}')
        plt.savefig(f'eda/plots/dist_{col}.png')
        plt.close()
        
    # 3. Bar Charts for Categorical Columns
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        plt.figure(figsize=(10, 6))
        # Take top 10 categories if too many
        top_cats = df[col].value_counts().head(10)
        sns.barplot(x=top_cats.index, y=top_cats.values, palette='viridis')
        plt.title(f'Top 10 Categories in {col}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f'eda/plots/cat_{col}.png')
        plt.close()
        
    # 4. Correlation Heatmap (for numerical)
    if len(num_cols) > 1:
        plt.figure(figsize=(12, 10))
        corr = df[num_cols].corr()
        sns.heatmap(corr, annot=False, cmap='coolwarm', fmt=".2f")
        plt.title('Correlation Heatmap')
        plt.tight_layout()
        plt.savefig('eda/plots/correlation_heatmap.png')
        plt.close()
        
    print("Plots generated successfully in eda/plots/")

if __name__ == "__main__":
    if os.path.exists('data.csv'):
        generate_plots('data.csv')
    else:
        print("data.csv not found!")
