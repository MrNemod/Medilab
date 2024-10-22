import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from dataframe_builder import df

def prediccion(sintomas):
    X = df.values  # Características: los síntomas
    y = df.index  # Etiquetas: las enfermedades

    # Verificar el balance de clases (enfermedades)
    # print("Distribución de las clases en el conjunto de datos:")
    # print(df.index.value_counts())

    # Dividir los datos sin estratificación y con un conjunto de prueba más pequeño
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    # Definir el modelo RandomForest
    rf = RandomForestClassifier(n_estimators=200, random_state=42)

    # Entrenar el modelo
    rf.fit(X_train, y_train)

    # Predecir en el conjunto de prueba
    y_pred = rf.predict(X_test)

    # Evaluar la precisión
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Precisión del modelo: {accuracy * 100:.2f}%")

    # Mostrar la importancia de las características (síntomas)
    importances = rf.feature_importances_
    print("\nImportancia de las características (síntomas):")
    for i, col in enumerate(df.columns):
        print(f"{col}: {importances[i]:.4f}")

    # Datos de entrada para predicción
    sintomas_enfermedad = np.array([sintomas])

    # Realizar la predicción de la enfermedad
    prediccion_enfermedad = rf.predict(sintomas_enfermedad)
    return prediccion_enfermedad[0]
