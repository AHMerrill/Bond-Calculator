# Bond Valuation Calculator - Streamlit App

This is a Streamlit web application that converts the Jupyter notebook functionality for bond valuation calculations into an interactive web interface.

## Features

- **Interactive Bond Valuation**: Calculate bond values, Macaulay duration, and modified duration
- **Real-time Calculations**: Update parameters and see results instantly
- **Visualizations**: Interactive charts showing bond value vs YTM relationships
- **Cash Flow Analysis**: Detailed breakdown of bond cash flows and present values
- **Professional UI**: Clean, modern interface with metrics and insights

## Installation

1. Install the required dependencies:
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

1. **Input Parameters** (sidebar):
   - Coupon Rate: Annual coupon rate as decimal (e.g., 0.06 for 6%)
   - Maturity: Time to maturity in years
   - Yield to Maturity: Market yield as decimal (e.g., 0.08 for 8%)
   - Face Value: Par value of the bond
   - Compounding Periods: Number of times interest is compounded per year

2. **Results Display**:
   - Bond Value: Current market value
   - Macaulay Duration: In both periods and years
   - Modified Duration: For interest rate sensitivity

3. **Visualizations**:
   - **Bond Value vs YTM**: Interactive chart showing price-yield relationship
   - **Cash Flow Analysis**: Detailed table of all cash flows and present values
   - **Bond Details**: Complete parameter summary and insights

## Original Notebook

This app was converted from `ahm2452_merrill_hw2.ipynb` which contains the original bond valuation functions and calculations.

## Author

Zan Merrill (ahm2452) - Financial Analytics Problem Set 2 