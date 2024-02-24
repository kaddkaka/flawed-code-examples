""" This file shows example error for different python tools (linters, etc)
The intention is for developers to use this file to test their editor and make
sure expected errors are shown.

Tools mentioned:
    pycodestyle
    mypy
    pylint
    pyflakes
    mccabe
"""

# pylint: disable=line-too-long



NUMBER = 100
# ^ Expected:
# pycodestyle: E303 too many blank lines (3) [E303]


def function(n: int) -> float:
    # ^ Expected
    # pylint : [missing-function-docstring] Missing function or method docstring [C0116]
    # pylint : [invalid-name] Argument name "n" doesn't conform to snake_case naming style [C0103]
    # pylint : [unused-argument] Unused argument 'n' [W0613]
    return f"banana"
    # ^ Expected
    # mypy : Incompatible return value type (got "str", expected "float") [return-value]
    # pylint : [f-string-without-interpolation] Using an f-string that does not have any interpolated variables [W1309]
    # pyflakes : f-string is missing placeholders


def complex_function():
    # ^ Expected
    # 1. pylint : [missing-function-docstring] Missing function or method docstring [C0116]
    # 2. pylint : [too-many-branches] Too many branches (15/12) [R0912]
    # 3. mccabe: Cyclomatic complexity too high: 16 (threshold 15)
    for _ in range(10):
        # ^ Expected
        # pylint : [too-many-nested-blocks] Too many nested blocks (15/5) [R1702]
        for _ in range(10):
            for _ in range(10):
                for _ in range(10):
                    for _ in range(10):
                        for _ in range(10):
                            for _ in range(10):
                                for _ in range(10):
                                    for _ in range(10):
                                        for _ in range(10):
                                            for _ in range(10):
                                                for _ in range(10):
                                                    for _ in range(10):
                                                        for _ in range(10):
                                                            for _ in range(10):
                                                                return
