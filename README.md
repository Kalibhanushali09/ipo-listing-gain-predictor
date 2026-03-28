# IPO Listing Gain Predictor — Indian Markets (2010–2025)

## Overview
When a company launches an IPO in India, retail investors have a short window to decide — apply or skip. This project predicts the listing gain (first-day return) of Indian IPOs using pre-listing data like issue size, subscription levels across investor categories (QIB, HNI, RII), offer price, and broader market conditions at the time of listing.

## Business Problem
Built on 15 years of Indian IPO data, the model helps answer one practical question: **is this IPO worth applying for?**

## Dataset
- 561 Indian IPOs from 2010–2025
- Source: Kaggle + NSE/BSE data
- Target variable: Listing Gain %

## Key Findings
- 52% of IPOs listed with modest 0–30% gain
- 25% listed at a loss
- Only 12% delivered above 50% gains
- QIB subscription (57% feature importance) is the strongest predictor of listing gains
- Institutional investors (smart money) going heavy is the most reliable signal

## Models Compared
| Model | RMSE | R² |
|---|---|---|
| Linear Regression | 31.43 | 0.12 |
| Ridge | 31.43 | 0.12 |
| Random Forest | 32.77 | 0.04 |
| XGBoost | 27.17 | 0.34 |

## Winner: XGBoost
Best RMSE and R² by a significant margin.

## Limitations
- Model uses post-subscription data — most useful in the 3-day window between subscription closing and listing day
- IPO returns are inherently noisy — even professional quant funds struggle to predict them
- Model cannot account for sudden market events or news between subscription and listing

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, YFinance, Streamlit
