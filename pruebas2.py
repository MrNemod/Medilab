import pandas as pd
from dataframe_builder import df  # Importar el DataFrame directamente
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Usar el DataFrame importado
data = df  # Cambia esto por tu DataFrame

# Verificar valores nulos
print("Valores nulos en cada columna:")
print(data.isnull().sum())

# Verificar la distribución de las clases
print("Distribución de clases:")
print(data['nombre_de_la_clase'].value_counts())  # Cambia 'nombre_de_la_clase' por tu columna de clases

# Preprocesamiento
# Convertir etiquetas a números
label_encoder = LabelEncoder()
data['nombre_de_la_clase'] = label_encoder.fit_transform(data['nombre_de_la_clase'])  # Cambia según tu columna

# Escalar características
X = data.drop('nombre_de_la_clase', axis=1)  # Asegúrate de usar las columnas correctas
y = data['nombre_de_la_clase']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir el conjunto de datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Modelo de árbol de decisión
print("Modelo de Árbol de Decisión:")
decision_tree_model = DecisionTreeClassifier(random_state=42)
decision_tree_model.fit(X_train, y_train)

# Hacer predicciones
y_pred_dt = decision_tree_model.predict(X_test)

# Evaluar el modelo
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f"Precisión del modelo de Árbol de Decisión: {accuracy_dt * 100:.2f}%")
print("Reporte de clasificación:")
print(classification_report(y_test, y_pred_dt))

# Modelo de Random Forest
print("Modelo de Random Forest:")
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(X_train, y_train)

# Hacer predicciones
y_pred_rf = rf_model.predict(X_test)

# Evaluar el modelo
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print(f"Precisión del modelo Random Forest: {accuracy_rf * 100:.2f}%")
print("Reporte de clasificación para Random Forest:")
print(classification_report(y_test, y_pred_rf))
