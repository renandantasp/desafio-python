# Desafio Dev Python Jr/Pl - 2022

Orientações gerais:

* Todos os problemas **devem** ser implementados em Python;
* Cada problema **deve** ser implementado em um arquivo separado;
* As implementações podem incluir casos de teste, utilizar POO, frameworks ou conter outros detalhes que você julgar necessários;
* Lembre-se de incluir instruções para instalação de dependências e execução das soluções.

------------------------------------------------

## Problema 1 - Identificação de substrings

Escreva uma função que recebe duas strings como entrada, `s1` e `s2`, e retorna quantas vezes `s2`ocorre em `s1`.

Exemplo:

| `s1`         | `s2`    | Retorno |
|--------------|---------|---------|
| `'ABCDCDC'`  | `'CDC'` | 2       |

------------------------------------------------

## Problema 2 - Validação de sequência de caracteres

Dois caracteres são considerados um par se o caracter de abertura (i.e. `(`, `{`, `[`) ocorre à esquerda do respectivo caracter de fechamento (`)`, `}`, `]`). São três tipos de pares de caracteres: `()`, `{}`, `[]`.

Um par de caracteres é válido se os caracteres que este cerca também forem pares. Caso contrário, o par não é válido. Exemplos:

| Sequência      | Válida? | Obs.                                                    |
|----------------|---------|---------------------------------------------------------|
| `{[()]}`       | Sim     |                                                         |
| `()[]{}`       | Sim     | A concatenação de subsequências válidas também é válida |
| `([])`         | Sim     |                                                         |
| `{{[[(())]]}}` | Sim     |                                                         |
| `{[()([])]}`   | Sim     |                                                         |
| `([]`          | Não     | Não ocorre o fechamento de par com `(`                  |
| `[({)}]`       | Não     | A substring entre `[` e `]` não é válida                |
| `)(`           | Não     | Não é um par válido                                     |
| `(([{()}])))`  | Não     | Não existe um `(` para parear com o último caracter `)` |


Escreva uma função que recebe uma string composta pelos caracteres `(`, `)`, `{`, `}`, `[` ou `]` e retorna `True` quando a string é válida e, caso contrário, retorna `False`. Obs: Uma sequência vazia também é considerada válida.

------------------------------------------------

## Problema 3 - Verificação de expressões em sentenças

Desenvolva um programa que recebe como entrada uma lista de textos. Cada texto deve ser separado em sentenças e, para cada início de sentença, deve ser verificada a presença de alguma das expressões definidas numa lista.

Definições:
* **sentença:** trecho de texto delimitado por pontuação final (`.?!`);
* **início de sentença:** para este problema, considerar que, se a expressão é iniciada num dos 3 primeiros tokens da sentença, então a expressão está presente no início da sentença;
* **token**: uma string de caracteres contíguos, delimitada por espaços em branco e/ou pontuação;

```
expressoes = ['a partir do exposto', 'baseado no que foi dito', 'por fim']
sentenca = 'Logo, baseado no que foi dito, vale citar o filósofo Pitágoras.'
tokens = ['Logo', ',', 'baseado', 'no', 'que', 'foi', 'dito', ',', 'vale', 
	  'citar', 'o', 'filósofo', 'Pitágoras', '.']
inicio_sentenca = tokens[:2]  # ['Logo', ',', 'baseado']

# a expressão 'baseado no que foi dito' é iniciada no terceiro token da 
# sentença. Pelas definições apresentadas, portanto, há presença de uma 
# expressão da lista `expressoes` no início da sentença.
```

Observações e requisitos:
* A lista de expressões é fixa e está definida no arquivo `expressoes.txt`, uma expressão por linha;
* A entrada para a solução deve ser um arquivo `json` com uma lista de identificadores e respectivos textos (como em `textos.json`);
* O texto relacionado a um identificador pode ter uma ou mais sentenças;
* A saída para a solução **deve** incluir:
    * o identificador do texto;
    * uma lista com cada sentença e a expressão cuja presença foi verificada (`null` se nenhuma das expressões está presente na sentença);
* `output.json` é um arquivo de exemplo de saída.

