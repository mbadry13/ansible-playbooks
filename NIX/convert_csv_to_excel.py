import pandas as pd
import sys

if len(sys.argv) != 3:
    print("Usage: python convert_csv_to_excel.py <input_csv> <output_xlsx>")
    sys.exit(1)

input_csv = sys.argv[1]
output_xlsx = sys.argv[2]

df = pd.read_csv(input_csv)
df.to_excel(output_xlsx, index=False, engine='openpyxl')
