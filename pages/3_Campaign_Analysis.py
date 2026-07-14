import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_connection

st.title("📢 Campaign Analysis")

from db import get_connection
conn = get_connection()

import pandas as pd

query = """
SELECT
    SUM(AcceptedCmp1) AS Campaign1,
    SUM(AcceptedCmp2) AS Campaign2,
    SUM(AcceptedCmp3) AS Campaign3,
    SUM(AcceptedCmp4) AS Campaign4,
    SUM(AcceptedCmp5) AS Campaign5,
    SUM(Response) AS FinalResponse
FROM marketing_analysis;
"""
df = pd.read_sql(query, conn)

# 👇 ADD THE KPI METRICS HERE
col1, col2, col3 = st.columns(3)

col1.metric("Campaign 1", int(df["Campaign1"][0]))
col2.metric("Campaign 4", int(df["Campaign4"][0]))
col3.metric("Final Response", int(df["FinalResponse"][0]))

# 👇 Then show the table
st.subheader("Campaign Performance")

st.dataframe(df)

campaign_df = pd.DataFrame({
    "Campaign": [
        "Campaign 1",
        "Campaign 2",
        "Campaign 3",
        "Campaign 4",
        "Campaign 5"
    ],
    "Accepted": [
        df["Campaign1"][0],
        df["Campaign2"][0],
        df["Campaign3"][0],
        df["Campaign4"][0],
        df["Campaign5"][0]
    ]
})

fig = px.bar(
    campaign_df,
    x="Campaign",
    y="Accepted",
    text="Accepted",
    color="Campaign",
    title="Campaign Acceptance"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)