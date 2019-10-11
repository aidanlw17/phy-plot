import os

from linear import calculations
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

def scatter(x, x_d, y, y_d, m, b, r_value, stderr_m, stderr_b, chi_squared, reduced_chi_squared):
    path = os.path.join(os.getcwd(), 'plots')
    try:
        os.makedirs(path)
    except OSError as exception:
        pass

    name = 'phylab1_plot_option_1.png'
    full_path = os.path.join(path, name)

    f = plt.figure(figsize=(12, 12))
    ax = plt.subplot(aspect='equal')
    ax.errorbar(x, y, xerr=x_d, yerr=y_d, fmt='o', label="Measured Data")
    ax.plot(x, np.multiply(m, x) + b, linestyle=":", label="Fitted: y = ({} +/- {} Ohms)x + ({} +/- {} V)\nR Squared: {}\nChi Squared: {}\nReduced Chi Squared: {}".format(format(m, '.2f'), format(stderr_m, '.2f'), format(b, '.2f'), format(stderr_b, '.2f'), format(r_value**2, '.2f'), format(chi_squared, '.2f'), format(reduced_chi_squared, '.2f')))
    ax.grid('on')
    ax.axis('tight')
    ax.set_title('Current (A) Versus Voltage (V) for Circuit Option 1')
    ax.set_ylabel('Voltage (V)')
    ax.set_xlabel('Current (A)')
    plt.ylim(6.46, 6.58)

    plt.legend()

    plt.savefig(full_path)
    plt.close()

    y_res = []
    for i in range(0, 4):
        y_res.append(y[i] - (m*x[i] + b))

    name = 'phylab1_plot_option_1_residuals.png'
    full_path = os.path.join(path, name)
    f_2 = plt.figure(figsize=(12, 12))
    ax = plt.subplot(aspect='equal')
    ax.errorbar(x, y, xerr=x_d, yerr=y_d, fmt='o', label="Measured Data")
    ax.scatter(x, y_res, color="red", marker="x", label="Residuals")
    ax.plot(x, np.multiply(m, x) + b, linestyle=":", label="Fitted: y = ({} +/- {} Ohms)x + ({} +/- {} V)\nR Squared: {}".format(format(m, '.2f'), format(stderr_m, '.2f'), format(b, '.2f'), format(stderr_b, '.2f'), format(r_value**2, '.2f')))
    ax.grid('on')
    ax.axis('tight')
    ax.set_title('Current (A) Versus Voltage (V) for Circuit Option 1 Residuals')
    ax.set_ylabel('Deviation y_actual - y_expected for Voltage (V)')
    ax.set_xlabel('Current (A)')
    plt.ylim(-0.2, 7.0)
    plt.legend()

    plt.savefig(full_path)
    plt.close()
