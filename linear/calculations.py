import math
import numpy as np


def calc_delta(x):
    """Compute delta over numpy array.

    Args:
        x (numpy array): independent variable

    Returns:
        delta
    """
    N = len(x)
    delta = N * np.sum(np.square(x)) - np.sum(x) * np.sum(x)
    return delta


def calc_slope(x, y, delta):
    """Compute slope for linear fit.

    Args:
        x (numpy array): independent variable
        y (numpy array): dependent variable
        delta: computed value of delta

    Returns:
        m: slope of linear fit
    """
    N = len(x)
    num = N * np.sum(np.multiply(x, y)) - np.multiply(np.sum(x), np.sum(y))
    m = num / delta
    return m


def calc_yint(x, y, m):
    """Compute y-intercept for linear fit.

    Args:
        x (numpy array): independent variable
        y (numpy array): dependent variable
        m: slope of linear fit

    Retuns:
        b: y-interecept of linear fit
    """
    N = len(x)
    b = (np.sum(y) - m * np.sum(x)) / N
    return b


def calc_stddev(x, y, m, b, delta):
    """Compute standard deviation of linear fit"""
    N = len(x)
    # print(y)
    # print(y - (b + np.multiply(m, x)))
    variance_squared = np.sum(np.square(y - (b + np.multiply(m, x)))) / (N - 2)

    stddev_m_squared = N * variance_squared / delta
    stddev_m = math.sqrt(stddev_m_squared)

    stddev_b_squared = (variance_squared * np.sum(np.square(x))) / delta
    stddev_b = math.sqrt(stddev_b_squared)

    return stddev_m, stddev_b, variance_squared


def calc_r_squared(y, variance_squared):
    """Compute coefficients of determination R squared"""
    # print(variance_squared)
    N = len(y)
    num = (N - 2) * variance_squared
    # print(num)
    print(y)
    y_sum = np.sum(y)
    print(np.subtract(y, y_sum / N))
    denom = np.sum(np.square(np.subtract(y, y_sum / N)))
    # print(denom)
    r_squared = 1 - num / denom
    return r_squared


def calc_chi_squared(x, y_d, y, m, b):
    """Compute chi squared value"""
    chi_squared = np.sum(np.divide(np.square(np.subtract(y, np.multiply(x, m) + b)), np.square(y_d)))
    return chi_squared


def calc_reduced_chi_squared(chi_squared, x):
    degrees = len(x) - 2
    reduced_chi_squared = chi_squared / degrees
    return reduced_chi_squared
