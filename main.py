import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df, x="x", y="y",
                size="size", color="color",
                animation_frame="animation_frame",
                color_continuous_scale="magenta",
                template="plotly_dark")

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()