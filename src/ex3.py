from spacy.lang.pt import Portuguese
import sys, json


def sentences(texts, expr, path):
  if path == None: path = 'out.json'

  out = list()
  nlp = Portuguese()
  nlp.add_pipe("sentencizer")

  doc_expr = list(nlp.pipe(expr))

  for text in texts:
    _id = text['id']
    obj = {"id":_id, "sentenças":[]}

    doc = nlp(text['texto'])
  
    for sent in doc.sents:
      txt_expr = None
      
      for expr in doc_expr:
        if str(expr) in str(sent[0:len(expr)+2]).lower():
          txt_expr = str(expr)
      
      obj['sentenças'].append({"sentença":str(sent),"expressao":txt_expr})

    out.append(obj)
  
  dump = json.dumps(out,indent = 2, ensure_ascii=False)
  
  f = open(path,'w')
  f.write(dump)
  f.close()




def main(argv):
  if len(argv) >= 2:
    path = None

    f = open(argv[1])
    texts = json.load(f)
    f.close()

    if len(argv) >= 3:
      path = argv[2]

    f = open('../expressoes.txt')
    exprs = f.read().split('\n')
    f.close()

    sentences(texts, exprs, path)
  else:
    print('Arquivo de entrada não encontrado')


if __name__ == '__main__':
    main(sys.argv)