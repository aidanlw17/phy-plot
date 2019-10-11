import os
from linear import main, scatter, calculations
from scipy import stats
import numpy as np

x, x_d, y, y_d = main.load_data_from_csv('option_1.csv', os.path.join(os.getcwd(), 'data'))
# main.fit_linear(x, x_d, y, y_d)
m, b, r_value, p_value, stderr = stats.linregress(x, y)

delta = calculations.calc_delta(x)
stddev_m, stddev_b, variance_sq = calculations.calc_stddev(x, y, m, b, delta)
chi_squared = calculations.calc_chi_squared(x, y_d, y, m, b)
reduced_chi_squared = calculations.calc_reduced_chi_squared(chi_squared, x)
chi = stats.chisquare(y, f_exp=np.array(np.multiply(x, m) + b))
print(chi)
print("m: {}\nb: {}\nR Squared: {}\nError in m: {}\nError in b: {}\nChi squared: {}\nReduced chi squared: {}".format(m, b, r_value**2, stderr, stddev_b, chi_squared, reduced_chi_squared))
scatter.scatter(x, x_d, y, y_d, m, b, r_value, stderr, stddev_b, chi_squared, reduced_chi_squared)
