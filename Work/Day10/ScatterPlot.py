import plotly.express as px
data = {
    'Hours' : [1,2,3,4,5,6,7,8] ,
    'Scores' : [50,55 , 60 ,65 , 70 , 75 , 80  , 85]

}

fig = px.scatter(data ,
                 x = 'Hours' ,
                 y = 'Scores' ,
                 title = 'Relationship between Marks and Hours')

fig.show()