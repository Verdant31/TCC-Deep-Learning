import yfinance as yf
import pandas as pd
from datetime import datetime

def save_action_to_csv(action):
  ticker = yf.Ticker(action)
  data = ticker.history(period="3mo")
  data = data.reset_index()[['Close', 'Date']]
  data.to_csv("data.csv")

  columns=[
    "Date",
    "Past_1_Days_Close", "Past_2_Days_Close", "Past_3_Days_Close", "Past_4_Days_Close", 
    "Past_5_Days_Close", "Past_6_Days_Close", "Past_7_Days_Close", "Past_8_Days_Close", 
    "Past_9_Days_Close","Past_10_Days_Close","Past_11_Days_Close","Past_12_Days_Close",
    "Past_13_Days_Close","Past_14_Days_Close","Past_15_Days_Close"
  ]

  new_rows = []

  for index, row in data[14:].iterrows():
    past_15_values = []
    date = str(row['Date']).split(" ")[0]
    past_15_values.append(date)
    for past_day in range(15):
      past_15_values.append(round(data.iloc[abs(past_day-index)]['Close'], 4))
    new_rows.append(past_15_values)

  df = pd.DataFrame(new_rows, columns=columns)
  df.to_csv("./backtest/" + action + ".csv", index=False)

actions = ["BBAS3.SA", "CSNA3.SA", "PETR4.SA", "VALE3.SA"]

for action in actions:
  save_action_to_csv(action)