import abc
from typing import Dict


class SeleniumInteraction(metaclass=abc.ABCMeta):
    """this class shoould be called by initiate method. The only problem is we have a problem declaring
    abstract private methods. It's also reponsible for return the freight information or return 0 if the
    things don't occur well"""

    def __init__(self, browser):
        self.browser = browser

    @abc.abstractmethod
    def initiate(self, *args) -> Dict:
        """Must be used to call all another methods

        Returns:
        """
        ...
