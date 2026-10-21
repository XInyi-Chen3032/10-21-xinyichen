import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# 1. Page Configuration
# ==========================================

st.set_page_config(
    page_title="Global Superstore Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# 2. Load Data
# ==========================================

@st.cache_data
def load_data():

    file_path = "Global Superstore.xls"

    df = pd.read_excel(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Convert numerical columns
    numerical_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Shipping Cost"
    ]

    for col in numerical_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


try:
    df = load_data()

except Exception as e:
    st.error(
        "Unable to load the dataset. "
        "Please check the Excel file and its column names."
    )

    st.exception(e)
    st.stop()


# ==========================================
# 3. Dashboard Title
# ==========================================

st.title("🌍 Global Superstore Sales Dashboard")

st.write(
    "This dashboard helps retail sales managers "
    "monitor sales performance, profitability, "
    "and order priorities."
)

st.caption(
    "Data source: Global Superstore dataset"
)


# ==========================================
# 4. Sidebar Filters
# ==========================================

st.sidebar.header("Dashboard Filters")

# Order Priority Filter

if "Order Priority" in df.columns:

    priority_options = sorted(
        df["Order Priority"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )

    selected_priorities = st.sidebar.multiselect(
        "Select Order Priority",
        options=priority_options,
        default=priority_options
    )

else:
    selected_priorities = None


# Discount Filter

if "Discount" in df.columns:

    min_discount = float(
        df["Discount"].min()
    )

    max_discount = float(
        df["Discount"].max()
    )

    discount_range = st.sidebar.slider(
        "Select Discount Range",
        min_value=min_discount,
        max_value=max_discount,
        value=(min_discount, max_discount)
    )

else:
    discount_range = None


# ==========================================
# 5. Apply Filters
# ==========================================

filtered_df = df.copy()

if selected_priorities is not None:

    filtered_df = filtered_df[
        filtered_df["Order Priority"]
        .astype(str)
        .isin(selected_priorities)
    ]

if discount_range is not None:

    filtered_df = filtered_df[
        filtered_df["Discount"].between(
            discount_range[0],
            discount_range[1]
        )
    ]


# ==========================================
# 6. Key Performance Indicators
# ==========================================

st.subheader("Key Performance Indicators")

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_quantity = filtered_df["Quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    f"${total_sales:,.2f}"
)

col2.metric(
    "Total Profit",
    f"${total_profit:,.2f}"
)

col3.metric(
    "Total Quantity",
    f"{total_quantity:,.0f}"
)


# ==========================================
# 7. Sales by Order Priority
# ==========================================

st.subheader("Sales by Order Priority")

if (
    "Order Priority" in filtered_df.columns
    and not filtered_df.empty
):

    priority_sales = (
        filtered_df
        .groupby("Order Priority", as_index=False)
        ["Sales"]
        .sum()
    )

    fig1 = px.bar(
        priority_sales,
        x="Order Priority",
        y="Sales",
        title="Total Sales by Order Priority",
        labels={
            "Order Priority": "Order Priority",
            "Sales": "Total Sales"
        },
        text_auto=".2s"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

else:
    st.info(
        "No data available for the selected filters."
    )


# ==========================================
# 8. Sales vs Profit
# ==========================================

st.subheader("Sales vs. Profit")

if not filtered_df.empty:

    fig2 = px.scatter(
        filtered_df,
        x="Sales",
        y="Profit",
        color="Order Priority",
        size="Quantity",
        hover_data=[
            c for c in [
                "Sales",
                "Profit",
                "Discount",
                "Shipping Cost",
                "Order Priority"
            ]
            if c in filtered_df.columns
        ],
        title="Relationship Between Sales and Profit"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

else:
    st.info(
        "No data available for the selected filters."
    )


# ==========================================
# 9. Profit by Discount
# ==========================================

st.subheader("Profit by Discount")

if (
    "Discount" in filtered_df.columns
    and "Profit" in filtered_df.columns
    and not filtered_df.empty
):

    discount_profit = (
        filtered_df
        .groupby("Discount", as_index=False)
        ["Profit"]
        .mean()
        .sort_values("Discount")
    )

    fig3 = px.line(
        discount_profit,
        x="Discount",
        y="Profit",
        markers=True,
        title="Average Profit by Discount Level",
        labels={
            "Discount": "Discount",
            "Profit": "Average Profit"
        }
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

else:
    st.info(
        "No data available for the selected filters."
    )


# ==========================================
# 10. Data Preview
# ==========================================

with st.expander("View Filtered Data"):

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True
    )


# ==========================================
# 11. Data Information
# ==========================================

st.divider()

st.subheader("Data and Refresh Information")

st.write(
    "**Current data source:** "
    "Static Global Superstore Excel dataset."
)

st.write(
    "**Current refresh status:** "
    "The application does not automatically retrieve new data."
)

st.write(
    "**Proposed production refresh:** "
    "Weekly, or more frequently if the business requires it."
)

st.caption(
    "Sales and profit figures reflect the selected records. "
    "The observed relationship between discounts and profit "
    "does not necessarily establish causation."
)
