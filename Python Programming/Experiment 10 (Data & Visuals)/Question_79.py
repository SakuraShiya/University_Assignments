# Write a Python Program To Demonstrate Different Visual Forms Using Matplotlib.

from matplotlib.axes import Axes
from matplotlib.pyplot import show, subplots
from numpy.random import Generator, default_rng

RANDOM_SEED: int = 42

def draw_line_chart(axis: Axes) -> None:
    """ Draw a Line Chart Showing Growth Over Time """
    axis.plot([1, 2, 3, 4, 5, 6], [2, 5, 4, 8, 7, 12], color="blue", marker="o", linestyle="-", linewidth=2)
    axis.set_title("1. Line Chart")
    axis.set_xlabel("Time")
    axis.set_ylabel("Growth")
    axis.grid(True, linestyle="--", alpha=0.6)

def draw_bar_chart(axis: Axes) -> None:
    """ Draw a Bar Chart Comparing Values Across Categories """
    axis.bar(["A", "B", "C", "D", "E"], [23, 45, 12, 56, 32], color=["red", "green", "blue", "orange", "purple"])
    axis.set_title("2. Bar Chart")
    axis.set_xlabel("Categories")
    axis.set_ylabel("Values")

def draw_scatter_plot(axis: Axes, rng: Generator) -> None:
    """ Draw a Scatter Plot Of Two Related Random Variables """
    x_values = rng.random(50) * 10
    y_values = x_values + rng.standard_normal(50) * 2
    axis.scatter(x_values, y_values, color="darkred", alpha=0.7)
    axis.set_title("3. Scatter Plot")
    axis.set_xlabel("Variable X")
    axis.set_ylabel("Variable Y")

def draw_histogram(axis: Axes, rng: Generator) -> None:
    """ Draw a Histogram Showing How 1000 Normally Distributed Values Are Spread """
    axis.hist(rng.standard_normal(1000), bins=20, color="teal", edgecolor="black")
    axis.set_title("4. Histogram")
    axis.set_xlabel("Data Range")
    axis.set_ylabel("Frequency")

def draw_pie_chart(axis: Axes) -> None:
    """ Draw a Pie Chart Of Programming Language Shares With The Largest Slice Pulled Out """
    axis.pie(
        [40, 25, 15, 20],
        explode=(0.1, 0, 0, 0),
        labels=["Python", "Java", "C++", "JavaScript"],
        colors=["gold", "lightblue", "lightcoral", "lightgreen"],
        autopct="%1.1f%%",
        shadow=True,
        startangle=90,
    )
    axis.set_title("5. Pie Chart")

def draw_box_plot(axis: Axes, rng: Generator) -> None:
    """ Draw Coloured Box Plots Comparing The Spread Of Three Random Groups """
    groups = [rng.normal(100, 10, 200), rng.normal(90, 20, 200), rng.normal(80, 30, 200)]
    box_plot = axis.boxplot(groups, patch_artist=True, notch=True, tick_labels=["G1", "G2", "G3"])

    for box, color in zip(box_plot["boxes"], ["lightblue", "lightgreen", "pink"]):
        box.set_facecolor(color)

    for median in box_plot["medians"]:
        median.set(color="red", linewidth=2)

    for flier in box_plot["fliers"]:
        flier.set(marker="o", markerfacecolor="purple", markeredgecolor="purple", alpha=0.5)

    axis.set_title("6. Box Plot")
    axis.set_xlabel("Groups")
    axis.set_ylabel("Values")
    axis.yaxis.grid(True, linestyle="--", alpha=0.7)

def main() -> None:
    rng = default_rng(RANDOM_SEED)

    figure, axes = subplots(2, 3, figsize=(15, 10))
    figure.suptitle("Matplotlib Visual Forms Demonstration", fontsize=18, fontweight="bold")
    figure.subplots_adjust(hspace=0.4, wspace=0.3)

    draw_line_chart(axes[0, 0])
    draw_bar_chart(axes[0, 1])
    draw_scatter_plot(axes[0, 2], rng)
    draw_histogram(axes[1, 0], rng)
    draw_pie_chart(axes[1, 1])
    draw_box_plot(axes[1, 2], rng)

    show()

if __name__ == "__main__":
    main()
