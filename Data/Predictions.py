import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Cargar datos
data = pd.read_excel("sales.xlsx")

# Convertir ORDERDATE a formato de fecha
data['ORDERDATE'] = pd.to_datetime(data['ORDERDATE'])

# Extraer mes y año de la fecha
data['MONTH'] = data['ORDERDATE'].dt.month
data['YEAR'] = data['ORDERDATE'].dt.year

# Agrupar por cliente, año y mes para obtener las ventas mensuales
monthly_sales = data.groupby(['CUSTOMERNAME', 'YEAR', 'MONTH'])['QUANTITYORDERED'].sum().reset_index()

# Filtrar los datos hasta mayo de 2005
filtered_sales = monthly_sales[(monthly_sales['YEAR'] == 2005) & (monthly_sales['MONTH'] <= 5)]

# Modelo de Random Forest para predecir ventas
model = RandomForestRegressor(n_estimators=100, random_state=42)  # Ajustamos el número de estimadores

# Entrenar el modelo
model.fit(filtered_sales[['YEAR', 'MONTH']], filtered_sales['QUANTITYORDERED'])

# Predecir para los meses faltantes del 2005
future_months = pd.DataFrame({'YEAR': [2005]*7, 'MONTH': list(range(6, 13))})
predicted_sales = model.predict(future_months)

# Resultado de las predicciones
predictions = pd.DataFrame({'YEAR': future_months['YEAR'],
                            'MONTH': future_months['MONTH'],
                            'Predicted_Sales': predicted_sales})
print(predictions)