import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data csv/marketing_campaign_cleaned.csv")

# Create Total Spending column
df["Total_Spending"] = (
    df["MntWines"] +
    df["MntFruits"] +
    df["MntMeatProducts"] +
    df["MntFishProducts"] +
    df["MntSweetProducts"] +
    df["MntGoldProds"]
)

# Title
st.title("📊 Marketing Analytics Dashboard")
st.write("Welcome to the Marketing Analytics Dashboard!")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Total Customers", len(df))
col2.metric("💰 Total Income", f"₹{df['Income'].sum():,.0f}")
col3.metric("🛒 Total Spending",f"₹{df['Total_Spending'].sum():,.0f}")
col4.metric("📈 Average Spending", f"{df['Total_Spending'].mean():.2f}")

st.markdown("---")

# Project Summary
st.subheader("📌 Project Overview")

st.write("""
This dashboard provides insights into:

- Customer Spending Analysis
- Product Performance
- Campaign Performance
- Customer Segmentation
- Purchase Channel Analysis
- SQL Analytics
""")

st.sidebar.success("Select a page from the sidebar.")