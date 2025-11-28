# ЗАДАНИЕ №5

Написать алгоритм, позволяющий определить параметры PDF с помощью метода наименьших квадратов. Продемонстрировать работу алгоритма на любом выбранном признаке из своего датасета. Сравнить качество аппроксимации c методом максимального правдоподобия посредством MSE.

# РЕШЕНИЕ

```
scipy.optimize.
minimize

minimize(fun, x0, args=(), method=None, jac=None, hess=None, hessp=None,
bounds=None, constraints=(), tol=None, callback=None, options=None)[source]

*   x0(shape(n), ndarray): First intuition. an array of real objects, where n is
    the total number of independent variables, and the size of the array is (n,).
*   args(tuple): Additional arguments supplied to the derivatives of the
    objective function.
*   bounds(bounds or sequence): For the L-BFGS-B, Nelder-Mead, TNC, Powell,
    SLSQP, and trust-constr techniques, bounds on the variables. The boundaries  
    can be specified in one of two ways: Instance of the class Bounds and for  
    each element in x, a list of (min, max) pairs is given. To specify no bound,  
    use the word none.
```

```
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import norm
from scipy.optimize import minimize

# Эмпирическая гистограмма данных
hist_values, bin_edges = np.histogram(CO2['CO2 Emissions(g/km)'], bins='sturges', density=True)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Метод наименьших квадратов (LSQ)
def mse_lsq(params):
    mu, sigma = params
    pdf_values = norm.pdf(bin_centers, loc=mu, scale=sigma)
    return np.mean((hist_values - pdf_values) ** 2)

# Начальные приближения для параметров
initial_params = [CO2['CO2 Emissions(g/km)'].mean(), CO2['CO2 Emissions(g/km)'].std()]

# Оптимизация с помощью метода наименьших квадратов
lsq_result = minimize(mse_lsq, initial_params, bounds=[(None, None), (1e-3, None)])
mu_lsq, sigma_lsq = lsq_result.x

# Метод максимального правдоподобия (MLE)
mle_params = norm.fit(CO2['CO2 Emissions(g/km)'])
mu_mle, sigma_mle = mle_params

# Теоретические плотности распределения
x = np.linspace(CO2['CO2 Emissions(g/km)'].min(), CO2['CO2 Emissions(g/km)'].max(), 1000)
pdf_lsq = norm.pdf(x, loc=mu_lsq, scale=sigma_lsq)
pdf_mle = norm.pdf(x, loc=mu_mle, scale=sigma_mle)

# Вычисление MSE для двух методов
mse_lsq_value = mse_lsq([mu_lsq, sigma_lsq])
mse_mle_value = np.mean((hist_values - norm.pdf(bin_centers, loc=mu_mle, scale=sigma_mle)) ** 2)

print(f"LSQ параметры: mu = {mu_lsq:.3f}, sigma = {sigma_lsq:.3f}, MSE = {mse_lsq_value:.5f}")
print(f"MLE параметры: mu = {mu_mle:.3f}, sigma = {sigma_mle:.3f}, MSE = {mse_mle_value:.5f}")

# Построение графиков
fig = go.Figure()
fig.add_trace(go.Histogram(x=CO2['CO2 Emissions(g/km)'], nbinsx=50, histnorm='probability density', opacity=0.5, name='Эмпирическая гистограмма'))
fig.add_trace(go.Scatter(x=x, y=pdf_lsq, mode='lines', name=f'LSQ PDF (MSE = {mse_lsq_value:.5f})', line=dict(width=2)))
fig.add_trace(go.Scatter(x=x, y=pdf_mle, mode='lines', name=f'MLE PDF (MSE = {mse_mle_value:.5f})', line=dict(width=2)))
fig.update_layout(title='Аппроксимация распределения: LSQ vs MLE', xaxis_title='CO2 Emissions(g/km)', yaxis_title='Density')
fig.show()
```

`LSQ параметры: mu = 250.585, sigma = 58.513, MSE = 0.00000`

`MLE параметры: mu = 250.585, sigma = 58.509, MSE = 0.00000`

<img width="1379" height="469" alt="image" src="https://github.com/user-attachments/assets/45eb574f-4bc2-41a5-8af8-1e1a89798bcb" />
