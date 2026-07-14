import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_connection

st.title("🛒 Channel Analysis")

conn = get_connection()

query = """
SELECT
    SUM(NumWebPurchases) AS Web_Purchases,
    SUM(NumStorePurchases) AS Store_Purchases,
    SUM(NumCatalogPurchases) AS Catalog_Purchases,
    SUM(NumDealsPurchases) AS Deal_Purchases
FROM marketing_analysis;
"""
df = pd.read_sql(query, conn)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Web", int(df["Web_Purchases"][0]))
col2.metric("Store", int(df["Store_Purchases"][0]))
col3.metric("Catalog", int(df["Catalog_Purchases"][0]))
col4.metric("Deals", int(df["Deal_Purchases"][0]))

st.subheader("Channel Performance")

st.dataframe(df)

channel_df = pd.DataFrame({
    "Channel": ["Web", "Store", "Catalog", "Deals"],
    "Purchases": [
        df["Web_Purchases"][0],
        df["Store_Purchases"][0],
        df["Catalog_Purchases"][0],
        df["Deal_Purchases"][0]
    ]
})

fig = px.bar(
    channel_df,
    x="Channel",
    y="Purchases",
    text="Purchases",
    color="Channel",
    title="Purchases by Channel"
)

st.plotly_chart(fig, use_container_width=True)