#Testando caminho dos arquivos no terminal do vscode

arquiteste = open(r'Aprendendo-Python\files\arquiteste.txt', 'w')
arquiteste.write('O terminal do vscode executou este código em ...\Documents\Code\Python.\n')
arquiteste.write('Caso tenha executado corretamente, este arquivo foi criado na pasta files deste repositório.')
arquiteste.close()