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
                    )
    return


if __name__ == "__main__":
    app.run()
