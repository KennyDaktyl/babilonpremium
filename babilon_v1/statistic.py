import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def numpy(dataframe):
    df = dataframe
    np.random.seed(19680801)

    # example data
    mu = 100  # mean of distribution
    sigma = 15  # standard deviation of distribution
    # x = mu + sigma * np.random.randn(437)
    x = df["type_of_order"]
    num_bins = 50

    fig, ax = plt.subplots()

    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, density=1)

    # add a 'best fit' line
    y = (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(
        -0.5 * (1 / sigma * (bins - mu)) ** 2
    )
    ax.plot(bins, y, "--")
    ax.set_xlabel("Smarts")
    ax.set_ylabel("Probability density")
    ax.set_title(r"Histogram of IQ: $\mu=100$, $\sigma=15$")

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    # plt.show()
    # print(plt)

    return plt


#############################################################################
#
# ------------
#
# References
# """"""""""
#
# The use of the following functions and methods is shown in this example:

# matplotlib.axes.Axes.hist
# matplotlib.axes.Axes.set_title
# matplotlib.axes.Axes.set_xlabel
# matplotlib.axes.Axes.set_ylabel


def py_plot_diagram():
    import numpy as np
    import matplotlib.pyplot as plt

    N = 5
    menMeans = (20, 35, 30, 35, 27)
    womenMeans = (25, 32, 34, 20, 25)
    menStd = (2, 3, 4, 1, 2)
    womenStd = (3, 5, 2, 3, 3)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans, width, yerr=menStd)
    p2 = plt.bar(ind, womenMeans, width, bottom=menMeans, yerr=womenStd)

    plt.ylabel("Scores")
    plt.title("Scores by group and gender")
    plt.xticks(ind, ("G1", "G2", "G3", "G4", "G5"))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ("Men", "Women"))
    # plt.savefig("pizzeria/static/media/foo.png")
    # plt.show()
    return plt
