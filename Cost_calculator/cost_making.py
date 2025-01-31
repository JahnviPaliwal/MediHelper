import joblib
import numpy as np

def cost_making(model_path, input_data):
    loaded_model = joblib.load(model_path)
    data = np.array(input_data).reshape(1, -1)
    predicted_cost = loaded_model.predict(data)
    print(predicted_cost[0])
    return predicted_cost[0]


