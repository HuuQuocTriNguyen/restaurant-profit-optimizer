import pandas as pd


def total_revenue(df):
    if "revenue" not in df.columns:
        raise ValueError("Missing 'revenue'. Did you run data_clean()?")
    
    results = int(df['revenue'].sum())
    return f"${results:,}"

def total_orders(df, quantity_col):
    return int(df[quantity_col].sum())

def top_product(df, product_col, top_n=5):
    product_revenue = (
        df.groupby(product_col)["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    top = product_revenue.head(top_n)
    others = pd.Series(product_revenue.iloc[top_n:].sum(), index=["Others"])

    return pd.concat([top, others])

    
def sales_per_day(df, date_col):
    daily_sales = df.groupby(date_col)["revenue"].sum().sort_index()

    smoothed = daily_sales.rolling(window=7, min_periods=1).mean()

    return smoothed


def worst_products(df, product_col, n=5):
    return (
        df.groupby(product_col)["quantity"]
        .sum()
        .sort_values(ascending=True)
        .head(n)
    )