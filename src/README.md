## Problema 1 - Identificação de substrings

Para a resolução desse problema é criado um loop para varrer a string `s1` onde `idx` vai de `0 -> len(s1)`. Em cada iteração é feita uma verificação se `s2` é igual a substring presente em `s1` entre o índice `[idx:idx+len(s2)]`. Dessa forma, no final da iteração será verificada a existencia da substring `s2` em todas posições possíveis de `s1`. 

Os casos de teste estão presentes dentro da solução, além disso, para esse problema não foi utilizado nenhuma biblioteca adicional

A solução está presente em `ex1.py` e pode ser executada pelo comando `python3 ex1.py`

----

## Problema 2 - Validação de sequência de caracteres

Para a resoluçao desse problema foi criada uma lista chamada `stack` que foi utilizada como uma pilha. Para evitar alguns erros em runtime envolvendo o acesso da ultima posição de lista uma lista vazia, a `stack` é inicializada contendo um valor qualquer.

Após isso, é feito um loop que percorre a sequência. Para cada ocorrência de algum caracter de abertura `['(','{','[']`, o caractere em questão é inserido na pilha. Para cada ocorrência de um caracter de fechamento `[')','}',']']` é verificado se o caracter em questão é o par do ultimo caracter de abertura inserido na lista. Se for, o caracter do topo da pilha é retirado, se não for, a função retorna `False` e termina sua execução.

No final do loop é verificado se a lista está igual quando se iniciou o loop, contendo apenas um valor qualquer. Se sim, quer dizer que todos os caracteres de abertura foram fechados a função retorna `True`, caso contrário retorna `False`.

Além disso, qualquer ocorrência de algum caracter diferente dos de abertura ou fechamento fará a função retornar `False`.

Os casos de teste estão presentes dentro da solução, além disso, para esse problema não foi utilizado nenhuma biblioteca adicional

A solução está presente em `ex2.py` e pode ser executada pelo comando `python3 ex2.py`

----

## Problema 3 - Verificação de expressões em sentenças

Para esse problema foi utilizado uma framework externa chamada Spacy, ela e suas dependencias estão presente no arquivo `requirements.txt`. Para instalá-los em um ambiente virtual ou no próprio ambiente é necessário exectuar:

```pip install -r requirements.txt```

A solução está presente em `ex3.py` e para ser executada é necessário passar o `path` do documento dos textos, assim os comandos de execução são:

#### Caminho do output sendo `out.json`

```python3 ex3.py '../textos.json```

#### Caminho do output sendo modificado

```python3 ex3.py '../textos.json <PATH>```


O primeiro passo para resolver esse problema é ler o arquivo de entrada contendo os textos e fazer o parsing de `JSON -> dict()` e armazenar no dict `texts`, após isso a lista de expressões também é lida e armazenada numa lista chamada `exprs`.

Após isso, é utilizada a framework Spacy pra inicializar na variavel `nlp` um objeto da classe Language, para essa aplicação utilizamos o `Portuguese()` dado que os textos estão em português. Em seguida adicionamos à pipeline o componente `sentencizer` que faz a identificação de sentenças em um texto. Além de identificar as sentenças, o `nlp` também é capaz de fazer a tokenização dos corpus, que será necessário em etapas futuras do problema.

Executamos o `nlp` em `exprs` e guardamos o retorno em `doc_exprs`. Com tudo isso pronto, inicializamos um loop para percorrer os textos.

Executamos o `nlp` em cada um dos textos e armazenamos o retorno em `doc`, o atributo `doc.sents` nos retorna a lista de sentenças presentes no texto. Com isso, é feito um loop percorrendo cada sentença em doc.sents para adicionar ao `json` de retorno e verificar a ocorrência de alguma das expressões inicializadas até os três primeiros tokens.

Após isso, é verificado se cada uma das expressões está presente na frase e se está inicializada entre o primeiro e terceiro token, se está a expressão vai pro retorno, mas se nenhuma for encontrada o campo expressão do retorno será `null`.

Após a finalização de todos os loops, estará pronto um dict contendo todas as frases de um texto e suas expressões caso encontrada, esse dict é convertido em um json e escrito no arquivo de saída.
