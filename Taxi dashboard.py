import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd


    return (pd,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(pd):
    df = pd.read_csv('taxi.csv',
                    parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'])
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(mo):
    min_distance = mo.ui.slider(0, 200)
    min_distance
    return (min_distance,)


@app.cell
def _(df, min_distance):
    (
        df
        .loc[lambda df_: df_['trip_distance'] > min_distance.value]
        .plot.scatter(x='trip_distance', y='total_amount')
    )
    return


app._unparsable_cell(
    r"""
    pd.read_csv(
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
