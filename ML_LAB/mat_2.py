import matplotlib.pyplot as plt
slices=[50,14,24,16]
depts=['sales','production','hr','finance']
colors=['magenta','cyan','brown','gold']
plt.pie(slices,labels=depts,colors=colors, startangle=90, explode=(0,0,0,0.2))
plt.legend(title='Department wise expenditure')
plt.show()
