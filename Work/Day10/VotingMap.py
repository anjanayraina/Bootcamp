import plotly.express as px

data  = {'Country' : ['USA' , 'Canada' , 'Mexico' , 'Brazil' , 'Argentina' , 'India'] ,
         'Votes' : [60 , 30, 12 , 56 , 45 , 120]
         }

fig = px.choropleth(
    locations = data['Country']
    , locationmode='country names'
    , color = data['Votes']
   , color_continuous_scale= 'Blues'
    , labels = {'color' : 'Votes'}
    , title = 'Election Results by Country'
)

fig.show()