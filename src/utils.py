import pandas as pd
textColor = {
    'matematica': 'green',
    'portugues': '#B8AA5E',
    'fisica': 'red',
    'quimica': 'blue',
    'historia': 'orange',
    'biologia': 'purple',
    'geografia': 'cyan',
    'ingles': 'pink',
    'interdisciplinar': 'brown',
    'filosofia-sociologia': 'gray'  
}

mediaDeAcertos = {
    'matematica': 'green',
    'portugues': '#B8AA5E',
    'fisica': 'red',
    'quimica': 'blue',
    'historia': 'orange',
    'biologia': 'purple',
    'geografia': 'cyan',
    'ingles': 'pink',
    'interdisciplinar': 'brown',
    'filosofia-sociologia': 'gray'  
}

textCorrector = {
    'matematica': 'Matemática',
    'portugues': 'Português',
    'fisica': 'Física',
    'quimica': 'Química',
    'historia': 'História',
    'biologia': 'Biologia', 
    'geografia': 'Geografia', 
    'ingles': 'Inglês',
    'interdisciplinar': 'Interdisciplinar',
    'filosofia-sociologia': 'Filosofia-Sociologia'  
}

numero_de_colunas = {
    "simulinho" :52
}

def convert_to_int(string):
    if isinstance(string,str):
            if string== "0" or string=="-" or string=="--":
                string = 0
            elif string[0] == "0" and len(string)>1:
                string = string[1::]
                string = int(string)
            else:
                string = int(string)
    return string


