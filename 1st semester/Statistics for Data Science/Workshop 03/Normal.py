import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class Normal:
    @staticmethod
    def P(m, std, x):
        return (1 / (std * np.sqrt(2 * np.pi))) * np.exp(
            (-((x - m) ** 2)) / (2 * std**2)
        )

    @staticmethod
    def sample(m, std):
        s_50 = np.array([Normal.P(m, std, i) for i in range(51)])
        s_100 = np.array([Normal.P(m, std, i) for i in range(101)])
        s_1000 = np.array([Normal.P(m, std, i) for i in range(1001)])
        return s_50, s_100, s_1000

    @staticmethod
    def hist_bar_kdeplot(m, std):
        fig, ax = plt.subplots(3, 3)
        fig.set_size_inches(15, 10)
        sample = Normal.sample(m, std)

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
