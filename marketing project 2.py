import streamlit as st

st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


st.set_page_config(
    page_title="Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("📊 Marketing Analytics")
st.sidebar.write(
    "Analyze customer behavior, campaigns, products, and sales channels."
)

# Main Title
st.title("📊 Marketing Campaign Analytics Dashboard")

# Welcome
st.markdown("## Welcome 👋")

st.write("""
This Marketing Campaign Analytics Dashboard helps analyze customer purchasing
behavior, campaign performance, product sales, and marketing channels.

Use the navigation menu on the left to explore the analytics pages.
""")

# Two Columns
col1, col2 = st.columns(2)

with col1:
    st.info("""
### 📊 Dashboard Features
- Dashboard
- Product Analysis
- Campaign Analysis
- Customer Segmentation
- Channel Analysis
- Customer Insights
- SQL Analytics
""")

with col2:
    st.success("""
### 🎯 Project Objectives
- Analyze customer behavior
- Compare campaign performance
- Understand sales channels
- Identify high-value products
- Generate business recommendations
""")

st.markdown("---")

# Workflow
st.subheader("📌 Workflow")

st.write("""
Customer Data
⬇️

MySQL Database
⬇️

Python + Pandas
⬇️

Streamlit Dashboard
⬇️

Business Insights
""")

st.markdown("---")

st.success("✅ Marketing Campaign Analytics Dashboard is ready to use.")
st.sidebar.write(
    "Analyze customer behavior, campaigns, products, and sales channels."
)

st.write("Welcome to the Marketing Analytics Dashboard.")

st.write("""
Use the sidebar to navigate between:

- Dashboard
- Product Analysis
- Campaign Analysis
- Customer Segmentation
- Channel Analysis
- Customer Insights
- SQL Analytics
""")

st.success("Project setup completed successfully!")