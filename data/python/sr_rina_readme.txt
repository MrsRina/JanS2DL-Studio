** Executar .py sem ter Python **

Eu estava fazendo uns testes com Python para ver como ele se comporta sem ter instalado, digamos que eu estou tentando compilar um c�digo sem ter Python, eu tive sucesso, sem precisar usar  terceiras biblitecas, aqui em baixo vou mostrar um tutorial de como compilar sem precisar ter instalado Python:

** 1 Passo: **
- Com seu c�digo feito, ou seja o c�digo que voc� quer compilar sem ter Python em seu S.O;

** 2 Passo: **
- Acesse esse link para voc� baixar os arquivos que usar� no Python, no entanto voc� ter� que baixar conforme o c�digo for feito, seria a vers�o, com a vers�o escolhida aperte no link que tenha "x86-64 embeddable" se for s� 32 bits "x86 embeddable" ;
  - https://www.python.org/downloads/windows/

** 3 Passo: **
- Depois de baixado, voc� ter� que abrir, l� vai ter um monte de arquivos, e voc� s� vai copiar esses arquivos;
  - python37.zip (dependendo da vers�o e diferente o nome do arquivo)
  - python3.dll (dependendo da vers�o)
  - python37.dll (dependendo da vers�o)
  - python.exe

** 4 Passo: **
- Em seguida voc� ter� que fazer um sistema de pasta um pouco complexa, at� por que voc� t� portando um arquivo .py, siga um exemplo abaixo:
```Python
data / qualquer nome
    	python / qualquer nome
       		 """ Basicamente aqui � como a pasta do Python ""
        		""" se querer adicionar alguma biblioteca entre
        		no arquivo python32.zip, l� vai perceber que 
        		ele funciona como a pasta LIB, ou em geral
        		como a que guarda as libs basicas como site-
        		-packages, ou seja caso quer colocar alguma
        		biblioteca coloque l� .
    
        		se dar algum problema de DLL, 
        		ou de lib, at� mesmo _tkinter d
        		a lib tkinter, �  s� criar conforme
        		est� na pasta do Python original.
        		"""
		python32.zip
        	python.exe
    
	seu_c�digo.py

exec.bat
python3.dll
python37.dll
```

** 5 Passo: **
- Voc� deve ter visto o exec.bat, ent�o ele basicmente � o exe do arquivo, isso para windows, ou seja ele serve para executar os arquivos, vou colocar em baixo como deve ser aquele arquivo:

```
path=data/python/

python data/seu_c�digo.py
```
 
** OBS: se voc� for um programador bom e esperto, voc� pode converter o bat para exe. **
Bom � isso, eu fiz essas pesquisas e consegui fazer um passo a passo para quem quer fazer sem terceiras librarys...