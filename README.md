# Bond Valuation Calculator

A professional Streamlit web application for bond valuation calculations, interactive visualizations, and financial analysis. This tool converts bond valuation functions into an accessible, real-time interactive interface.

## About

This is an MSBA (Master of Science in Business Administration) student project built to provide an interactive tool for bond valuation and analysis. Originally developed as a Jupyter notebook for Financial Analytics coursework, this application brings the calculations to a modern web interface with live visualizations and detailed financial metrics.

## Features

- **Interactive Bond Valuation**: Calculate bond values, Macaulay duration, and modified duration in real-time
- **Real-time Calculations**: Update parameters and see results instantly without page refresh
- **Visualizations**: 
  - Interactive charts showing bond value vs YTM relationships
  - Cash flow analysis with detailed tables
  - Bond parameter summaries and financial insights
- **Cash Flow Analysis**: Detailed breakdown of all bond cash flows with present values
- **Financial Insights**: Automatic detection of premium/discount bonds and interest rate risk analysis
- **Professional UI**: Clean, modern interface built with Streamlit featuring metrics, tabs, and interactive charts

## Technologies Used

- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computations
- **Plotly** - Interactive visualizations
- **Matplotlib** - Additional plotting capabilities

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AHMerrill/Bond-Calculator.git
cd Bond-Calculator
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

1. Navigate to the project directory
2. Run the Streamlit app:
```bash
streamlit run bond_streamlit_app.py
```

3. The app will open in your default web browser (usually at http://localhost:8501)

## Usage

### Input Parameters (Sidebar)

Configure your bond parameters in the left sidebar:

- **Coupon Rate (APR)**: Annual coupon rate as a decimal (e.g., 0.06 for 6%)
- **Maturity**: Time to maturity in years
- **Yield to Maturity (YTM)**: Market yield as a decimal (e.g., 0.08 for 8%)
- **Face Value**: Par value of the bond (default $1,000)
- **Compounding Periods**: Number of times interest is compounded per year (1, 2, 4, 12, or 365)

### Results Display

The application displays four key financial metrics:

1. **Bond Value**: Current market value with percentage difference from par
2. **Macaulay Duration (Periods)**: Duration measured in compounding periods
3. **Macaulay Duration (Years)**: Duration converted to years
4. **Modified Duration**: Approximate percentage change in bond value for each 1% change in YTM

### Visualizations & Tabs

**Bond Value vs YTM**
- Interactive chart showing the price-yield relationship
- Current market point highlighted
- Automatic classification of premium, par, or discount bonds

**Cash Flow Analysis**
- Detailed table of all bond cash flows
- Period-by-period coupon payments and face value
- Present value factors and weighted present values
- Summary statistics

**Bond Details**
- Complete parameter summary
- Bond pricing insights (premium/discount/par classification)
- Duration metrics and interpretations
- Estimated price change for 1% YTM movement

## File Structure

```
Bond-Calculator/
├── bond_streamlit_app.py     # Main Streamlit application
├── requirements.txt           # Project dependencies
├── README.md                  # This file
└── LICENSE                    # License information
```

## Key Calculations

The application implements the following financial calculations:

- **Bond Value**: Present value of all future cash flows (coupons + face value)
- **Macaulay Duration**: Weighted average time to receive cash flows
- **Modified Duration**: Interest rate sensitivity metric

## Original Source

This app was converted from `ahm2452_merrill_hw2.ipynb`, which contains the original bond valuation functions and calculations developed for Financial Analytics coursework.

## Author

**Zan Merrill** (ahm2452)
- MSBA Student
- Financial Analytics Problem Set 2

## License

This project is provided for educational purposes. See LICENSE file for details.

## Notes

- All calculations follow standard bond valuation methodologies
- The app supports various compounding frequencies for flexibility
- Results are calculated in real-time using pandas and NumPy for accuracy
- Plotly ensures interactive, responsive visualizations across devices

---

*Last Updated: 2026*
