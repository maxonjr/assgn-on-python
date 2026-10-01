import altair as alt
import pandas as pd

df = pd.DataFrame({'x':[1,2,3,4], 'y':[10,20,25,30]})
alt.Chart(df).mark_line().encode(x='x',y='y')
