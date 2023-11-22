# import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.special import gammaln
from Normal import Normal


class Poisson:
    @staticmethod
    def P(ld, x):
        if type(x) == int and x >= 0:
            return np.exp(
                x * np.log(ld) - ld - gammaln(x + 1)
            )  # np.exp(-ld) * (ld**x / math.factorial(x))
        else:
            return 0

    @staticmethod
    def sample(ld):
        s_50 = np.array([Poisson.P(ld, i) for i in range(51)])
        s_100 = np.array([Poisson.P(ld, i) for i in range(101)])
        s_1000 = np.array([Poisson.P(ld, i) for i in range(1001)])
        return s_50, s_100, s_1000

    @staticmethod
    def gaussian_approximation(ld):
        if ld >= 10:
            gaussian_mean = ld
            gaussian_std = np.sqrt(ld)
            return gaussian_mean, gaussian_std
        else:
            raise ValueError("Approximation not possible.")

    @staticmethod
    def superimpose_kde_plots(ld):
        gaussian_mean, gaussian_std = Poisson.gaussian_approximation(ld)
        n_sample = Normal.sample(gaussian_mean, gaussian_std)
        p_sample = Poisson.sample(ld)

        fig, ax = plt.subplots(1, 3)
        fig.set_size_inches(15, 5)

        ax[0].set_title("sample size = 50")
        ax[1].set_title("sample size = 100")
        ax[2].set_title("sample size = 1000")
        sns.kdeplot(p_sample[0], label="Original Distribution", ax=ax[0])
        sns.kdeplot(n_sample[0], label="Gaussian Approximation", ax=ax[0])
        sns.kdeplot(p_sample[1], label="Original Distribution", ax=ax[1])
        sns.kdeplot(n_sample[1], label="Gaussian Approximation", ax=ax[1])
        sns.kdeplot(p_sample[2], label="Original Distribution", ax=ax[2])
        sns.kdeplot(n_sample[2], label="Gaussian Approximation", ax=ax[2])

        plt.legend()
        plt.show()

    @staticmethod
    def hist_bar_kdeplot(ld):
        fig, ax = plt.subplots(3, 3)
        fig.set_size_inches(15, 10)
        sample = Poisson.sample(ld)

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
