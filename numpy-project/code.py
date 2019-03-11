# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
path
data = np.genfromtxt(path, delimiter=',', skip_header=1)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
census = np.concatenate((data,np.array(new_record)),axis=0)
#print(census)
#Code starts here



# --------------
#Code starts here
age = census[:,0]
print(age)
max_age = max(age)
min_age = min(age)
age_mean = age.mean()
age_std = age.std()


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
len_0 = len(race_0)
race_1 = census[census[:,2]==1]
len_1 = len(race_1)
race_2 = census[census[:,2]==2]
len_2 = len(race_2)
race_3 = census[census[:,2]==3]
len_3 = len(race_3)
race_4 = census[census[:,2]==4]
len_4 = len(race_4)

minority_race=3


# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
#print("No. of senior citizens",len(senior_citizens))
working_hours_sum = sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

avg_pay_high = high[:,7].mean()
avg_pay_low = low[:,7].mean()

print(avg_pay_high)
print(avg_pay_low)


