import matplotlib.pyplot as plt
import pandas as pd
def test_value_on_bar_top():
    x=['A','B','C','D']
    y=[1,2,3,4]
    #plt.barh(x,y)
    plt.bar(x,y)
    for index,value in enumerate(y):
        plt.text(index,value,str(value))
    plt.show()
test_value_on_bar_top()
                 
        
        
