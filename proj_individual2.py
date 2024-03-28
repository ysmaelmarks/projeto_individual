dados = [
    ["candidato1", 10, 9, 9, 9],
    ["candidato2", 10, 7, 9, 9],
    ["candidato3", 10, 6, 8, 9],
]
def procurarCandidato(dados, entrevista, testeTeorico, testePratico, softSkills):
    resultado = []
    for candidato in dados:
        nome, e, t, p, s = candidato
        if e >= entrevista and t >= testeTeorico and p >= testePratico and s >= softSkills:
            resultado.append([
                nome,
                adicionarPrefixo(e, "e"),
                adicionarPrefixo(t, "t"),
                adicionarPrefixo(p, "p"),
                adicionarPrefixo(s, "s"),
            ])
            # Transforma os valores númericos em string
            # Depois a partir do indice 1, o join concatena todos os indices restantes com o caractere _
            resultado = [[candidato[0], '_'.join(map(str, candidato[1:]))] for candidato in resultado]
    return resultado

def adicionarPrefixo(nota, prefixo):
    return prefixo + str(nota)

busca = procurarCandidato(dados, 1, 1, 1, 1)
print(busca)
