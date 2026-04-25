import pandas as pd
import re

order = ["Morning", "Afternoon", "Evening", "Night"]

def sales_by_time_of_day(df):
    df = df.copy()
    time_col = 'time_of_sale'
    sales = df.groupby(time_col)["revenue"].sum()
    sales = sales.reindex(order)
    
    return sales


def average_sales_by_time_of_day(df, date_col):
    df = df.copy()
    df["date_only"] = df[date_col].dt.date
    grouped = df.groupby(["date_only", "time_of_sale"])["revenue"].sum()
    avg = grouped.groupby("time_of_sale").mean()

    return avg.reindex(order)

