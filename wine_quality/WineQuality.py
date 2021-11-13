import pickle

class WineQuality(object):
    def __init__(self): # criacao do construtor
        self.free_sulfur_dioxide_scaler = pickle.load(open('parameter/free_sulfur_dioxide_scaler.pkl','rb'))
        self.total_sulfur_dioxide_scaler = pickle.load(open('parameter/total_sulfur_dioxide_scaler.pkl','rb'))
        
    
    def data_preparation(self, df): # criacao de metodos que vao implementar os construtores
        # rescaling free
        df['free sulfur dioxide'] = self.free_sulfur_dioxide_scaler.transform(df[['free sulfur dioxide']].values)
        
        # rescaling total
        df['total sulfur dioxide'] = self.total_sulfur_dioxide_scaler.transform(df[['total sulfur dioxide']].values)
        
        return df
