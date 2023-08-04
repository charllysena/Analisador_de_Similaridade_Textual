import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista
    contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do
    texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas



def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca'''
    return re.split(r'[,:;]+', sentenca)




def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase'''
    return frase.split()



def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def separa_sentenças_na_lista(lista_textos):
    texto_separado = []
    for e in range(0, len(lista_textos)):
        lista_textos[e] = separa_sentencas(lista_textos[e])
        texto_separado.append(lista_textos[e])
    return texto_separado


def separa_frases_na_lista(sentenças):
    frases = []
    for e in range(0, len(sentenças)):
        frases_interm = []
        for s in sentenças[e]:
            frases_interm.append(separa_frases(s))
        frases.append(frases_interm)
    return frases   


def separa_palavras_na_lista(frases):
    palavras = []
    for e in range(0, len(frases)):
        palavras_int = []
        for s in range(0, len(frases[e])):
            for f in frases[e][s]:
                palavras_int.append(separa_palavras(f))
            
        palavras.append(palavras_int)
    return palavras


def concatena_lista_na_lista(lista_palavras):
    lista_unida = []
    for e in range(0, len(lista_palavras)):
        lista_int = []
        for p in lista_palavras[e]:
            lista_int += p
        lista_unida.append(lista_int)
    return lista_unida


def tamanho_médio_das_palavras(palavras):
    tamanho_palavras = []
    for e in range(0, len(palavras)):
        tamanho_parcial = 0
        for tp in palavras[e]:
            tamanho_parcial += len(tp)
        tamanho_medio = tamanho_parcial / len(palavras[e])
        tamanho_palavras.append(tamanho_medio)
    return tamanho_palavras


def palavras_diferentes_nas_listas(listas):
    palav_dif = []
    for p in listas:
        palav_dif.append(n_palavras_diferentes(p))
    return palav_dif


def relação_type_token(lista):
    tamanho = []
    for li in range(0, len(lista)):
        frequencia = palavras_diferentes_nas_listas(lista)
        tam = len(lista[li])
        tamanho.append(tam)

    rel_typetoken = []
    for f in range(0, len(frequencia)):
        typetoken = frequencia[f] / tamanho[f]
        rel_typetoken.append(typetoken)
    
    return rel_typetoken


def razão_hapax_legomana(lista):
    palavras_unicas = []
    tamanho2 = []
    for e in range(0, len(lista)):
        palavras_unicas.append(n_palavras_unicas(lista[e]))
        tamanho2.append(len(lista[e]))
        razão_hl = []
        for r in range(0, len(palavras_unicas)):
            razão_hl.append(palavras_unicas[r] / tamanho2[r])

    return razão_hl

def tamanho_médio_da_sentença(lista):
    tamanhos_medios = []
    for sl in range(0, len(lista)):
        tamanho_total = 0
        for s in lista[sl]:
            taman = len(s)
            tamanho_total += taman
        tam_med = tamanho_total / len(lista[sl])
        tamanhos_medios.append(tam_med)

    return tamanhos_medios

def complexidade_de_senteça(frases):
    tamanhos_medios = []
    for f in range(0, len(frases)):
        tamanho = 0
        for s in range(0, len(frases[f])):
            tamanho +=(len(frases[f][s]))
        tamanhos_medios.append(tamanho / len(frases[f]))

    return tamanhos_medios


def tamanho_medio_de_frase(frases):
    tamanhos_medios_frase = []
    for f in range(0, len(frases)):
        tamanho = 0
        for s in range(0, len(frases[f])):
            tamanho +=(len(frases[f][s]))
        tamanhos_medios_frase.append(tamanho / len(frases[f]))

    return tamanhos_medios_frase


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura
    do texto.'''
    tex = []
    if type(texto) is str:
        tex.append(texto)
    else:
        tex = texto
    sent = separa_sentenças_na_lista(tex)
    fras = separa_frases_na_lista(sent)
    palav = separa_palavras_na_lista(fras)
    palavras_reun = concatena_lista_na_lista(palav)
    extensão_média_das_palavras = tamanho_médio_das_palavras(palavras_reun)
    tp_token = relação_type_token(palavras_reun)
    raz_hlego = razão_hapax_legomana(palavras_reun)
    tam_med_sent = tamanho_médio_da_sentença(sent)
    comp_de_sent = complexidade_de_senteça(fras)
    frases_reun = concatena_lista_na_lista(fras)
    tam_med_fras = tamanho_medio_de_frase(frases_reun)
    assinaturas = []
    for val in range(0, len(extensão_média_das_palavras)):
        assinaturas.append(extensão_média_das_palavras[val])
        assinaturas.append(tp_token[val])
        assinaturas.append(raz_hlego[val])
        assinaturas.append(tam_med_sent[val])
        assinaturas.append(comp_de_sent[val])
        assinaturas.append(tam_med_fras[val])
    return assinaturas


def calcula_similaridades(assi_a, assi_b):
    similaridades = [] 
    for e in range(0, len(assi_a)):
        simil = (abs(assi_a[0] - assi_b[0]) + abs(assi_a[1] - assi_b[1]) + abs(assi_a[2]- assi_b[2])
            + abs(assi_a[3] - assi_b[3]) + abs(assi_a[4] - assi_b[4]) + abs(assi_a[5] - assi_b[5])) / 6
        similaridades.append(simil)
    return similaridades


def compara_assinatura(assi_a, assi_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade
        nas assinaturas.'''
    indice_similaridade = (abs(assi_a[0] - assi_b[0]) + abs(assi_a[1] - assi_b[1]) + abs(assi_a[2]- assi_b[2])
            + abs(assi_a[3] - assi_b[3]) + abs(assi_a[4] - assi_b[4]) + abs(assi_a[5] - assi_b[5])) / 6
    return indice_similaridade


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero
    (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ind_similaridade = []
    assinaturas_calculadas = []
    for t in range(0, len(textos)):
        assinaturas_calculadas.append(calcula_assinatura(textos[t]))
    print(assinaturas_calculadas)
    ind_similaridade = []
    for assina in range(0, len(assinaturas_calculadas)):  
        similaridades_calc = compara_assinatura(ass_cp, assinaturas_calculadas[assina])
        ind_similaridade.append(similaridades_calc)
    print(ind_similaridade)
    posição_min = ind_similaridade.index(min(ind_similaridade))
    return posição_min + 1


assinat_ref = le_assinatura()
tex = le_textos()
texto_infec = avalia_textos(tex, assinat_ref)
print(f'O autor do texto {texto_infec + 1} está infectado com COH-PIAH')
