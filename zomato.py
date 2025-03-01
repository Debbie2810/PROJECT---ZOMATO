import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/mnt/data/ZomatoRestaurantsIndia.csv'  # Adjust if needed
df = pd.read_csv(file_path)

# Display basic info
display(df.head())
display(df.info())

def clean_data(df):
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Handling missing values
    df = df.dropna(subset=['Rating', 'Cuisines', 'Price range'])  # Drop rows with critical missing values
    
    # Convert Rating to numeric
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    
    return df

df = clean_data(df)

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10,5))
sns.histplot(df['Rating'], bins=20, kde=True, color='blue')
plt.title('Distribution of Ratings')
plt.show()

# Price Range Distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Price range', data=df, palette='coolwarm')
plt.title('Price Range Distribution')
plt.show()

# Top 10 most common cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
plt.figure(figsize=(12,6))
top_cuisines.plot(kind='bar', color='teal')
plt.title('Top 10 Most Common Cuisines')
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Delivery vs Takeaway Count
plt.figure(figsize=(8,5))
sns.countplot(x='Has Online delivery', data=df, palette='viridis')
plt.title('Online Delivery Availability')
plt.show()

plt.figure(figsize=(8,5))
sns.countplot(x='Has Table booking', data=df, palette='plasma')
plt.title('Table Booking Availability')
plt.show()

print("Data Cleaning and Visualization Complete ✅")
