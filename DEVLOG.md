comecei criando uma função que converte strings para bits
o primeiro passo foi transfomrar cada caracter da string em seu valor numerico seguindo a tabela ASCII
e agora vou transformar cada numero em seu valor binario
    entao tipo 4 >> 0
    pega o binario do 4 entao 100
    e desloca 0 bits entao o retorno é 4
    mas 4 >> 1
    desloca um bit pra direita entao
    100 vira 10
    porque o mais pra direita meio que some dai retorna 2 
    4 >> 2
    faz os dois sumirem sobra 1, dai retorna 1
    
    dai se associado ao & 1 ele faz uma operação lógica do retorno binario de >> e compara com 0...0001 (AND) que basicamente 
    retorna o utlimo digito da palavra binaria

