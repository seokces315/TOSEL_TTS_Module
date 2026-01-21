import pandas as pd


# Load a CSV file into a pandas DataFrame
def load_csv(data_path):
    # Define general dtypes for text columns to ensure stable parsing
    dtype = {
        "No.": "string",
        "Script": "string",
        "Type": "string",
    }

    # Load CSV with a robust parser
    df = pd.read_csv(
        data_path,
        header=0,
        dtype=dtype,
        encoding="utf-8",
        engine="python",
    )

    # Return the loaded DataFrame
    return df
