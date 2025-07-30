import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Bond Valuation Calculator",
    page_icon="💰",
    layout="wide"
)

# Title and description
st.title("💰 Bond Valuation Calculator")
st.markdown("**Financial Analytics Problem Set 2** - Converted to Streamlit App")
st.markdown("*By Zan Merrill (ahm2452)*")

# Sidebar for inputs
st.sidebar.header("📊 Bond Parameters")

# Input widgets
coupon_rate = st.sidebar.number_input(
    "Coupon Rate (APR)",
    min_value=0.0,
    max_value=1.0,
    value=0.06,
    step=0.01,
    help="Enter as decimal (e.g., 0.06 for 6%)"
)

maturity_years = st.sidebar.number_input(
    "Maturity (Years)",
    min_value=1,
    max_value=50,
    value=5,
    step=1,
    help="Time to maturity in years"
)

ytm_apr = st.sidebar.number_input(
    "Yield to Maturity (APR)",
    min_value=0.0,
    max_value=1.0,
    value=0.08,
    step=0.01,
    help="Enter as decimal (e.g., 0.08 for 8%)"
)

face_value = st.sidebar.number_input(
    "Face Value ($)",
    min_value=1.0,
    max_value=1000000.0,
    value=1000.0,
    step=100.0,
    help="Par value of the bond"
)

periods_per_year = st.sidebar.selectbox(
    "Compounding Periods per Year",
    options=[1, 2, 4, 12, 365],
    index=1,
    help="Number of times interest is compounded per year"
)

# Bond calculation functions
def bond_value2(face_value, coupon_apr, maturity_years, periods_per_year, ytm_apr):
    """Calculate bond value using present value and annuity present value"""
    pv_face = face_value / ((1+ytm_apr/periods_per_year)**(maturity_years * periods_per_year))
    coupon = face_value * (coupon_apr/periods_per_year)
    actual_rate = (ytm_apr / periods_per_year)
    actual_periods = maturity_years * periods_per_year
    value = (coupon/actual_rate)*(1-((1+actual_rate)** (-1* actual_periods))) + pv_face
    return value

def mac_duration(face_value, coupon_apr, maturity_years, periods_per_year, ytm_apr):
    """Calculate Macaulay duration"""
    total_periods = maturity_years * periods_per_year
    periodic_coupon = face_value * (coupon_apr / periods_per_year)
    
    periods_series = pd.Series(range(1,total_periods + 1), name = 'Period')
    coupon_series = pd.Series([periodic_coupon] * total_periods, name = "Coupon Payment")
    face_values = [0] * (total_periods -1) + [face_value]
    face_value_series = pd.Series(face_values, name = "Face Value")

    total_cf = coupon_series + face_value_series
    total_cf.name = "Total Cash Flow"

    cf_pv = total_cf / ((1 + (ytm_apr / periods_per_year))**periods_series)
    cf_pv.name = "PV of Total Cash Flow"

    wt_pv = cf_pv * periods_series
    wt_pv.name = "Weighted PV"
    
    maturity_frame = pd.concat([periods_series, coupon_series, face_value_series, total_cf, cf_pv, wt_pv], axis = 1)
    maturity_frame_transpose = maturity_frame.T
    maturity_frame_transpose['Total'] = maturity_frame_transpose.sum(axis = 1)
    maturity_frame = maturity_frame_transpose.T
    weighted_pv = maturity_frame.loc['Total', 'Weighted PV']
    total_pv = maturity_frame.loc['Total', 'PV of Total Cash Flow']
    duration = weighted_pv / total_pv

    return duration

def mod_duration(face_value, coupon_apr, maturity_years, periods_per_year, ytm_apr):
    """Calculate modified duration"""
    total_periods = maturity_years * periods_per_year
    periodic_coupon = face_value * (coupon_apr / periods_per_year)
    
    periods_series = pd.Series(range(1,total_periods + 1), name = 'Period')
    coupon_series = pd.Series([periodic_coupon] * total_periods, name = "Coupon Payment")
    face_values = [0] * (total_periods -1) + [face_value]
    face_value_series = pd.Series(face_values, name = "Face Value")

    total_cf = coupon_series + face_value_series
    total_cf.name = "Total Cash Flow"

    cf_pv = total_cf / ((1 + (ytm_apr / periods_per_year))**periods_series)
    cf_pv.name = "PV of Total Cash Flow"

    wt_pv = cf_pv * periods_series
    wt_pv.name = "Weighted PV"
    
    maturity_frame = pd.concat([periods_series, coupon_series, face_value_series, total_cf, cf_pv, wt_pv], axis = 1)
    maturity_frame_transpose = maturity_frame.T
    maturity_frame_transpose['Total'] = maturity_frame_transpose.sum(axis = 1)
    maturity_frame = maturity_frame_transpose.T
    weighted_pv = maturity_frame.loc['Total', 'Weighted PV']
    total_pv = maturity_frame.loc['Total', 'PV of Total Cash Flow']
    duration = weighted_pv / total_pv

    mod_duration = duration / (1+(ytm_apr / periods_per_year))

    return mod_duration

# Calculate bond metrics
try:
    value_calc = bond_value2(face_value, coupon_rate, maturity_years, periods_per_year, ytm_apr)
    mac_calc = mac_duration(face_value, coupon_rate, maturity_years, periods_per_year, ytm_apr)
    mac_years = mac_calc / periods_per_year
    mod_calc = mod_duration(face_value, coupon_rate, maturity_years, periods_per_year, ytm_apr) / periods_per_year
    
    # Display results in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Bond Value",
            value=f"${value_calc:,.2f}",
            delta=f"{((value_calc - face_value) / face_value * 100):.2f}% from par"
        )
    
    with col2:
        st.metric(
            label="Macaulay Duration (Periods)",
            value=f"{mac_calc:.2f}",
            help="Duration in compounding periods"
        )
    
    with col3:
        st.metric(
            label="Macaulay Duration (Years)",
            value=f"{mac_years:.2f}",
            help="Duration in years"
        )
    
    with col4:
        st.metric(
            label="Modified Duration",
            value=f"{mod_calc:.2f}",
            help="Approximate % change in value for 1% YTM change"
        )
    
    # Create tabs for different visualizations
    tab1, tab2, tab3 = st.tabs(["📈 Bond Value vs YTM", "📊 Cash Flow Analysis", "📋 Bond Details"])
    
    with tab1:
        st.subheader("Bond Value vs Yield to Maturity")
        
        # Generate YTM range for plotting
        ytm_range = np.arange(0.00001, 0.5, 0.001)
        bond_values = [bond_value2(face_value, coupon_rate, maturity_years, periods_per_year, ytm) for ytm in ytm_range]
        
        # Create interactive plot with Plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=ytm_range * 100,  # Convert to percentage
            y=bond_values,
            mode='lines',
            name='Bond Value',
            line=dict(color='blue', width=2)
        ))
        
        # Add current YTM point
        fig.add_trace(go.Scatter(
            x=[ytm_apr * 100],
            y=[value_calc],
            mode='markers',
            name='Current Point',
            marker=dict(color='red', size=10, symbol='diamond')
        ))
        
        fig.update_layout(
            title="Bond Value vs Yield to Maturity",
            xaxis_title="Yield to Maturity (%)",
            yaxis_title="Bond Value ($)",
            hovermode='x unified',
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Add insights
        if value_calc > face_value:
            st.info("💡 This bond is trading at a **premium** (above par value)")
        elif value_calc < face_value:
            st.info("💡 This bond is trading at a **discount** (below par value)")
        else:
            st.info("💡 This bond is trading at **par value**")
    
    with tab2:
        st.subheader("Cash Flow Analysis")
        
        # Generate cash flow table
        total_periods = maturity_years * periods_per_year
        periodic_coupon = face_value * (coupon_rate / periods_per_year)
        
        periods = list(range(1, total_periods + 1))
        coupon_payments = [periodic_coupon] * total_periods
        face_value_payments = [0] * (total_periods - 1) + [face_value]
        total_cash_flows = [c + f for c, f in zip(coupon_payments, face_value_payments)]
        
        # Calculate present values
        pv_factors = [(1 + ytm_apr / periods_per_year) ** -p for p in periods]
        pv_cash_flows = [cf * pv for cf, pv in zip(total_cash_flows, pv_factors)]
        weighted_pv = [pv * p for pv, p in zip(pv_cash_flows, periods)]
        
        # Create DataFrame
        cf_df = pd.DataFrame({
            'Period': periods,
            'Coupon Payment': coupon_payments,
            'Face Value': face_value_payments,
            'Total Cash Flow': total_cash_flows,
            'PV Factor': [f"{pv:.4f}" for pv in pv_factors],
            'PV of Cash Flow': [f"${pv:.2f}" for pv in pv_cash_flows],
            'Weighted PV': [f"${wpv:.2f}" for wpv in weighted_pv]
        })
        
        st.dataframe(cf_df, use_container_width=True)
        
        # Summary statistics
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total PV of Cash Flows", f"${sum(pv_cash_flows):,.2f}")
        with col2:
            st.metric("Total Weighted PV", f"${sum(weighted_pv):,.2f}")
    
    with tab3:
        st.subheader("Bond Details")
        
        # Create a detailed summary
        details_data = {
            "Parameter": [
                "Face Value",
                "Coupon Rate (APR)",
                "Coupon Rate (Periodic)",
                "Maturity (Years)",
                "Maturity (Periods)",
                "YTM (APR)",
                "YTM (Periodic)",
                "Compounding Frequency"
            ],
            "Value": [
                f"${face_value:,.2f}",
                f"{coupon_rate:.1%}",
                f"{coupon_rate/periods_per_year:.4%}",
                f"{maturity_years} years",
                f"{maturity_years * periods_per_year} periods",
                f"{ytm_apr:.1%}",
                f"{ytm_apr/periods_per_year:.4%}",
                f"{periods_per_year}x per year"
            ]
        }
        
        details_df = pd.DataFrame(details_data)
        st.dataframe(details_df, use_container_width=True)
        
        # Bond pricing insights
        st.subheader("💡 Pricing Insights")
        
        if coupon_rate > ytm_apr:
            st.success("**Premium Bond**: Coupon rate > YTM → Bond trades above par")
        elif coupon_rate < ytm_apr:
            st.warning("**Discount Bond**: Coupon rate < YTM → Bond trades below par")
        else:
            st.info("**Par Bond**: Coupon rate = YTM → Bond trades at par")
        
        # Duration insights
        st.subheader("📊 Duration Insights")
        st.write(f"**Macaulay Duration**: {mac_years:.2f} years")
        st.write(f"**Modified Duration**: {mod_calc:.2f} (approximate % change for 1% YTM change)")
        st.write(f"**Duration in Periods**: {mac_calc:.2f} periods")
        
        # Interest rate risk
        price_change_1pct = -mod_calc * 0.01 * value_calc
        st.write(f"**Estimated price change for 1% YTM increase**: ${price_change_1pct:.2f}")

except Exception as e:
    st.error(f"Error in calculations: {str(e)}")
    st.info("Please check your input parameters and try again.")

# Footer
st.markdown("---")
st.markdown("*This app was converted from a Jupyter notebook for Financial Analytics Problem Set 2*") 