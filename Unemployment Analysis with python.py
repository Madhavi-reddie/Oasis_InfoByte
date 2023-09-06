## UNEMPLOYMENT ANALYSIS WITH PYTHON

Unemployment is measured by the unemployment rate which is the number of people
who are unemployed as a percentage of the total labour force. We have seen a sharp
increase in the unemployment rate during Covid-19, so analyzing the unemployment rate
can be a good data science project. 



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import plotly.express as px


import warnings

warnings.filterwarnings("ignore")

# Reading Data frame
df=pd.read_csv('Unemployment in India.csv')

# Print Dataframe
print(df)

# Print first 5 rows in dataframe
print(df.head())

#Print last 6 rows in data frame
print(df.tail(6))

#checking for null values in Dataframe
df.isnull().sum()

#removing the null values
df=df.dropna()
print(df)

# After removing null values checking null values are drop or not
df.isnull().sum()

#checking duplicate values in dataframe
df.duplicated().sum()

# shape of the dataframe
df.shape

#size of the dataframe
df.size

#columns of the dataframe
df.columns

#info od Dataframe
df.info()

#describing dataframe
df.describe()

#data types used in dataframe
df.dtypes

#counting the values in each region
df['Region'].value_counts()

#counting the values of the area
df['Area'].value_counts()

date_count = df["dat-mon-year"].nunique()
print(date_count)

#change second column name as Date from dat-mon-year
df['Date'] = pd.to_datetime(df['dat-mon-year'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

df['dat-mon-year'].value_counts()

print(df)

df = df.drop(df.columns[1], axis=1)


print(df)

region_counts = df['Region'].value_counts().reset_index()


# Create a bar plot for the count of each region
plt.figure(figsize=(10, 4))
plt.bar(region_counts['index'], region_counts['Region'])
plt.xlabel('Region')
plt.ylabel('Count')
plt.title('Count of Each Region')

plt.xticks(rotation=90)

plt.show()


area_counts = df['Area'].value_counts().reset_index()


# Create a bar plot for the count of each region
plt.figure(figsize=(6, 2))
plt.bar(area_counts['index'], area_counts['Area'])
plt.xlabel('Area')
plt.ylabel('Count')
plt.title('Count of Each Area')

plt.show()



#heat map on columns
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu', fmt='.2f', cbar=True)
plt.title('Heatmap of Correlation between Columns')
plt.show()


plt.figure(figsize=(10, 4))
sns.boxplot(x='Region', y=' Estimated_Unemployment_Rate (%)', data=df, palette='Set2')
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate')
plt.title('Boxplot of Estimated Unemployment Rate by Region')
plt.xticks(rotation=90)  
plt.show()

# Sunburst plot of Unemployement Rate based on Area
unemploment = df[["Area", "Region", " Estimated_Unemployment_Rate (%)"]]
fig = px.sunburst(unemploment, path = ["Area", "Region"], 
                     values = " Estimated_Unemployment_Rate (%)", 
                     width = 500, height=500,
                     title ="Unemployment Rate based on Area")
fig.show()

# Animation using scatterplot of Estimated_Unemployment_Rate (%)
px.scatter(data_frame = df, x = ' Estimated_Unemployment_Rate (%)', y = 'Region', animation_frame = 'Month')


# Animation using scatterplot  of Estimated_Employed
px.scatter(data_frame = df, x = ' Estimated_Employed', y = 'Region', animation_frame = 'Month')


# Animation using scatterplot of Estimated_Labour_Participation_Rate (%)
px.scatter(data_frame = df, x = ' Estimated_Labour_Participation_Rate (%)', y = 'Region', animation_frame = 'Month')


# Create a line plot to visualize the trend of the Estimated unemployment rate
Average_Estimated_unemployment_rate = df[' Estimated_Unemployment_Rate (%)'].mean()


plt.figure(figsize=(6, 4))
plt.plot(df['Year'], df[' Estimated_Unemployment_Rate (%)'], marker='o', linestyle='-')
plt.axhline(Average_Estimated_unemployment_rate, color='red', linestyle='--', label='Average_Estimated_unemployment_rate')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.title('Trend of Estimated Unemployment Rate ')
plt.legend()
plt.grid(True)
plt.show()

# Print the calculated average unemployment rate
print(f'Average Unemployment Rate: {Average_Estimated_unemployment_rate:.2f}%')

# Create a line plot to visualize the trend of the Estimated employed rate
Average_Estimated_Employed = df[' Estimated_Employed'].mean()


plt.figure(figsize=(6, 4))
plt.plot(df['Year'], df[' Estimated_Employed'], marker='o', linestyle='-')
plt.axhline(Average_Estimated_Employed, color='red', linestyle='--', label='Average  Estimated_Employed rate')
plt.xlabel('Year')
plt.ylabel(' Estimated_Employed')
plt.title('Trend of  Estimated_Employed rate ')
plt.legend()
plt.grid(True)
plt.show()


print(f'Average Estimated_Employed rate: {Average_Estimated_Employed:.2f}%')

# Create a line plot to visualize the trend of the Average_ Estimated_Labour_Participation rate
Average_Estimated_Labour_Participation = df[' Estimated_Labour_Participation_Rate (%)'].mean()


plt.figure(figsize=(6, 4))
plt.plot(df['Year'], df[' Estimated_Labour_Participation_Rate (%)'], marker='o', linestyle='-')
plt.axhline(Average_Estimated_Labour_Participation, color='red', linestyle='--', label='Average Estimated_Labour_Participation_Rate')
plt.xlabel('Year')
plt.ylabel(' Estimated_Labour_Participation_Rate (%)')
plt.title('Trend of  Estimated_Labour_Participation_Rate (%)')
plt.legend()
plt.grid(True)
plt.show()


print(f'Average  Estimated_Labour_Participation_Rate: {Average_Estimated_Labour_Participation:.2f}%')

