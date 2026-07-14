import streamlit as st
import pandas as pd
from db import get_connection

st.title("📑 SQL Analytics")

conn = get_connection()

query = """
SELECT
    Country,
    COUNT(*) AS Customers,
    ROUND(AVG(Income),2) AS Avg_Income
FROM marketing_analysis
GROUP BY Country
ORDER BY Customers DESC;
"""

df = pd.read_sql(query, conn)

st.subheader("Customers by Country")

st.dataframe(df)

import plotly.express as px

fig = px.bar(
    df,
    x="Country",
    y="Customers",
    text="Customers",
    color="Country",
    title="Customers by Country"
)

st.subheader("Average Income by Country")

fig2 = px.bar(
    df,
    x="Country",
    y="Avg_Income",
    text="Avg_Income",
    color="Country",
    title="Average Income by Country"
)

st.plotly_chart(fig2, use_container_width=True)

