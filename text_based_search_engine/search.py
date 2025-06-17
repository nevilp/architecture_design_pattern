import re
from collections import defaultdict
import math
'''
 A. Tokenization
Split text into words (tokens).
Remove stopwords, lowercase, and optionally stem.
'''
def tokenize(text):
    stopwords={"the","is","of","to","a"}
    tokens = re.findall(r'\b\w+\b',text.lower())
    return [ t for t in tokens if t not in stopwords]
'''
🔹 B. Inverted Index Construction
Maps token → set of document IDs (docIDs).
'''

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(set)

    def add_document(self, doc_id,text) :
        for token in tokenize(text):
            self.index[token].add(doc_id)

    def get_docs(self,token):
        return self.index.get(token,set())      

'''
🔹 C. Ranking (TF-IDF Score)
Rank documents based on TF-IDF (Term Frequency-Inverse Document Frequency):
TF(t, d) = term frequency in document

IDF(t) = log(N / df(t)) where N = total documents, df(t) = document frequency of term.
'''

class Ranker:
    def __init__(self,index,documents):
        self.index = index
        self.documents = documents
        self.doc_count = len(documents)

    #"How Rare or Special is This Word?"
    def compute_idf(self,term):
        df = len(self.index.get_docs(term))
        return math.log((self.doc_count+1)/(df+1))+1
    
    def score(self,query):
        scores = defaultdict(float)
        query_terms = tokenize(query)
        for term in query_terms:
            idf = self.compute_idf(term)
            for doc_id in self.index.get_docs(term):
                tf = tokenize(self.documents[doc_id]).count(term)
                scores[doc_id]+=tf*idf
        return sorted(scores.items(),key= lambda x:x[1], reverse=True)        


class SearchEngine:
    def __init__(self):
        self.index = InvertedIndex()
        self.documents = {}

    def add_document(self,doc_id,text):
        self.documents[doc_id] = text
        self.index.add_document(doc_id,text)

    def search(self,query):
        ranker = Ranker(self.index,self.documents)
        return ranker.score(query)
    
se = SearchEngine()
se.add_document(1, "The quick brown fox jumps over the lazy dog")
se.add_document(2, "Never jump over the lazy dog quickly")

results = se.search("quick dog")
print(results)   