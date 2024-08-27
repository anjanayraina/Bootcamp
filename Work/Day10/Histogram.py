import plotly.express as px
import random as rand
data = [rand.randrange(1,10 , 1) for i in range(15)]

fig = px.histogram(data ,
                   x=data,
                   title = 'Histogram Sample Data'  ,
                   labels = {'x' : 'Value' , 'y' : 'Frequency'}
                   , nbins = 10)

fig.show()