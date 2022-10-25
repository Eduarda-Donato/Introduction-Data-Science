from matplotlib import pyplot as plt
 

years  = [2000, 2005 , 2010, 2015, 2020, 2022]
num_murders = [300.2, 545.7, 1064.5, 2831.9, 5968.1, 10318.7]

plt.plot(years, num_murders, color = 'red', marker = 'o', linestyle = 'solid')

plt.title("Number of Murders")

plt.ylabel("Milhões")
plt.show()