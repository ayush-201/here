import marimo

__generated_with = "0.14.17"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import marimo as mo
    # 24f1002092@ds.study.iitm.ac.in
    # Marimo notebook demonstrating reactive cells with widget dependencies and dynamic output.

    # Cell 1: Create the interactive slider widget for data size
    slider = mo.ui.slider(10, 1000, 100)  # Range: 10 to 1000, default 100

    # Cell 2: Generate dataset dependent on slider value
    import numpy as np
    import pandas as pd

    data_size = slider.value  # Access slider value in a separate cell
    x = np.linspace(0, 10, data_size)
    noise = np.random.normal(0, 5, data_size)
    y = x**2 + noise
    df = pd.DataFrame({'x': x, 'y': y})

    # Cell 3: Dynamic markdown showing summary statistics based on current slider state
    mo.md(f"""
    # Interactive Data Analysis

    Using **{slider.value}** data points.

    - Mean of x: {df['x'].mean():.2f}
    - Mean of y: {df['y'].mean():.2f}
    - Standard deviation of y: {df['y'].std():.2f}

    Adjust the slider to change the number of data points and see updated statistics and plots below.
    """)

    # Cell 4: Plot scatterplot showing relationship between x and y
    import matplotlib.pyplot as plt

    plt.figure(figsize=(8, 4))
    plt.scatter(df['x'], df['y'], alpha=0.6)
    plt.title('Scatterplot of x vs y (y = x^2 with noise)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
    return


if __name__ == "__main__":
    app.run()
