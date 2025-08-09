# analyze_netflix.py
import pandas as pd

# Load the data
df = pd.read_csv('NetflixViewingHistory.csv')

# Show the first 5 rows
print("🔍 First 5 rows of your Netflix history:")
print(df.head())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Convert 'Duration' to total minutes (as a number)
def duration_to_minutes(duration):
    try:
        mins, secs = duration.split(':')
        return int(mins) + round(int(secs) / 60, 2)
    except:
        return 0  # in case of bad data

df['Duration_min'] = df['Duration'].apply(duration_to_minutes)

# Show updated data
print("\n✅ Data with cleaned duration (in minutes):")
print(df[['Title', 'Date', 'Duration', 'Duration_min']].head())

# Total time watched
total_hours = df['Duration_min'].sum() / 60
print(f"\n📊 Total time spent watching: {total_hours:.2f} hours")
# Plot watch time over time
import matplotlib.pyplot as plt

# Sort by date
df = df.sort_values('Date')

# Cumulative watch time
df['Cumulative_hours'] = df['Duration_min'].cumsum() / 60

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Cumulative_hours'], marker='o', linestyle='-', color='red')
plt.title('Netflix Watch Time Over Time')
plt.ylabel('Cumulative Hours Watched')
plt.xlabel('Date')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()  # Prevents labels from being cut off
plt.show()
