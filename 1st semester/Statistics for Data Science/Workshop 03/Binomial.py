import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from Poisson import Poisson
from Normal import Normal


def C(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


class Binomial:
    @staticmethod
    def P(x, n, p):
        if x > 0 and x <= n:
            return C(n, x) * (p**x) * ((1 - p) ** (n - x))
        else:
            return 0

    @staticmethod
    def sample(p):
        s_50 = np.array([Binomial.P(i, 50, p) for i in range(51)])
        s_100 = np.array([Binomial.P(i, 100, p) for i in range(101)])
        s_1000 = np.array([Binomial.P(i, 1000, p) for i in range(1001)])
        return s_50, s_100, s_1000

    @staticmethod
    def poisson_approximation(p):
        if 50 * p >= 5:
            ld = 50 * p
            return ld
        else:
            raise ValueError("Approximation not possible.")

    @staticmethod
    def gaussian_approximation(p):
        if p * 50 >= 5 and (1 - p) * 50 >= 5:
            mean = 50 * p
            std = np.sqrt(50 * p * (1 - p))
            return mean, std
        else:
            raise ValueError("Approximation not possible.")

    @staticmethod
    def superimpose_kde_plots(p):
        gaussian_mean, gaussian_std = Binomial.gaussian_approximation(p)
        poisson_ld = Binomial.poisson_approximation(p)
        n_sample = Normal.sample(gaussian_mean, gaussian_std)
        p_sample = Poisson.sample(poisson_ld)
        b_sample = Binomial.sample(p)

        fig, ax = plt.subplots(1, 3)
        fig.set_size_inches(15, 5)

        ax[0].set_title("sample size = 50")
        ax[1].set_title("sample size = 100")
        ax[2].set_title("sample size = 1000")
        sns.kdeplot(b_sample[0], label="Original Distribution", ax=ax[0])
        sns.kdeplot(n_sample[0], label="Gaussian Approximation", ax=ax[0])
        sns.kdeplot(p_sample[0], label="Poisson Approximation", ax=ax[0])
        sns.kdeplot(b_sample[1], label="Original Distribution", ax=ax[1])
        sns.kdeplot(n_sample[1], label="Gaussian Approximation", ax=ax[1])
        sns.kdeplot(p_sample[1], label="Poisson Approximation", ax=ax[1])
        sns.kdeplot(b_sample[2], label="Original Distribution", ax=ax[2])
        sns.kdeplot(n_sample[2], label="Gaussian Approximation", ax=ax[2])
        sns.kdeplot(p_sample[2], label="Poisson Approximation", ax=ax[2])

        plt.legend()
        plt.show()

    @staticmethod
    def hist_bar_kdeplot(p):
        fig, ax = plt.subplots(3, 3)
        fig.set_size_inches(15, 10)
        sample = Binomial.sample(p)

        ax[0, 0].set_title("sample size = 50")
        ax[0, 1].set_title("sample size = 100")
        ax[0, 2].set_title("sample size = 1000")
        ax[0, 0].hist(sample[0], bins=20, edgecolor="black")
        ax[0, 1].hist(sample[1], bins=20, edgecolor="black")
        ax[0, 2].hist(sample[2], bins=20, edgecolor="black")
        ax[1, 0].bar(np.arange(51), sample[0])
        ax[1, 1].bar(np.arange(101), sample[1])
        ax[1, 2].bar(np.arange(1001), sample[2])
        sns.kdeplot(sample[0], ax=ax[2, 0])
        sns.kdeplot(sample[1], ax=ax[2, 1])
        sns.kdeplot(sample[2], ax=ax[2, 2])

        plt.show()
