** Executar .py sem ter Python **

Eu estava fazendo uns testes com Python para ver como ele se comporta sem ter instalado, digamos que eu estou tentando compilar um código sem ter Python, eu tive sucesso, sem precisar usar  terceiras biblitecas, aqui em baixo vou mostrar um tutorial de como compilar sem precisar ter instalado Python:

** 1 Passo: **
- Com seu código feito, ou seja o código que você quer compilar sem ter Python em seu S.O;

** 2 Passo: **
- Acesse esse link para você baixar os arquivos que usará no Python, no entanto você terá que baixar conforme o código for feito, seria a versão, com a versão escolhida aperte no link que tenha "x86-64 embeddable" se for só 32 bits "x86 embeddable" ;
  - https://www.python.org/downloads/windows/

** 3 Passo: **
- Depois de baixado, você terá que abrir, lá vai ter um monte de arquivos, e você só vai copiar esses arquivos;
  - python37.zip (dependendo da versão e diferente o nome do arquivo)
  - python3.dll (dependendo da versão)
  - python37.dll (dependendo da versão)
  - python.exe

** 4 Passo: **
- Em seguida você terá que fazer um sistema de pasta um pouco complexa, até por que você tá portando um arquivo .py, siga um exemplo abaixo:
```Python
data / qualquer nome
    	python / qualquer nome
       		 """ Basicamente aqui é como a pasta do Python ""
        		""" se querer adicionar alguma biblioteca entre
        		no arquivo python32.zip, lá vai perceber que 
        		ele funciona como a pasta LIB, ou em geral
        		como a que guarda as libs basicas como site-
        		-packages, ou seja caso quer colocar alguma
        		biblioteca coloque lá .
    
        		se dar algum problema de DLL, 
        		ou de lib, até mesmo _tkinter d
        		a lib tkinter, é  só criar conforme
        		está na pasta do Python original.
        		"""
		python32.zip
        	python.exe
    
	seu_código.py

exec.bat
python3.dll
python37.dll
```

** 5 Passo: **
- Você deve ter visto o exec.bat, então ele basicmente é o exe do arquivo, isso para windows, ou seja ele serve para executar os arquivos, vou colocar em baixo como deve ser aquele arquivo:

```
path=data/python/

python data/seu_código.py
```
 
** OBS: se você for um programador bom e esperto, você pode converter o bat para exe. **
Bom é isso, eu fiz essas pesquisas e consegui fazer um passo a passo para quem quer fazer sem terceiras librarys...