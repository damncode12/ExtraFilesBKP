import matplotlib.pyplot as plt
cgpa1=[9.2,6.2,8.6,8.2,6.7,5.4,6,8]
cgpa2=[7,7.7,6.7,9,8,5.6,8,6] 
cgpa3=[7.2,6.7,7.7,7,6,6.6,7,5.4]
cgpa4=[7.6,8.8,8.7,9,8,7.6,9,9.4] 
sem=[1,2,3,4,5,6,7,8]

plt.plot(sem,cgpa1)
plt.scatter(sem,cgpa2)
plt.ylim(0,10)
plt.show()


