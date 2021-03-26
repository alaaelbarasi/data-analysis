import pandas as pd 
from matplotlib import pyplot as plt 
countries=pd.read_csv('countries.csv')
libya=countries[countries.country=='Libya']
mongolia= countries[countries.country=='Mongolia']
plt.plot(libya.population/10**6,libya.year)
plt.plot(mongolia.population/10**6,mongolia.year)
plt.title('Libya Vs mongolia')
plt.xlabel('Population')
plt.ylabel('Year')
plt.legend(['Libya','mongolia'])
plt.show()
