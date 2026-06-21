import pandas as pd
import plotly.express as px

df = pd.read_csv("data/strategy_comparison.csv")

fig = px.bar(
    df,
    x="strategy",
    y="average_reward",
    text="average_reward",
    title="Rule-Based vs ML-Based vs Deep RL Reward Comparison"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside",
    marker_color=["#6366f1", "#f97316", "#22c55e"]
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white", size=14),
    height=500,
    margin=dict(l=60, r=40, t=80, b=80),
    showlegend=False
)

fig.update_xaxes(title="Strategy")
fig.update_yaxes(title="Average Reward")

fig.write_html(
    "data/strategy_comparison.html",
    include_plotlyjs="cdn"
)

print("Strategy comparison graph saved!")