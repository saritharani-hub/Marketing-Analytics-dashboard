import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_connection

st.title("📦 Product Analysis")

conn = get_connection()

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

df = pd.read_sql(query, conn)
conn.close()

products = pd.DataFrame({
    "Product": ["Wines","Fruits","Meat","Fish","Sweets","Gold"],
    "Amount":[
        df["Wines"][0],
        df["Fruits"][0],
        df["Meat"][0],
        df["Fish"][0],
        df["Sweets"][0],
        df["Gold"][0]
    ]
})

fig = px.bar(
    products,
    x="Product",
    y="Amount",
    text="Amount",
    title="Total Spending by Product Category"
)

st.plotly_chart(fig, use_container_width=True)