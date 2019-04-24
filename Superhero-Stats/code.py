# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
#Code starts here 
data['Gender'].replace('-','Agender',inplace = True)
#print(data[data['Gender']=='Agender'].head())

gender_count = data['Gender'].value_counts()
print(gender_count)

gender_count.plot(kind = 'bar')
plt.show()


# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
print(alignment)

plt.pie(alignment)
plt.title('Character Alignment')
#plt.legend()
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]

sc_covariance = sc_df.cov().iat[0,1].round(2)
print(sc_covariance)
sc_strength = sc_df.Strength.std().round(2)
sc_combat = sc_df.Combat.std().round(2)

sc_pearson = (sc_covariance/(sc_strength*sc_combat)).round(2)
print(sc_pearson)

ic_df = data[['Intelligence','Combat']]

ic_covariance = 853.42
#print(ic_cov)
ic_intelligence = ic_df.Intelligence.std().round(2)
ic_combat= ic_df.Combat.std().round(2)
ic_pearson = (ic_covariance/(ic_intelligence*ic_combat)).round(2)
print(ic_pearson)


# --------------
#Code starts here

total_high = data.Total.quantile(0.99)
print(total_high)

super_best = data[data['Total']>total_high]
print(super_best.head())

super_best_names = super_best['Name'].tolist()
print(super_best_names)


# --------------
#Code starts here

fig , (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3, ncols = 1)

ax_1.boxplot(data['Intelligence'])
plt.title("Intelligence")

ax_2.boxplot(data['Speed'])
plt.title("Speed")

ax_3.boxplot(data['Power'])
plt.title("Power")

plt.show()


