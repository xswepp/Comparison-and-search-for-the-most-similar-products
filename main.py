import pandas as pd
import numpy as np
import joblib
import hnswlib
from sklearn.preprocessing import StandardScaler
from catboost import CatBoostClassifier
from flask import Flask, jsonify, request

# Загрузка моделей
scaler = StandardScaler()
scaler = joblib.load("standard_scaler.pkl")

mcbc = CatBoostClassifier()
mcbc.load_model("mcbc_model.cbm")

# Загрузка индексов
base_index = joblib.load("base_index.pkl")
idx_hnsw = hnswlib.Index(space="cosine", dim=65)
idx_hnsw.load_index("idx_hnsw.bin") # Загружаем индекс из файла
idx_hnsw.set_ef(600)

# Инициализация app
app = Flask("default")

# Настройка конечного пути прогнозирования
@app.route("/predict", methods=["POST"])
def predict():
    X = request.get_json() # Получение JSON

    # Проверка наличия необходимых признаков
    X = pd.DataFrame(X)[
    "0",  "1",  "2",  "3",  "4",  "5",  "7",  "8",  "9",  "10", "11", "12",
    "13", "14", "15", "16", "17", "18", "19", "20", "22", "23", "24", "26",
    "27", "28", "29", "30", "31", "32", "34", "35", "36", "37", "38", "39",
    "40", "41", "42", "43", "45", "46", "47", "48", "49", "50", "51", "52",
    "53", "54", "55", "56", "57", "58", "60", "61", "62", "63", "64", "66",
    "67", "68", "69", "70", "71"
    ]

    # Стандартизация данных
    X = scaler.transform(X)

    # Получение ближайших 200 векторов
    labels, distances = idx_hnsw.knn_query(X, k=200)

    # Предсказание вхождения в первую 5 предсказанных векторов
    mcbc_val = mcbc.predict(X)

    if mcbc_val == 1:
        result = {"Похожие товары": [base_index[x] for x in labels[:5]]}
    else:
        ind = 8 # Константа индекса невалидных векторов
        result = {"Похожие товары": [base_index[x] for x in labels[ind-3:ind+2]]}

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8989) # Запуск приложения на локальном хосте и порте 8989