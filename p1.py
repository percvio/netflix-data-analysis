import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')
#print(df)

df_filled = df
df_filled = df_filled.dropna(subset=['type', 'release_year']) # Remove rows where type or release_year are NaN for plots

# Convert movie duration to numeric (assuming NaNs in movies were handled or are rare)
is_movie = df_filled['type'] == 'Movie'
# Ensure remaining movie entries that are NOT NaN are strings before replacing ' min'
df_filled.loc[is_movie, 'duration'] = df_filled.loc[is_movie, 'duration'].astype(str).str.replace(' min', '', regex=False)
# Now convert only numeric strings to int, NaNs and series strings will remain as they are or become NaN if conversion fails
df_filled.loc[is_movie, 'duration'] = pd.to_numeric(df_filled.loc[is_movie, 'duration'], errors='coerce') # Use coerce to handle original NaNs or conversion errors


# Fill other NaNs with 'Unknown' for categorical columns used in value_counts
cat_cols_to_fill = ['director', 'cast', 'country', 'rating', 'listed_in']
for col in cat_cols_to_fill:
    df_filled[col] = df_filled[col].fillna('Unknown')


genre_df_filled = df_filled['listed_in'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row
director_df_filled = df_filled['director'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row
cast_df_filled = df_filled['cast'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row


print("\nExample DataFrame filled.\n")
print(df_filled.info()) # Check dtypes after preparation

#print(df.head(100))
#df.info()

#print('For numeric columns\n')
#print(df.describe())

#print('For text columns\n')
#print(df.describe(include='all'))

#print("Number of missing values per column:")
#print(df.isnull().sum())



#print("Original DataFrame:")
#print(df)


df_cleaned = df.dropna() # Excludes rows that have any blank gap
#print("Cleaned Df: \n")
#print(df_cleaned)
df_cleaned.info()

df_cleaned.loc[:, 'date_added'] = pd.to_datetime(df_cleaned['date_added'], errors='coerce') # Changes the data type of the 'date_added' column from object to datetime

#print("DataFrame columns to be studied:")
#print(df_cleaned[['director', 'listed_in', 'cast']])

genre_df_cleaned = df_cleaned['listed_in'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row
director_df_cleaned = df_cleaned['director'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row
cast_df_cleaned = df_cleaned['cast'].str.split(',').explode().str.strip() # Splits the string by comma, removes whitespace, transforms each item of each list into a new row

'''
print('genres\n')
print(genre_df) # Note: Original code uses generic 'genre_df' here, likely a typo or leftover from development

print('directors\n')
print(director_df) # Note: Original code uses generic 'director_df' here

print('cast\n')
print(cast_df) # Note: Original code uses generic 'cast_df' here
'''

#print("\nGenre frequency:")
#print(genre_df.value_counts())

#print("\nDirector frequency:")
#print(director_df.value_counts())

#print("\nCast member frequency:")
#print(cast_df.value_counts())

###

#print("\nDuration column type: ")
#print(df_cleaned['duration'].dtype)

is_movie = df_cleaned['type'] == 'Movie' # Mask to identify which rows are 'movie'
df_cleaned.loc[is_movie, 'duration'] = df_cleaned.loc[is_movie, 'duration'].str.replace(' min', '', regex=False).astype(int) # str.replace removes text ' min', .astype(int) converts the result to integer, .loc ensures assignment is done on the rows

#print("\nDuration column type: ")
#print(df_cleaned['duration'].dtype)

print("\nExample cleaned DataFrame.\n")
print(df_cleaned.info())

print("\n Most frequent countries (cleaned data) : ")
print(df_cleaned['country'].value_counts())

print("\n Most frequent countries (filled data): ")
print(df_filled['country'].value_counts())

print("\n Most frequent genres (cleaned data) : ")
print(df_cleaned['listed_in'].value_counts())

print("\n Most frequent genres (filled data): ")
print(df_filled['listed_in'].value_counts())


genres_counts_cleaned = genre_df_cleaned[genre_df_cleaned != 'Unknown'].value_counts().head(10) # Exclude 'Unknown' if applicable
genres_counts_filled = genre_df_filled[genre_df_filled != 'Unknown'].value_counts().head(10) # Exclude 'Unknown' if applicable


# --- 3. Top 10 Most Frequent Genres ---
plt.figure(figsize=(12, 7))
sns.barplot(x=genres_counts_cleaned.index, y=genres_counts_cleaned.values, palette='mako')
plt.title('Top 10 Most Frequent Genres (cleaned dataset)')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.tight_layout() # Adjust layout to prevent overlap
plt.show()


plt.figure(figsize=(12, 7))
sns.barplot(x=genres_counts_filled.index, y=genres_counts_filled.values, palette='mako')
plt.title('Top 10 Most Frequent Genres (filled dataset)')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right') # Rotate labels for better readability
plt.tight_layout() # Adjust layout to prevent overlap
plt.show()


# --- 1. Movie vs. TV Show Count ---
plt.figure(figsize=(7, 5))
sns.countplot(x='type', data=df_cleaned, palette='viridis')
plt.title('Movie vs. TV Show Count (cleaned DataFrame)')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')
plt.show()

plt.figure(figsize=(7, 5))
sns.countplot(x='type', data=df_filled, palette='viridis')
plt.title('Movie vs. TV Show Count (filled DataFrame)')
plt.xlabel('Content Type')
plt.ylabel('Number of Titles')
plt.show()


# --- 5. Number of Releases per Year ---
releases_per_year_cleaned = df_cleaned['release_year'].value_counts().sort_index()
releases_per_year_filled = df_filled['release_year'].value_counts().sort_index()

plt.figure(figsize=(14, 7))
sns.lineplot(x=releases_per_year_cleaned.index, y=releases_per_year_cleaned.values, marker='o', color='purple')
plt.title('Number of Titles Released per Year (cleaned DataFrame)')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid(axis='y', linestyle='--') # Add grid lines on Y axis
plt.show()

plt.figure(figsize=(14, 7))
sns.lineplot(x=releases_per_year_filled.index, y=releases_per_year_filled.values, marker='o', color='purple')
plt.title('Number of Titles Released per Year (filled DataFrame)')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles')
plt.grid(axis='y', linestyle='--') # Add grid lines on Y axis
plt.show()