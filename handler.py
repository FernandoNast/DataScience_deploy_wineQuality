import pandas as pd
import pickle
import os

from flask import Flask, request
from wine_quality.WineQuality import WineQuality

# deixando modelo carregado
model = pickle.load(open('model/model_wine_quality.pkl','rb'))

app = Flask( __name__ )

@app.route('/predict',methods=['POST'])
def predict():
    test_json = request.get_json()

    # coletando os dados
    if test_json:
        if isinstance(test_json, dict): # se for vdd, unique value (apenas uma linha)
            df_raw = pd.DataFrame(test_json, index = [0])
        else:
            df_raw = pd.DataFrame(test_json, columns = test_json[0].keys())

    # intanciando data preparation (onde entra a classe WineQulity)
    pipeline = WineQuality()
    
    # data preparation
    df1 = pipeline.data_preparation(df_raw)
    

    # prediction
    pred = model.predict(df1)

    df1['prediction'] = pred

    return df1.to_json(orient = 'records')

# iniciando flask
if __name__=='__main__':
    port = os.environ.get( 'PORT', 5000)
    app.run(host='0.0.0.0', port=port)
