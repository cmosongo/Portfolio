import numpy as np
import pandas as pd
import datetime
import plotly.graph_objects as go

def get_lsl_and_lsh(df):
    try:
        df['LSL'] = np.nan
        df['LSH'] = np.nan
        last_type = None
        last_index = -3
        last_lsl_index = 0
        last_lsh_index = 0
        min_so_far = 10000000000000
        max_so_far = -10000000000000

        for i, row in enumerate(df.iterrows()):
            if i + 3 >= df.shape[0] or i < last_index:
                continue

            if not last_type:  # Last type is unknown
                if min_so_far == 10000000000000:
                    if not pd.isna(df['SL'][i]):
                        min_so_far = df['SL'][i]
                else:
                    if min_so_far > df.Low[i]:
                        last_lsh_value = df.iloc[last_lsl_index:i - 1, 'SH'].dropna().max()
                        last_type = 'LSH'
                        last_index = i
                        for j in range(i, -1, -1):
                            if last_lsh_value == df['High'][j] and df['SH'][j] == df['High'][j]:
                                last_lsh_index = j
                                df.at[last_lsh_index, 'LSH'] = last_lsh_value
                                min_so_far = df.loc[last_lsh_index:i, 'SL'].dropna().max()
                                max_so_far = df.loc[last_lsh_index:i, 'SH'].dropna().min()
                                break

                    if not pd.isna(df['SL'][i]):
                        min_so_far = max(df['SL'][i], min_so_far)

                if max_so_far == -10000000000000:
                    if not pd.isna(df['SH'][i]):
                        max_so_far = df['SH'][i]
                else:
                    if max_so_far < df.High[i]:  # High broken min point will be LSL
                        last_lsl_value = df.loc[last_lsh_index:i - 1, 'SL'].dropna().min()
                        last_type = 'LSL'
                        last_index = i
                        for j in range(i, -1, -1):
                            if last_lsl_value == df['Low'][j]:
                                last_lsl_index = j
                                df.at[last_lsl_index, 'LSL'] = last_lsl_value
                                max_so_far = df.loc[last_lsl_index:i - 1, 'SH'].dropna().min()
                                min_so_far = df.loc[last_lsl_index:i - 1, 'SL'].dropna().max()
                                break
                    if not pd.isna(df['SH'][i]):
                        max_so_far = min(df['SH'][i], max_so_far)

            if last_type == 'LSL':
                if not pd.isna(min_so_far) and min_so_far > df.Low[i]:
                    for j in range(i, last_lsl_index - 1, -1):
                        last_lsh_value = df.loc[last_lsl_index:i - 1, 'SH'].dropna().max()
                        last_type = 'LSH'
                        last_index = i
                        if last_lsh_value == df['High'][j] and df['SH'][j] == df['High'][j]:
                            last_lsh_index = j
                            df.at[last_lsh_index, 'LSH'] = last_lsh_value
                            min_so_far = df.loc[last_lsh_index:i, 'SL'].dropna().max()
                            max_so_far = df.loc[last_lsh_index:i, 'SH'].dropna().min()
                            break
                if not pd.isna(df['SL'][i]):
                    min_so_far = max(df['SL'][i], min_so_far)

            elif last_type == 'LSH':
                if not pd.isna(max_so_far) and max_so_far < df.High[i]:  # High broken min point will be LSL
                    last_lsl_value = df.loc[last_lsh_index:i - 1, 'SL'].dropna().min()
                    last_type = 'LSL'
                    last_index = i
                    for j in range(i, last_lsh_index - 1, -1):
                        if last_lsl_value == df['Low'][j] and df['SL'][j] == df['Low'][j]:
                            last_lsl_index = j
                            df.at[last_lsl_index, 'LSL'] = last_lsl_value
                            max_so_far = df.loc[last_lsl_index:i - 1, 'SH'].dropna().min()
                            min_so_far = df.loc[last_lsl_index:i - 1, 'SL'].dropna().max()
                            break

                if not pd.isna(df['SH'][i]):
                    max_so_far = min(df['SH'][i], max_so_far)
    except ValueError as e:
        print(f"Error {e} in {df}")
    return df

def plot_data(df):
    df['SL'] = np.nan
    df['SH'] = np.nan

    def is_swing_high(df, i):
        return df['High'][i] > df['High'][i + 1] and df['High'][i] > df['High'][i + 2] and df['High'][i] > df['High'][
            i + 3]

    def is_swing_low(df, i):
        return df['Low'][i] < df['Low'][i + 1] and df['Low'][i] < df['Low'][i + 2] and df['Low'][i] < df['Low'][i + 3]

    last_type = None
    last_index = -3
    for i, row in enumerate(df.iterrows()):

        if i + 3 >= df.shape[0] or i < last_index:
            continue

        if not last_type:  # Last type is unknown
            if is_swing_low(df, i):
                last_type = 'SL'
                last_index = i
                df.at[i, last_type] = df['Low'][i]

            if is_swing_high(df, i):
                last_type = 'SH'
                last_index = i
                df.at[i, last_type] = df['High'][i]

        elif last_type == 'SL':
            if is_swing_high(df, i):
                last_type = 'SH'
                last_index = i
                df.at[i, last_type] = df['High'][i]
                if is_swing_low(df, i):
                    last_type = 'SL'
                    last_index = i
                    df.at[i, last_type] = df['Low'][i]

        elif last_type == 'SH':
            if is_swing_low(df, i):
                last_type = 'SL'
                last_index = i
                df.at[i, last_type] = df['Low'][i]
                if is_swing_high(df, i):
                    last_type = 'SH'
                    last_index = i
                    df.at[i, last_type] = df['High'][i]

    df = get_lsl_and_lsh(df)

    return df

#get data
file = 'AUDCAD.pro_M15_201901020000_202107302345'
url = f'../data/cleaned/currency/{file}.csv'
stock = file[:6]
df = pd.read_csv(url)
df = plot_data(df[:5000])

OHLC_trace = go.Candlestick(x=df['Date'],
                                open=df['Open'], high=df['High'],
                                low=df['Low'], close=df['Close'],
                                name="OHLC Data", )

swing_low = go.Scatter(
    x=df['Date'],
    y=df['SL'] - .5,
    name='Swing Low',
    mode='text',
    textposition='bottom center',
    text="SL",
    textfont=dict(family='sans serif',
                    size=12,
                    color='aqua'
                    )
)

swing_high = go.Scatter(
    x=df['Date'],
    y=df['SH'] + .5,
    mode='text',
    name='Swing High',
    textposition='top center',
    text="SH",
    textfont=dict(family='sans serif',
                    size=12,
                    color='pink'
                    )
)

large_swing_low = go.Scatter(
    x=df['Date'],
    y=df['LSL']-min(35, df['Close'][0]*.05),
    name='Large Swing Low',
    mode='text',
    textposition='bottom center',
    text="LSL",
    textfont=dict(family='sans serif',
                    size=12,
                    color='yellow'
                    )
)

large_swing_high = go.Scatter(
    x=df['Date'],
    y=df['LSH']+ min(35, df['Close'][0]*.05),
    mode='text',
    name='Large Swing High',
    textposition='top center',
    text="LSH",
    textfont=dict(family='sans serif',
                    size=12,
                    color='yellow'
                    )
)

data = [OHLC_trace, swing_low, swing_high, large_swing_high, large_swing_low]

layout = go.Layout(
    colorway=["#5E0DAC", '#FF4F00', '#375CB1', '#FF7400', '#FFF400', '#FF0056'],
    template='plotly_dark',
    paper_bgcolor='rgba(0, 0, 0, 0)',
    plot_bgcolor='rgba(0, 0, 0, 0)',
    margin={'b': 15},
    hovermode='x',
    autosize=True,
    height=900,
    title={'text': stock + ' Prices', 'font': {'color': 'white'}, 'x': 0.5},
    xaxis={'range': [df.Date.min(), df.Date.max()], 'type': "category"},
    yaxis={'range': [df.Low.min() * .92, df.High.max() * 1.07]},
)
fig = go.Figure(data=data, layout=layout)
fig.update_layout()
fig.update_yaxes(
    scaleanchor="x",
    scaleratio=1,
)
fig.show()




