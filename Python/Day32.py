## ANOVA

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# SAmple data for three groups
group1 = [5, 6, 7, 8, 9]
group2 = [2, 4, 6, 8, 9]
group3 = [3, 6, 9, 12, 15]

#Perform one-way ANOVA
f_statistic, p_value = stats.f_oneway(group1, group2, group3)

# Print the F-Statistics and p-value
print(f"F-statistic = {f_statistic: .2f}")
print(f"P-value = {p_value: .4f}")


# Combine the data into a single list
data = [group1, group2, group3]

# Create box plot
plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['Group 1', 'Group 2', 'Group 3'])
plt.xlabel('Groups')
plt.ylabel('Values')
plt.title('Box Plot of Data')
plt.show()


## Vectors

import numpy as np
import matplotlib.pyplot as plt

# Geometric Vector Plot


