import pandas as pd

# Load the data from the zip file
file_path = 'data/winemag-data-130k-v2.csv.zip'
df = pd.read_csv(file_path)

# Create a summary of the data
# Group by 'country', count the number of reviews, and calculate the average points
summary = df.groupby('country').agg(
    count=('country', 'size'),
    points=('points', 'mean')
).reset_index()

# Sort by number of reviews in descending order for better readability
summary = summary.sort_values(by='count', ascending=False)

# Write the summary to a CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary written to data/reviews-per-country.csv")