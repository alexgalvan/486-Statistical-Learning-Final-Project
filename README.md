<ins>**Predictors and Causal Effects of College Completion**</ins>

This project analyzes the factors that predict college completion by age 25 and investigates whether finishing college has a causal impact on future employment stability. Utilizing data from the **National Longitudinal Study of Youth 1997** (NLSY97), the study employs both supervised learning for prediction and causal inference techniques to account for selection bias.  

<ins>**Key Findings**</ins>

- **Strongest Predictors**: High school GPA, ASVAB percentiles, and 8th-grade grades were the most significant predictors of completion.  
- **Employment Impact**: College completion reduces the proportion of weeks spent unemployed by **1.45%** (95% CI: -2.41% to -0.50%) after adjusting for confounding factors.  
- **Selection Bias**: The "naive" employment benefit (3.44%) was significantly higher than the causal estimate, suggesting that individuals who complete college often possess pre-existing advantages, such as higher family income.  

<ins>**Methodology**</ins>

The analysis utilized a cleaned sample of **7,741** individuals and 33 variables covering demographics, student ability, and family dynamics. 

- **Data Processing**: Missing values were handled via **MICE** (numerical - Multiple Imputation by Chained Equations) and **mode** imputation (categorical).  
- **Prediction Model**: A **Lasso Logistic Regression** was used to create a sparse, interpretable model.  
    - **Performance**: Achieved an **83.2% accuracy** and an **AUC of 0.860**, significantly outperforming the 75.6% baseline.  
- **Causal Inference**: An **Augmented Inverse Probability Weighted (AIPW)** estimator was used for its "doubly robust" properties, requiring only one of its underlying models to be correctly specified for bias reduction. 

**Results Summary**

```  Predictor         Log-oddsCoef  OddsRatio  Direction```

```High school GPA     0.482         1.62       Higher completion```

```ASVAB percentile    0.469         1.60       Higher completion```

```8th grade grades    0.318         1.37       Higher completion```

```Delinquency index  -0.134         0.87       Lower completion```

**Conclusions & Limitations**

The study concludes that early academic preparation and family background are primary drivers of college success. While college completion does improve employment outcomes, the effect is more modest than a simple correlation would suggest. **Limitations** include the potential for unmeasured confounders (e.g., student motivation), the assumptions inherent in data imputation, and the fact that NLSY97 data may not fully reflect the modern labor market.

[Statistical learning Final Project Writeup.pdf](https://github.com/user-attachments/files/27728828/Statistical.learning.Final.Project.Writeup.pdf)

<img width="770" height="262" alt="image" src="https://github.com/user-attachments/assets/24a9eb35-4815-42d1-a7e4-90e017857d0d" />

<img width="798" height="288" alt="image" src="https://github.com/user-attachments/assets/a29186ae-ef5c-4b7f-91c2-f9debcf95e4e" />

