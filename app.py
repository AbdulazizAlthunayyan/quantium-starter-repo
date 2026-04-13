from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

daily_sales = df.groupby("date", as_index=False)["sales"].sum()
daily_sales = daily_sales.sort_values("date")

fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales"}
)

fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)