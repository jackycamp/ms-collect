from typing import List
import matplotlib.pyplot as plt

class Bar:
    def __init__(self, x: List[float], y: List[float]) -> None:
        """
        Constructor for the bar class. Serves as a wrapper around
        matplotlib's bar charts.

        Args:
            x (List[float]): The values to be plotted with respect to the x-axis.
            y (List[float]): The values to be plotted with respect to the y-axis.
        """
        self.x = x
        self.y = y

    def plot(self) -> None:
        """
        Renders the bar using matplotlib api.
        TODO: Pretty barebones in terms of flexibility. What else should go here? :,)
        """
        plt.figure()
        plt.bar(self.x, self.y, width=0.1, color='black')
        plt.show()
