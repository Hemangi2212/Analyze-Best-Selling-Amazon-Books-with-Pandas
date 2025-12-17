# Import the Lib 
import pandas as pd

# Then load the dataset 
df = pd.read_csv('bestsellers.csv')

# Print first 5 rows 
print(df.head())

# Get the shape dataset
print(df.shape)

# Get the columns names in dataset 
print(df.columns)

# Summary statistics for each column
print(df.describe())

# -------------------------------------------- Cleaning the dataset -------------------------------------- 

# Removing the Duplicates values 
df.drop_duplicates(inplace=True)

df["Price"] = df["Price"].astype(float)


# Rename the col 
df.rename(
    columns={
        "Name": "Title",
        "Year": "Publication Year",
        "User Rating": "Rating"
    },
    inplace=True
)

# Total Author Count 
author_counts = df['Author'].value_counts()
print(author_counts)

# Get rating 
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# First top 10 best sellers and Convert data into CSV file 
author_counts.head(10).to_csv("top_authors.csv")
