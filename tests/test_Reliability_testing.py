from reliability.Reliability_testing import likelihood_plot
import matplotlib.pyplot as plt

failures = [2, 9, 23, 38, 67, 2, 11, 28, 40, 76, 3, 17, 33, 45, 90,
            4, 17, 34, 55, 115, 6, 19, 34, 56, 126, 9, 21, 37, 57, 197]


def test_likelihood_plot():
    # regression test for matplotlib 3.10+ which removed
    # QuadContourSet.collections (used to compute plot limits)
    plt.ion()  # enables plt.close() to clear the plt.show() block
    likelihood_plot(distribution="Weibull", failures=failures, CI=[0.9])
    plt.close()
    likelihood_plot(distribution="Weibull", failures=failures,
                    CI=[0.9, 0.95])
    plt.close()
    plt.ioff()
