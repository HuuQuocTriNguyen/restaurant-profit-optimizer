import re

def find_column(df, patterns):
    for pattern in patterns:
        regex = re.compile(pattern, re.IGNORECASE)
        for col in df.columns:
            if regex.search(col):
                return col
    return None


