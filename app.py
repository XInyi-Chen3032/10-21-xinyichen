import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("Global Superstore Sales Dashboard")
st.subheader("See more filters in the sidebar")

df = pd.read_excel("Global Superstore.xls")

# 侧边栏筛选
st.sidebar.header("Filters")
region_list = sorted(df["Region"].unique())
selected_region = st.sidebar.multiselect("Select Region", region_list, default=region_list)

category_list = sorted(df["Category"].unique())
selected_category = st.sidebar.multiselect("Select Category", category_list, default=category_list)

min_sales_val = float(df["Sales"].min())
max_sales_val = float(df["Sales"].max())
sales_range = st.sidebar.slider("Sales Range", min_sales_val, max_sales_val, (min_sales_val, max_sales_val))

# 筛选逻辑
df_filtered = df[
    (df["Region"].isin(selected_region)) &
    (df["Category"].isin(selected_category)) &
    (df["Sales"] >= sales_range[0]) &
    (df["Sales"] <= sales_range[1])
]

st.markdown("### Filtered Order Table")
st.dataframe(df_filtered, use_container_width=True)

st.markdown("### Total Sales by Sub-Category")
sales_by_subcat = df_filtered.groupby("Sub-Category")["Sales"].sum().reset_index()
st.bar_chart(sales_by_subcat, x="Sub-Category", y="Sales")
