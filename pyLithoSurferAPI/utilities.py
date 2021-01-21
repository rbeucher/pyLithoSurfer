import numpy as np
import pandas as pd

url = str

# Convert if data is not nan or None
# This is to make sure that we are pushing the right type to the API.
convert_int = lambda x: int(x) if not pd.isna(x) else None
convert_float = lambda x: float(x) if not pd.isna(x) else None

def convert_str(value):
        if value is None:
            return None
        if isinstance(value, str):
            return value.strip()
        if np.isnan(value):
            return None