## Dataset Overview
- **Number of rows:** 7741
- **Number of columns:** 33

## Data Types and Missing Values

| Column | Dtype | Non-Null Count | Null Count | Null Percentage |
| :--- | :--- | :--- | :--- | :--- |
| ID | int64 | 7741 | 0 | 0.00% |
| sex | object | 7741 | 0 | 0.00% |
| DOB | object | 7741 | 0 | 0.00% |
| age97 | int64 | 7741 | 0 | 0.00% |
| compcoll_age25 | int64 | 7741 | 0 | 0.00% |
| race | object | 7741 | 0 | 0.00% |
| father_educ_years | float64 | 6264 | 1477 | 19.08% |
| mother_educ_years | float64 | 7202 | 539 | 6.96% |
| parinc | float64 | 7184 | 557 | 7.20% |
| intact | float64 | 6797 | 944 | 12.19% |
| sibsz | float64 | 6876 | 865 | 11.17% |
| region_age17 | object | 7741 | 0 | 0.00% |
| urban_rural_age17 | object | 7741 | 0 | 0.00% |
| asvab_mv_pct | float64 | 6281 | 1460 | 18.86% |
| grades8th | float64 | 7708 | 33 | 0.43% |
| hsprog | float64 | 7690 | 51 | 0.66% |
| gpa | float64 | 7698 | 43 | 0.56% |
| peers_aspiration_college | object | 7650 | 91 | 1.18% |
| delinq | float64 | 7730 | 11 | 0.14% |
| tchgood | float64 | 7727 | 14 | 0.18% |
| schsafe | float64 | 7725 | 16 | 0.21% |
| marstat_age17 | object | 7682 | 59 | 0.76% |
| res_children_age17 | float64 | 7740 | 1 | 0.01% |
| weeks_Unemployed | float64 | 7426 | 315 | 4.07% |
| weeks_Out of labor force | float64 | 7426 | 315 | 4.07% |
| weeks_Employed | float64 | 7426 | 315 | 4.07% |
| weeks_Not working (unclear if unemployed or NILF) | float64 | 7426 | 315 | 4.07% |
| weeks_Active military | float64 | 7426 | 315 | 4.07% |
| prop_Unemployed | float64 | 7426 | 315 | 4.07% |
| prop_Out of labor force | float64 | 7426 | 315 | 4.07% |
| prop_Employed | float64 | 7426 | 315 | 4.07% |
| prop_Not working (unclear if unemployed or NILF) | float64 | 7426 | 315 | 4.07% |
| prop_Active military | float64 | 7426 | 315 | 4.07% |

## Descriptive Statistics (Numerical)

| Column | count | mean | std | min | 25% | 50% | 75% | max |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ID | 7741.0 | 4458.61 | 2587.76 | 1.0 | 2226.0 | 4460.0 | 6662.0 | 9022.0 |
| age97 | 7741.0 | 13.99 | 1.40 | 12.0 | 13.0 | 14.0 | 15.0 | 16.0 |
| compcoll_age25 | 7741.0 | 0.24 | 0.43 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 |
| father_educ_years | 6264.0 | 12.79 | 3.14 | 1.0 | 12.0 | 12.0 | 14.0 | 20.0 |
| mother_educ_years | 7202.0 | 12.67 | 2.85 | 1.0 | 12.0 | 12.0 | 14.0 | 20.0 |
| parinc | 7184.0 | 54375.71 | 47283.87 | 0.0 | 22364.33 | 43000.0 | 72141.67 | 425586.0 |
| intact | 6797.0 | 0.48 | 0.50 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| sibsz | 6876.0 | 4.34 | 3.04 | 0.0 | 2.0 | 4.0 | 6.0 | 16.0 |
| asvab_mv_pct | 6281.0 | 48.41 | 28.56 | 0.0 | 23.63 | 47.09 | 72.69 | 100.0 |
| grades8th | 7708.0 | 2.89 | 0.82 | 0.0 | 2.5 | 3.0 | 3.5 | 4.0 |
| hsprog | 7690.0 | 0.32 | 0.47 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| gpa | 7698.0 | 2.86 | 0.77 | 0.0 | 2.5 | 3.0 | 3.5 | 4.0 |
| delinq | 7730.0 | 1.25 | 1.75 | 0.0 | 0.0 | 1.0 | 2.0 | 10.0 |
| tchgood | 7727.0 | 0.88 | 0.32 | 0.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| schsafe | 7725.0 | 0.87 | 0.34 | 0.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| res_children_age17 | 7740.0 | 0.06 | 0.26 | 0.0 | 0.0 | 0.0 | 0.0 | 3.0 |
| weeks_Unemployed | 7426.0 | 35.98 | 64.49 | 0.0 | 0.0 | 7.0 | 44.0 | 711.0 |
| weeks_Out of labor force | 7426.0 | 113.64 | 182.78 | 0.0 | 1.0 | 25.0 | 139.0 | 1008.0 |
| weeks_Employed | 7426.0 | 616.78 | 264.82 | 0.0 | 450.0 | 706.0 | 818.75 | 1012.0 |
| weeks_Not working (unclear if unemployed or NILF) | 7426.0 | 3.79 | 24.16 | 0.0 | 0.0 | 0.0 | 0.0 | 766.0 |
| weeks_Active military | 7426.0 | 13.43 | 87.57 | 0.0 | 0.0 | 0.0 | 0.0 | 955.0 |
| prop_Unemployed | 7426.0 | 0.05 | 0.08 | 0.0 | 0.0 | 0.01 | 0.06 | 0.89 |
| prop_Out of labor force | 7426.0 | 0.15 | 0.23 | 0.0 | 0.00 | 0.03 | 0.19 | 1.00 |
| prop_Employed | 7426.0 | 0.78 | 0.28 | 0.0 | 0.67 | 0.91 | 0.99 | 1.00 |
| prop_Not working (unclear if unemployed or NILF) | 7426.0 | 0.01 | 0.03 | 0.0 | 0.0 | 0.0 | 0.0 | 1.00 |
| prop_Active military | 7426.0 | 0.02 | 0.11 | 0.0 | 0.0 | 0.0 | 0.0 | 1.00 |

## Categorical Column Summaries

### sex
| Category | Count |
| :--- | :--- |
| M | 3895 |
| F | 3846 |

### race
| Category | Count |
| :--- | :--- |
| Non-Black / Non-Hispanic | 4162 |
| Black | 1967 |
| Hispanic | 1537 |
| Mixed Race (Non-Hispanic) | 75 |

### region_age17
| Category | Count |
| :--- | :--- |
| South | 2744 |
| North Central | 1706 |
| West | 1646 |
| Northeast | 1306 |
| Non-interview | 326 |
| Outside U.S. | 8 |
| Invalid Skip | 5 |

### urban_rural_age17
| Category | Count |
| :--- | :--- |
| Urban | 5365 |
| Rural | 1816 |
| Non-interview | 326 |
| Unknown | 215 |
| Invalid Skip | 11 |
| Outside U.S. | 8 |

### peers_aspiration_college
| Category | Count |
| :--- | :--- |
| About 75% | 2602 |
| About half (50%) | 2222 |
| Almost all (>90%) | 1728 |
| About 25% | 859 |
| Almost none (<10%) | 239 |

### marstat_age17
| Category | Count |
| :--- | :--- |
| Never married | 7578 |
| Married | 99 |
| Separated | 3 |
| Divorced | 2 |

### DOB (Top 10)
| Category | Count |
| :--- | :--- |
| 1981-09-01 | 162 |
| 1983-09-01 | 151 |
| 1982-07-01 | 147 |
| 1981-01-01 | 145 |
| 1981-08-01 | 145 |
| 1983-10-01 | 143 |
| 1982-08-01 | 143 |
| 1982-01-01 | 143 |
| 1984-01-01 | 143 |
| 1981-07-01 | 141 |