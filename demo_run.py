import pandas as pd

from etl import bronze, silver

# Load your raw CSV (update the path as needed)
raw_path = "./data/raw.csv"
df_raw = pd.read_csv(raw_path)

# Dummy lookup table
country_lookup = {
    "us": "USA", "united states": "USA", "uk": "GBR", "gb": "GBR",
}

# Run bronze then silver
df_bronze, rep_bronze = bronze.run(df_raw)
df_silver, rep_silver = silver.run(
    df_bronze,
    resources={"country_lookup": country_lookup}
)

# Save outputs
df_bronze.to_csv("./data/bronze.csv", index=False)
df_silver.to_csv("./data/silver.csv", index=False)

print("Bronze saved to ./data/bronze.csv")
print("Silver saved to ./data/silver.csv")

print("Bronze report")
print(rep_bronze['column_metrics'])
print(rep_bronze['record_passed'])
print(rep_bronze['dataset_pass_rate'])

print("\n---\n")

print("Silver report")
print(rep_silver['column_metrics'])
print(rep_silver['record_passed'])
print(rep_silver['dataset_pass_rate'])
