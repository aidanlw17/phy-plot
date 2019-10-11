import os
import csv

from linear import calculations, scatter

import numpy as np


def fit_linear(x, x_d, y, y_d):
    x = np.array(x)
    x_d = np.array(x_d)
    y = np.array(y)
    y_d = np.array(y_d)

    delta = calculations.calc_delta(x)
    m = calculations.calc_slope(x, y, delta)
    b = calculations.calc_yint(x, y, m)
    stddev_m, stddev_b, variance_sq = calculations.calc_stddev(x, y, m, b, delta)
    r_squared = calculations.calc_r_squared(y, variance_sq)

    y_fit = np.multiply(m, x) + b
    y_fit_max = np.multiply(m + stddev_m, x) + b
    y_fit_min = np.multiply(m - stddev_m, x) + b

    fit = {"r_squared": r_squared,
           "y_fit": y_fit,
           "y_max": y_fit_max,
           "y_fit_min": y_fit_min}

    scatter.scatter(x, x_d, y, y_d, y_fit)
    return fit


def load_data_from_csv(name, path):
    full_path = os.path.join(path, name)
    with open(full_path, mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        x = []
        x_d = []
        y = []
        y_d = []
        for row in csv_reader:
            x.append(row[0])
            x_d.append(row[1])
            y.append(row[2])
            y_d.append(row[3])

        x = np.array(x)
        x_d = np.array(x_d)
        y = np.array(y)
        y_d = np.array(y_d)
        return x.astype(np.float), x_d.astype(np.float), y.astype(np.float), y_d.astype(np.float)
