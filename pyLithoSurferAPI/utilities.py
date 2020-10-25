import numpy as np

url = str

# Convert if data is not nan or None
# This is to make sure that we are pushing the right type to the API.
convert_int = lambda x: int(x) if (x and not np.isnan(x)) or x == 0 else None
convert_float = lambda x: float(x) if (x and not np.isnan(x)) or x == 0 else None

def convert_str(value):
        if value is None:
            return None
        if isinstance(value, str):
            return value.strip()
        if np.isnan(value):
            return None