import plotly.express as px
from matplotlib.pyplot import xlabel, title

data = {'Month' : ['Jan' , 'Feb' , 'Mar' , 'Apr' , 'May']
        ,
        'Product A' : [10 , 12, 5 , 14 , 7] ,
         'Product B' : [9 , 5, 10, 18 , 6]}

fig = px.line(data ,
              x = 'Month' ,
              y = ['Product A' , 'Product B'] ,
              title = 'Monthly Sales')
fig.update_layout(
    xaxis_title = "Monthly" ,
    yaxis_title = "Number of Sales" ,
    title_font_size = 20 ,
    xaxis = dict(showgrid = True) ,
    title = "Monthly Sales of Products "
)
fig.show()