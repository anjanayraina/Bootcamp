import plotly.express as px

data = {
    'Course' : ['Maths' , 'Chemistry' , 'Biology' , 'English'] ,
    'Marks' : [97 , 89 , 78  ,  80]
}

fig = px.pie(names = data['Course'] , values =data['Marks'] ,
             title = 'Marks Distribution' , hole = 0.5 )


fig.update_traces(
    textinfo = 'percent+label' ,
    pull = [0.04 , 0.05 , 0 ,0.05]
)
fig.show()