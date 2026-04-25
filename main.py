import streamlit as st
from features.utils.data_cleaning import data_clean
from features.utils.extract import top_product, total_revenue, sales_per_day, total_orders, worst_products
from features.hours_insight import sales_by_time_of_day, average_sales_by_time_of_day

st.set_page_config(layout = "wide")
st.title("Restaurant Profit Optimizer")

st.sidebar.header("Controls")

file = st.sidebar.file_uploader("Upload CSV")

if file:
    df, cols = data_clean(file)   

    data = average_sales_by_time_of_day(df, cols["date"])
    best_time = data.idxmax()
    worst_time = data.idxmin()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", total_revenue(df))
    col2.metric("Orders", total_orders(df, cols["quantity"]))
    col3.metric("Best period", best_time, "increase staff & Upsell combos")
    col4.metric("Worst period", worst_time, "Run promotions or discounts", "inverse")

    st.subheader("Top Products")
    st.bar_chart(top_product(df, cols["product"]), x_label="Product names", y_label="Total Revenue", color="green")

    st.subheader("Products to Reconsider")
    st.bar_chart(worst_products(df, cols["product"]), x_label="Product names", y_label="Quantity", color="red")

    st.subheader("Average Sales")
    st.scatter_chart(sales_per_day(df, cols["date"]), x_label="Date", y_label="USD")

    st.subheader("Revenue by Time of Day")
    st.line_chart(sales_by_time_of_day(df))

    st.subheader("Average Revenue by Time of Day")
    st.line_chart(average_sales_by_time_of_day(df, cols["date"]))

