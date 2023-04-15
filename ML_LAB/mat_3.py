import matplotlib.pyplot as plt
x=['2015','2016','2017','2018','2019','2020','2021','2022']
y=[9,10,10.5,8.9,12.75,7.51,6.45,11.12]
plt.scatter(x,y,color='green',label='Profit of the company')
plt.title('Company sales')
plt.xlabel('Years')
plt.ylabel('Profit in lakhs')
plt.legend()
plt.show()
