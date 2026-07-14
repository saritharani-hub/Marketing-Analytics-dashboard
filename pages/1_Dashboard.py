import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_connection

st.title("📊 Marketing Dashboard")

conn = get_connection()

query = """
SELECT
    COUNT(*) AS Total_Customers,
    ROUND(AVG(Income),2) AS Average_Income,
    SUM(Total_Spending) AS Total_Spending,
    SUM(Response) AS Total_Responses
FROM marketing_analysis;
"""

df = pd.read_sql(query, conn)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Customers", int(df["Total_Customers"][0]))
col2.metric("Avg Income", f"{df['Average_Income'][0]:,.2f}")
col3.metric("Total Spending", f"{df['Total_Spending'][0]:,.0f}")
col4.metric("Responses", int(df["Total_Responses"][0]))

st.dataframe(df)

query = """
SELECT
    SUM(MntWines) AS Wines,
    SUM(MntFruits) AS Fruits,
    SUM(MntMeatProducts) AS Meat,
    SUM(MntFishProducts) AS Fish,
    SUM(MntSweetProducts) AS Sweets,
    SUM(MntGoldProds) AS Gold
FROM marketing_analysis;
"""

product_df = pd.read_sql(query, conn)

chart_df = pd.DataFrame({
    "Product": ["Wines", "Fruits", "Meat", "Fish", "Sweets", "Gold"],
    "Amount": product_df.iloc[0].values
})

fig = px.bar(
    chart_df,
    x="Product",
    y="Amount",
    text="Amount",
    title="Total Spending by Product"
)

st.plotly_chart(fig, use_container_width=True)