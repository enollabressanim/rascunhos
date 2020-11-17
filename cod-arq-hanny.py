import base64

def codificar(cod_arq, nome_arq):
    
    texto_bytes = cod_arq.encode('ascii')
    base64_bytes = base64.b64encode(texto_bytes)
    base64_message = base64_bytes.decode('ascii')
    arquivo = open(nome_arq, "w")
    arquivo.write(base64_message)
    arquivo.close()
    return arquivo

def decodificar(nome_arq_cod):

    decod_arq = open(nome_arq_cod,'r')
    line = decod_arq.readline()
    decodificarBytes = base64.b64decode(line)
    decodificarStr = str(decodificarBytes, "utf-8")
    print(decodificarStr)
    return decodificarStr

def main () : 

    alternativa = input(str("Digite CODIFICAR se desejas codificar ou DECODIFICAR se desejas decodificar um arquivo: "))

    if alternativa == "CODIFICAR":
        cod_arq = input("Digite o que desejas codificar: ")
        nome_arq = input("Digite o nome do arquivo: ")
        codificar(cod_arq, nome_arq)

    elif alternativa == "DECODIFICAR": 
        nome_arq_cod = input("digite o nome do arquivo para decodificar: ")
        decodificar(nome_arq_cod)

if __name__ =='__main__':
    main ()