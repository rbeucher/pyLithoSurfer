import numpy as np

url = str

# Convert if data is not nan or None
# This is to make sure that we are pushing the right type to the API.
convert_str = lambda x: str(x).strip() if x else None
convert_int = lambda x: int(x) if x else None
convert_float = lambda x: float(x) if x and not isinstance(x, np.nan) else None