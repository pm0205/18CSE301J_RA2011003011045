!pip install pandas
!pip install numpy
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
data = pd.read_csv('/content/sample_data/athlete_events.csv')  
# data.head() display first 5 entry
pregions = pd.read_csv('/content/sample_data/datasets_31029_40943_noc_regions.csv')

# merging to data and regions frame
merged = pd.merge(data, regions, on='NOC', how='left')

#creating goldmedal dataframes
goldMedals = merged[(merged.Medal == 'Gold')]

plt.figure(figsize=(20, 10))
plt.title('Distribution of Gold Medals')
sns.countplot(goldMedals['Age'])
plt.show()
masterDisciplines = goldMedals['Sport'][goldMedals['Age'] > 50]
plt.figure(figsize=(20, 10))
plt.tight_layout()
sns.countplot(masterDisciplines)
plt.title('Gold Medals for Athletes Over 50')
plt.show()
womenInOlympics = merged[(merged.Sex == 'F') &
                         (merged.Season == 'Summer')]
print(womenInOlympics.head(10))
 
sns.set(style="darkgrid")
plt.figure(figsize=(20, 10))
sns.countplot(x='Year', data=womenInOlympics)
plt.title('Women medals per edition of the Games')
plt.show()
