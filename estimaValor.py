from keras.models import load_model
import numpy as np 
import pandas as pd

# Valida se o valor passado como entrada é um float
def validaFloat(strvalor):

    if strvalor.replace('.','',1).isdigit():
        return True
    else:
        return False

# Valida se o valor passado como entrada é válido
def validaEntrada(msg, valor_max, valor_min = 0):
    aux = 0

    while True:
        aux = input(msg)

        if validaFloat(aux):
            if valor_min <= float(aux) and valor_max >= float(aux):
                return float(aux)
            else:
                print('\033[0;31mErro! Digite um valor válido.\033[m')
        else:
            print('\033[0;31mErro! Digite um valor Float.\033[m')

    
    return True


dados = pd.read_csv('./dadosExpandidos.csv')

model = load_model('modelo.h5')

x = validaEntrada('Entre com um valor entre 0-60:', 60) / dados['Entrada'].abs().max()

x_array = np.array([[[x]]])

y_prevision = model.predict(x_array)

print('Valor previsto: ', y_prevision[0][0][0]*dados['Saída'].abs().max())
