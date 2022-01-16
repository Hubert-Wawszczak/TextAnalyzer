import matplotlib
from matplotlib import pylab as plt
from text_analyze import *
matplotlib.use('TkAgg')


class Plot:
    def __init__(self):
        self.textanalyzeObj = TextAnalyzer()

    def plot_countEachWord(self, filename):
        plt.rcParams["figure.figsize"] = [350, 10]
        plt.rcParams["figure.autolayout"] = True
        plt.xticks(
            rotation=90,
            horizontalalignment='right',
            fontweight='light',
            fontsize=7
        )

        words = self.textanalyzeObj.countEachWord(filename)
        plt.bar(words.keys(), words.values())
        plt.show()

    def plot_countVowels(self, filename):
        plt.rcParams["figure.figsize"] = [350, 10]
        plt.rcParams["figure.autolayout"] = True
        plt.xticks(
            rotation=90,
            horizontalalignment='right',
            fontweight='light',
            fontsize=7
        )

        words = self.textanalyzeObj.countVowels(filename)
        plt.bar(words.keys(), words.values())
        plt.show()

    def plot_countConsonants(self, filename):
        plt.rcParams["figure.figsize"] = [350, 10]
        plt.rcParams["figure.autolayout"] = True
        plt.xticks(
            rotation=90,
            horizontalalignment='right',
            fontweight='light',
            fontsize=7
        )

        words = self.textanalyzeObj.countConsonants(filename)
        plt.bar(words.keys(), words.values())
        plt.show()
