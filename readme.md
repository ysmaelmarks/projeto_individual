## Projeto de Curso do Senac / Resilia
===================================

## Descrição do Projeto
--------------------

Este projeto consiste em um sistema de busca de candidatos com base em critérios de avaliação, como entrevista, teste teórico, teste prático e soft skills.
O sistema retorna os candidatos que atendem aos requisitos especificados.
Este projeto também será utilizado para avaliação da atividade individual do primeiro módulo do curso SENAC CNSeg

## Como usar
------------------

Clone o repositório para seu ambiente local. Será necessário python 3.11 ou superior

```sh
$ git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

Execute o arquivo Python proj_individual2.py para realizar a busca de candidatos:

```sh
$ py proj_individual2.py
```

### Você também pode utilizar o programa alterando os argumentos da função procurarCandidato() e a lista "dados"

## Exemplo de uso
```sh
$ dados = [
$    ["candidato1", 10, 9, 9, 9],
$    ["candidato2", 10, 7, 9, 9],
$    ["candidato3", 10, 6, 8, 9],
$ ]
$
$ busca = procurarCandidato(dados, 1, 1, 1, 1)
$ print(busca)
```


## Funções Principais
------------------

### `procurarCandidato(dados, entrevista, testeTeorico, testePratico, softSkills)`

*   Descrição: Realiza a busca de candidatos com base nos critérios especificados.
*   Parâmetros:
    *   `dados`: Lista de listas contendo os dados dos candidatos.
    *   `entrevista`, `testeTeorico`, `testePratico`, `softSkills`: Notas mínimas necessárias para cada critério.
*   Retorno: Lista dos candidatos que atendem aos critérios especificados.

### `adicionarPrefixo(nota, prefixo)`

*   Descrição: Adiciona um prefixo a uma nota.
*   Parâmetros:
    *   `nota`: Nota do candidato.
    *   `prefixo`: Prefixo a ser adicionado à nota.
*   Retorno: Nota com o prefixo adicionado.