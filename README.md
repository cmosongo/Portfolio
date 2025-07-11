# 📊 Financial Data Analysis & Machine Learning Portfolio

## 🤵 About Me

I'm passionate about applying data science and machine learning to solve real-world problems across finance, healthcare, and entertainment industries. My work focuses on:

- **Fraud Detection & Risk Management** in financial services
- **Recommendation Systems** for improved user engagement
- **Time-Series Analysis** and pattern recognition
- **Deep Learning Applications** in financial markets

I believe in combining traditional quantitative analysis with modern machine learning techniques to create robust, practical solutions.

---

## 🚀 Projects Included

### [1. 🔍 FWA (Fraud, Waste, and Abuse) Claims Modelling](https://github.com/cmosongo/tree/main/1-fwa_claims_modelling)

**Overview:**
Detects Fraud, Waste, and Abuse (FWA) in health insurance claims using machine learning models and risk scoring systems.

**Data:**
Health insurance claims dataset with features including:
- Claim ID, Member ID, Provider ID
- Claim Amount, Diagnosis Code (ICD-10), Procedure Code (CPT)
- Date of Service, Member Age, Geographic Location
- Previous Claims history

**Highlights:**
- **Random Forest Classifier** for fraud prediction
- **Risk Scoring System** to prioritize claims for investigation
- Feature engineering (High Claim Flag, Claims Frequency tracking)
- Comprehensive data preprocessing and EDA with visualizations
- Model evaluation achieving 92.86% accuracy

**Key Results:**
- Improved recall from 15% to 25% through feature engineering
- Developed ranking system for fraudulent claim likelihood
- Identified high-risk claims based on amount thresholds and member behavior

---

### [2. 🎬 Popcorn-Pilot Movie Recommendation System](https://github.com/cmosongo/tree/main/2-popcorn_pilot)

**Overview:**
A personalized movie recommendation system using collaborative filtering to improve user engagement and subscription renewals.

**Data:**
User rating data for movies including:
- Star Wars, The Godfather, Titanic, The Matrix
- Inception, Pulp Fiction, Forrest Gump

**Techniques:**
- **Cosine Similarity Algorithm** for user preference matching
- Weight adjustment based on individual user ratings
- Fallback system using highest-rated movies
- Command-line interface for user interaction

**Key Features:**
- Data cleaning and preprocessing (handling duplicates, rating normalization)
- User preference analysis and movie popularity insights
- Personalized recommendations based on historical preferences
- Robust fallback for new users

---

### [3. 📈 Perceptually Important Points (PIP)](https://github.com/cmosongo/tree/main/3-perceptually_important_points)

**Overview:**
A novel method for reducing dimensionality of time-series data that mimics human visual pattern recognition by identifying perceptually important points.

**Methodology:**
- Identifies points with largest Euclidean distance from connecting lines
- Focuses on visually significant patterns in time-series data
- Mimics human analyst behavior in pattern recognition

**Applications:**
- Time-series data compression
- Fractal dimensionality analysis
- Visual pattern recognition in financial data
- Anomaly detection in sequential data

**Key Features:**
- Algorithm for identifying critical turning points
- Visualization of perceptually important patterns
- Fractal dimension calculations for complexity analysis

---

### [4. 📈 Bond Yields on Currencies](https://github.com/cmosongo/Portfolio/tree/main/4-bond_yields_on_currencies)

**Overview:**
Analyzes how U.S. treasury bond yields influence currency markets and exchange rates.

**Data:**
Uses datasets like `^TNX.csv` (10-year treasury yield) and currency price data.

**Highlights:**
- Data ingestion & preprocessing (Pandas)
- Time-series plotting of yields vs currency pairs
- Exploring correlations and leading indicators

---

### [5. 🔍 Swing High & Low Detection](https://github.com/cmosongo/Portfolio/tree/main/5-swing_high_low)

**Overview:**
Detects local swing highs and lows in OHLC (Open, High, Low, Close) price data to assist in identifying support & resistance levels.

**Techniques:**
- Custom algorithms to identify turning points
- Visualization of swings on price charts

**Use Case:**
Useful for technical analysis and building trading strategies.

---

### [6. 🤖 Deep Learning on OHLC Data](https://github.com/cmosongo/Portfolio/tree/main/6-deep_learning_on_ohlc)

**Overview:**
Applies deep learning models to OHLC financial data to explore predictive price movement.

**Key Features:**
- Data preprocessing pipelines for sequential data
- Experimentation with neural network architectures (LSTM/CNN)
- Evaluation on prediction tasks

---

## 🎯 Project Highlights

**Machine Learning Applications:**
- **Fraud Detection:** 92.86% accuracy in identifying fraudulent insurance claims
- **Recommendation Systems:** Personalized movie suggestions using cosine similarity
- **Time-Series Analysis:** Novel PIP algorithm for pattern recognition

**Financial Analytics:**
- **Currency Analysis:** Bond yield impact on exchange rates
- **Technical Analysis:** Swing point detection for trading strategies
- **Predictive Modeling:** Deep learning for price movement prediction

**Data Processing Expertise:**
- Complex data cleaning and preprocessing pipelines
- Feature engineering for improved model performance
- Handling missing data and class imbalance issues
- Real-time data processing and visualization

---

## 🧰 Tools & Libraries

**Core Data Science Stack:**
- Python (NumPy, pandas, matplotlib, seaborn)
- Scikit-learn for machine learning models
- Jupyter Notebooks for exploratory data analysis

**Deep Learning & Advanced Analytics:**
- TensorFlow / Keras or PyTorch (for deep learning)
- Time-series analysis libraries
- Custom algorithm implementations

**Data Sources:**
- CSV time-series datasets
- Health insurance claims data
- Movie rating databases
- Financial market data (bonds, currencies, OHLC)

---

## 📬 Contact

- **GitHub:** [@cmosongo](https://github.com/cmosongo)
- **LinkedIn:** [Charles Mosongo](https://www.linkedin.com/in/charles-mosongo/)

---

## 🤝 Contributing

I welcome collaboration and feedback! If you're interested in:
- Improving existing models
- Adding new features
- Discussing methodologies
- Exploring new applications

Please feel free to:
- Open an issue
- Submit a pull request
- Reach out directly

---

⭐️ **If you find these projects interesting, please star this repository!**

I'd love to hear your feedback and suggestions for improvement.

---

*Last updated: July 2025*