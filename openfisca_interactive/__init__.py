import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import List


class BarType(Enum):
    VALUE = 1
    SUB_TOTAL = 2
    TOTAL = 3


@dataclass
class Bar:
    variable_name: str
    type: BarType
    short_name: str = None
    value: float = None


def get_bars(decomposition: dict) -> List[Bar]:
    def visit(node):
        children = node.get("children")
        if children:
            for child in children:
                yield from visit(child)
            type_ = BarType.TOTAL if node["variable_name"] == decomposition["variable_name"] else BarType.SUB_TOTAL
            yield Bar(variable_name=node["variable_name"], short_name=node.get("short_name"), type=type_)
        else:
            yield Bar(variable_name=node["variable_name"], short_name=node.get("short_name"), type=BarType.VALUE)

    return list(visit(decomposition))


def iter_displayed_bars(bars: List[Bar], results: dict, x_variable_arr: List[float], x_variable: float, include_subtotals: bool, include_zero: bool):
    for bar in bars:
        if bar.type == BarType.SUB_TOTAL and not include_subtotals:
            continue
        value = dict(zip(x_variable_arr, results[bar.variable_name]))[x_variable]
        if include_zero or value != 0:
            yield dataclasses.replace(bar, value=value)


def calculate_bars(bars, simulation, period):
    return {
        bar.variable_name: simulation.calculate_add(bar.variable_name, period)
        for bar in bars
    }
