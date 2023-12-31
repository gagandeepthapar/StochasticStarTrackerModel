"""
enums

File to contain all different types of enums
Includes:
    - SimType
    - PlotterType

startrackermodel
"""

import logging
import logging.config
from enum import Enum

from data import CONSTANTS

logging.config.dictConfig(CONSTANTS.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


class SimType(Enum):
    """
    Enum to differentiate between Monte Carlo and Sensitivity Analysis
    """

    MONTE_CARLO = 1
    SENSITIVITY = 2


class PlotterType(Enum):
    """
    Enum to differentiate plotting styles
    """

    SIMPLE = 1
    VERBOSE = 2


class ComponentType(Enum):
    """
    Enum to differentiate component types
    """

    HARDWARE = 1
    SOFTWARE = 2
    SENSOR = 3
    ENVIRONMENT = 4


class DataType(Enum):
    """
    Enum to differentiate between scrambled, spanned, or ideal data
    """

    SCRAMBLED = 1
    SPANNED = 2
    IDEAL = 3
