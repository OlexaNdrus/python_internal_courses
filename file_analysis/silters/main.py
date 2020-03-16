import sys
from abc import ABC, abstractmethod


class Option(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        print (__class__.__name__)


    @abstractmethod
    def matches(self, line: str, rule) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""

        return True


class Filter(Option):

    def __init__(self, line, rule):
        self.line = line
        self.rule = rule

    def display(self) -> str:
        """Provides a name of the rule (like FP005)."""
        if self.matches(self.line, self.rule):
            return self.line


class Annotate(Option):

    def __init__(self, line, rule):
        self.line = line
        self.applied_rules = list()

    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    def apply(self, rule) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        if self.matches(self.line, rule)
            self.applied_rules.append(rule)

class Display_rules:
    

