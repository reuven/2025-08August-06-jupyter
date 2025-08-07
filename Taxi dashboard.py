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
    return


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
def _():
    return


@app.cell
def _(df):
    (
        df
        .loc[lambda df_: df_['trip_distance'] > 0]
        .plot.scatter(x='trip_distance', y='total_amount')
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
