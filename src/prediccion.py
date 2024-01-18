import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def ajustar_modelo_arima(serie_temporal, orden):
    modelo_arima = ARIMA(serie_temporal, order=orden)
    resultados_arima = modelo_arima.fit()
    return resultados_arima

def hacer_predicciones_arima(resultados_arima, dias_futuros):
    predicciones_arima = resultados_arima.get_forecast(steps=dias_futuros)
    predicciones_arima_ci = predicciones_arima.conf_int()
    return predicciones_arima, predicciones_arima_ci
