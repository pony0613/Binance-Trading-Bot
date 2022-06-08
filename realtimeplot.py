from cProfile import label
import pandas as pd 
from sqlalchemy import create_engine
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
engine = create_engine("sqlite:///LivePrice.db")

df = pd.read_sql('BTCUSDT', engine)

mpl.use('TkAgg') 
def animate(i):
    data = pd.read_sql('BTCUSDT', engine)
    plt.cla()
    plt.plot(data.timestamp, data.price, color='g')
    plt.axhline(y=data.price.mean(), color='r')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('BTCUSDT')
    plt.gcf().autofmt_xdate()
    plt.tight_layout()

ani = animation.FuncAnimation(plt.gcf(), animate, 100)

plt.title('BTCUSDT')
plt.tight_layout()
plt.show()