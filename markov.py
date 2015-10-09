from pymarkovchain import MarkovChain

mc = MarkovChain("./markov2")


sentence_regex = """(?s-i)(?<=^|\A|\.[^.]+)[A-Z\d]
(
(Jan|Feb)\.\s+\d{1,2}\s*,\s+\d{4}
|
[^!?] 
)*?
[.!?]
(?=\s|$|\Z)"""


with open("data.txt", "r") as f:
    mc.generateDatabase(f.read(),
                        sentenceSep='[.!?]\s',
                        n=2)

mc.generateString()
