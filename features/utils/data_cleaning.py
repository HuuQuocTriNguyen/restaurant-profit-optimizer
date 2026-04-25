import pandas as pd
from features.utils.find_column import find_column

def data_clean(file_path):
    df = pd.read_csv(file_path, encoding="ISO-8859-1")

    df.columns = df.columns.str.strip().str.lower()

    date_col = find_column(df, ["date", "time"])
    product_col = find_column(df, ["product", "item", "name"])
    price_col = find_column(df, ["price", "unit price"])
    quantity_col = find_column(df, ["quantity", "qty"])

    if date_col:
        df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
        df = df[df[date_col].notna()]

    if price_col:
        df[price_col] = pd.to_numeric(df[price_col], errors="coerce")

    if quantity_col:
        df[quantity_col] = pd.to_numeric(df[quantity_col], errors="coerce")

    if product_col:
        df[product_col] = df[product_col].astype(str).str.lower().str.strip()

    df = df.dropna(subset=[price_col, quantity_col])

    df["revenue"] = df[price_col] * df[quantity_col]

    return df, {
        "date": date_col,
        "product": product_col,
        "price": price_col,
        "quantity": quantity_col
    }
    
