"""
Top level script.
"""
import matplotlib.pyplot as plt
import seaborn as sns
from lib.data_loader import master

if __name__ == "__main__":
    df = master()

    # Visualize using Seaborn and Matplotlib
    sns.set(style="whitegrid")

    # Scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df.to_pandas(), x="literacy_rate", y="gdp_pc")
    plt.title("Scatter Plot of Litercy vs. GDP Per Capita")
    plt.xlabel("Literacy Rate")
    plt.ylabel("GDP Per Capita")
    plt.savefig("outputs/Scatterplot.png")

    # descriptive stats
    df.describe().write_csv("outputs/descriptive_stats.csv")
