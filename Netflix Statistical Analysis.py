import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


#Load dataset
netflix = pd.read_csv("/Users/captainmj/Downloads/netflix_titles.csv")



netflix.head()

netflix.tail()

netflix.shape

netflix.columns


# Check for missing values
print(netflix.isnull().sum())


# drop rows with missing values for simplicity 
netflix.dropna(inplace=True)
netflix


# Get descriptive statistics 
print(netflix.describe())



# Plot histogram for release_year 
plt.hist(netflix["release_year"], bins=30) 
plt.xlabel("Release Year") 
plt.ylabel("Count")
plt.title("Histogram of Release Year")
plt.show()


# Plot scatterplot for duration
sns.scatterplot(x="release_year", y="duration", data=netflix) 
plt.xlabel("Release Year")
plt.ylabel("Duration")
plt.title("Scatterplot of Duration by Release Year") 
plt.show()


# Get the top 5 countries with the most movies and TV shows
top_countries = netflix['country'].value_counts().head(5).index.tolist()

# Create a bar chart
plt.figure(figsize=(12,7))
ax = sns.countplot(x='country', data=netflix[netflix['country'].isin(top_countries)])
for i in ax.containers:
    plt.bar_label(i, label_type='edge')
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Top 5 Countries with the Most Movies and TV Shows')
plt.ylim(0,3000)
plt.show()


# Histogram of type distribution
ax = sns.histplot(data=netflix, x='type', bins=20) 
for i in ax.containers:
    plt.bar_label(i)
plt.ylim(0,7000)
plt.show()


netflix_movies = netflix[netflix['type'] == 'Movie'] 
print(netflix_movies.shape)



# filtering only the movies with existing duration
movies_data = netflix[netflix['duration']!= 0]
m_subset = movies_data[['title','country','release_year','listed_in','duration']]
m_subset.head()
movies_data.describe()



#Plot Histogram for release year of movies
plt.hist(netflix_movies["release_year"], bins=30) 
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.title("Histogram of Release Year for Movies")
plt.show()


#Get descriptive statistics for TV Shows only 
tv_shows_data = netflix[netflix["type"]=="TV Show"] 
print(tv_shows_data.describe())


#Plot Histogram for release year of tv shows
plt.hist(tv_shows_data['release_year'], bins=30) 
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.title('Distribution of Release Year for TV Shows')
plt.show()


# Pie chart of the proportion of TV shows and movies
type_counts = netflix['type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%')
plt.title('Proportion of TV Shows and Movies')
plt.show()


# Line plot of the count of TV shows and movies over time
time_counts = netflix.groupby(['release_year', 'type'])['show_id'].count().reset_index()
sns.lineplot(x='release_year', y='show_id', hue='type', data=time_counts)
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.title('Number of TV Shows and Movies over Time')
plt.show()



# Stacked bar plot of the count of TV shows and movies by rating and type
rating_counts = netflix.groupby(['rating', 'type'])['show_id'].count().reset_index()
sns.barplot(x='rating', y='show_id', hue='type', data=rating_counts)
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.title('Number of TV Shows and Movies by Rating and Type')
plt.show()



