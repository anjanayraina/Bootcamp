import plotly.express as px
data = {'Products' : ['electronics' , 'Furniture' , 'Clothing' , 'Food']
        ,
        'Sales' : [1500 , 2000 , 1800 , 3000]
        }

fig = px.bar(
    x = data['Products'] ,
    y = data['Sales']
     , labels  = {'x' : 'Product Cateogry' , 'y' : 'Sales($)'} ,
    title = 'Total Sales of Products'
)

fig.show()