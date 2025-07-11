
## 📊 Overview

This analysis includes the following:

* **Visualization**:

  * Line plots of TNX and DXY.
  * Scaled comparison of TNX and DXY.
  * Scatter plot and regression line to explore correlation.

* **Stationarity Testing**:

  * Augmented Dickey-Fuller (ADF) tests are used to assess whether TNX and DXY are stationary.
  * Differencing is applied until both series are stationary, denoted as I(d).

* **Time Series Diagnostics**:

  * ACF and PACF plots visualize the correlation structure of each series.
  * Ljung-Box tests assess autocorrelation up to lag 20.

* **Model Considerations**:

  * Initial results indicate both TNX and DXY may follow martingale-like behavior.
  * The stationarity and correlation structure help guide potential univariate or multivariate modeling.

---

## 📦 R Packages Used

```r
library(readr)
library(tidyverse)
library(tseries)
```

---

## 📈 Key Concepts

* **TNX (Ten-Year Treasury Yield)**: Often used as a benchmark for long-term interest rate expectations.
* **DXY (U.S. Dollar Index)**: Measures the value of the U.S. dollar against a basket of foreign currencies.
* **Stationarity**: Required for time series modeling; non-stationary data is differenced until stationary.
* **ACF & PACF**: Visual tools to determine lag structure.
* **Ljung-Box Test**: Tests for autocorrelation in residuals.

---

## 🛠️ How to Run

1. Clone or download this repository.
2. Place your `data/data.csv` file in the same folder as the `.Rmd` file.
3. Open `notebooks/TNX_and_DXY.Rmd` in RStudio.
4. Knit to HTML to generate the analysis report.

---

## 📌 Notes

* Ensure the `data.csv` file contains properly formatted date and numeric columns for `TNX` and `DXY`.
* The current setup uses absolute paths. Modify the path to match your system or use `here::here()` for portability.
* Serial correlation testing section is prepared but not implemented—add models (e.g., ARIMA) to continue the analysis.

---

## 🔍 Future Enhancements

* Add cointegration tests and vector error correction models (VECM).
* Expand analysis to include macroeconomic covariates (e.g., inflation, interest rates).
* Develop forecasting models based on the time series properties identified.

---
