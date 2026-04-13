from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    className="app-container",
    children=[
        html.H1("Soul Foods Pink Morsel Sales Visualiser", className="main-title"),

        html.Div(
            className="controls-card",
            children=[
                html.Label("Filter by Region", className="radio-label"),
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="radio-items",
                ),
            ],
        ),

        dcc.Graph(id="sales-chart", className="chart-card"),
    ],
)


@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"].str.lower() == selected_region]

    daily_sales = (
        filtered_df.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    title_text = (
        "Pink Morsel Sales Over Time - All Regions"
        if selected_region == "all"
        else f"Pink Morsel Sales Over Time - {selected_region.capitalize()}"
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=title_text,
        labels={"date": "Date", "sales": "Sales"},
    )

    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_dash="dash",
        line_color="red"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font=dict(size=14),
        title_x=0.5,
    )

    fig.update_traces(line=dict(width=3))
    fig.update_xaxes(showgrid=True, gridcolor="#e6e6e6")
    fig.update_yaxes(showgrid=True, gridcolor="#e6e6e6")

    return fig


if __name__ == "__main__":
    app.run(debug=True)