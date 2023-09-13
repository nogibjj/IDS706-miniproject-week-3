"""
Top level script.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from lib.data_loader import master


if __name__ == "__main__":
    df = master()

    # data cleaning
    df["year"] = pd.to_datetime(df["year"], format="%Y")
    df_grouped_by_year = (
        df.drop(columns=["country"], axis="columns").groupby("year").mean()
    )

    # plot - variation of metrics w.r.t. time
    df_grouped_by_year.plot(
        figsize=(15, 10), subplots=True, title="Time series of Metrics (1991 - 2011)"
    )
    plt.savefig("outputs/Time series of Metrics (1991 - 2011).png")

    # plot - literacy rates of bottom 10 and top 20 countries
    # separate the bottom and top 20 countries by literacy rate
    top_20_literate_countries_2011 = (
        df.groupby("country").max()["literacy_rate"].sort_values(ascending=False)[:20]
    )
    bottom_20_literate_countries_2011 = (
        df.groupby("country").max()["literacy_rate"].sort_values(ascending=True)[:20]
    )

    # Note: the last country in the bottom 20 was excluded since the Literacy Rate for it was absent

    # select color palette
    pal_top = sns.color_palette("Greens_r", len(top_20_literate_countries_2011))
    pal_bottom = sns.color_palette("Reds_r", len(bottom_20_literate_countries_2011))

    # define function to rank the percentage values
    def rankmin(x):
        _, inv, counts = np.unique(x, return_inverse=True, return_counts=True)
        csum = np.zeros_like(counts)
        csum[1:] = counts[:-1].cumsum()
        return csum[inv]

    # calculate the rank for each percentage value
    rank = rankmin(bottom_20_literate_countries_2011)

    ticks = np.arange(0, 100 + 20, 20)

    # plot
    plt.figure(figsize=(18, 8))
    sns.set_style("whitegrid")

    # =========================================plot for top 20 countries========================================================

    plt.subplot(2, 1, 1)
    splot = sns.barplot(
        x=top_20_literate_countries_2011.index,
        y=top_20_literate_countries_2011.values,
        palette=np.array(pal_top[::-1])[rank],
    )

    # annotate the bars
    for p in splot.patches:
        splot.annotate(
            format(p.get_height(), ".1f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, -9),
            textcoords="offset points",
            color="black",
            fontsize=14,
        )

    # labeling
    plt.title("Literacy Rates of top 20 Countries as of 2011", fontsize=15)
    plt.xlabel("Country", fontsize=13)
    plt.xticks(rotation=25, fontsize=12)
    plt.yticks(ticks, ticks)

    # ======================================plot for bottom 20 countries========================================================
    plt.subplot(2, 1, 2)
    splot = sns.barplot(
        x=bottom_20_literate_countries_2011.index,
        y=bottom_20_literate_countries_2011.values,
        palette=np.array(pal_bottom[::-1])[rank],
    )

    # annotate the bars
    for p in splot.patches:
        splot.annotate(
            format(p.get_height(), ".1f"),
            (p.get_x() + p.get_width() / 2.0, p.get_height()),
            ha="center",
            va="center",
            xytext=(0, -9),
            textcoords="offset points",
            color="black",
            fontsize=14,
        )

    # labeling
    plt.title("Literacy Rates of bottom 20 Countries as of 2011", fontsize=15)
    plt.xlabel("Country", fontsize=13)
    plt.xticks(rotation=20, fontsize=12)
    plt.yticks(ticks, ticks)

    plt.tight_layout()
    plt.savefig("outputs/Literacy Rates.png")

    # ======================= generate descriptive statistics table ===============================
    df[[col for col in df.columns if col != "year"]].describe().round(1).to_csv(
        "outputs/descriptive_stats.csv"
    )

    print(df[[col for col in df.columns if col != "year"]].describe().round(1))
