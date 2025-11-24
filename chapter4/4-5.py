# 35. 係り受け木
# 「メロスは激怒した。」の係り受け木を可視化せよ。

import spacy
import ginza
from spacy import displacy
nlp = spacy.load("ja_ginza")

doc = nlp("メロスは激怒した。")
displacy.serve(doc, style="dep", auto_select_port=True)


