import pandas as pd
import plotly.express as px

df = pd.read_csv("data/dqn_training_rewards.csv")

fig = px.line(
    df,
    x="episode",
    y="reward",
    title="DQN Training Reward Curve"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="#020617",
    plot_bgcolor="#020617",
    font=dict(color="white"),
    height=500
)

fig.write_html("data/dqn_reward_curve.html")

print("DQN reward curve saved successfully!")