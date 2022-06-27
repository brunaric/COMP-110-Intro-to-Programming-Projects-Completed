"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union


__author__ = "730466477"


class Simpy:
    """Defining the Simpy Class."""
    values: list[float]

    # TODO: Your constructor and methods will go here.

    def __init__(self, values: list[float]): 
        """Constructer definition; initlializes  the `values` attribute of the newly constructed `Simpy` object to the argument passed in."""
        self.values = values
    
    def __str__(self) -> str:
        """Produces a str representation of a Point for humans."""
        return f"({self.values}"
    
    def fill(self, fillers: float, number: int) -> None:
        """Fills Simpy's values with a number of repeating values."""
        i: int = 0
        result = []
        while i < number:
            result.append(fillers)
            i += 1
        self.values = result
     
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in Simpy's values given a certain range.""" 
        assert step != 0
        self.values = []
        if step > 0:
            while start < stop:
                self.values.append(start)
                start += step
        else: 
            while start > stop:
                self.values.append(start)
                start += step

    def sum(self) -> float:
        """Returns the sum of all items in values."""
        i: float = 0.0
        for item in self.values:
            i += item
        return i

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overloading with the addition operator."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item + rhs)
            return Simpy(result)
        else: 
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] + rhs.values[i])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Operator overloading with the power operator: exponentiates the correspoding items in a list."""
        if isinstance(rhs, float):
            result: list[float] = []
            for item in self.values:
                result.append(item ** rhs)
            return Simpy(result)
        else: 
            result: list[float] = []
            for i in range(0, len(self.values)):
                result.append(self.values[i] ** rhs.values[i])
            return Simpy(result)

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Opperator overloading with equal operator: returns list of bools telling whether each item in a list given is equal to what it is being compared to."""
        if isinstance(rhs, float):
            result: list[bool] = []
            for item in self.values:
                if item == rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        if isinstance(rhs, Simpy):
            result: list[bool] = []
            for item in range(0, len(self.values)):
                if self.values[item] == rhs.values[item]:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a list of bools telling whether something is greater than what it is compared to."""
        if isinstance(rhs, float):
            result: list[bool] = []
            for item in self.values:
                if item > rhs:
                    result.append(True)
                else:
                    result.append(False)
            return result
        if isinstance(rhs, Simpy):
            result: list[bool] = []
            for item in range(0, len(self.values)):
                if self.values[item] > rhs.values[item]:
                    result.append(True)
                else:
                    result.append(False)
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Returns value of Simpy at given index."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
            return result
