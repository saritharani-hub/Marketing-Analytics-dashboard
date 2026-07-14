import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_connection

st.title("👥 Customer Segmentation")

conn = get_connection()

query = """
SELECT
CASE
    WHEN Income >= 75000 THEN 'High Income'
    WHEN Income BETWEEN 40000 AND 74999 THEN 'Middle Income'
    ELSE 'Low Income'
END AS Income_Group,
COUNT(*) AS Customers
FROM marketing_analysis
GROUP BY Income_Group;
"""
df = pd.read_sql(query, conn)
st.subheader("Income Segmentation")

st.dataframe(df)

fig = px.bar(
    df,
    x="Income_Group",
    y="Customers",
    color="Income_Group",
    text="Customers",
    title="Customers by Income Group"
)

st.plotly_chart(fig, use_container_width=True)