# Corretor de provas oficial 

Repositorio do corretor de provas do Einstein Floripa

## Descrição

Esse repositório tem como objetivo corrigir as provas do EinsteinFloripa, além de, gerar gráficos e informações sobre dados das provas
para auxiliar os organizadores na qualidade do Ensino

[Documentação](https://docs.google.com/document/d/1mI35ySDHd7H55XcEsuavb23hBNMRAuuJiFJMtd-sevg/edit?usp=sharing) de como utilizar o projeto.

## Primeiros passos
### Instalação

* Clone o projeto com o comando:
```shell
$ git clone git@github.com:einsteinfloripa/corretor-de-provas-2024.git
``` 

* Entre dentro da pasta "corretor-de-provas"

### Dependências

* Instale os pacotes de dependências usando:
```shell
$ pip install -r ./requirements/requirements.txt
```


* Para executar o programa, execute o arquivo main_window.py, e a interface gráfica deve abrir normalmente.

* para gerar um executável, rode o seguinte comando:
```shell
$ pyinstaller --windowed --icon=assets/icons/einsteinlogo.png --onefile --paths=src main_window.py
```

