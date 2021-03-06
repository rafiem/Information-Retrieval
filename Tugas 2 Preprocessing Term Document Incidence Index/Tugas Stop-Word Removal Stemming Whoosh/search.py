from whoosh.qparser import QueryParser
from whoosh import scoring
from whoosh.index import open_dir
import sys
#indexdir = full corpus, no stemming no stopwords
#indexdir1 = full corpus, stemming, stopwords
#indexdir2 = small corpus, stemming, stopwords, for testing

ix = open_dir("indexdir2")


# query_str is query string
query_str = sys.argv[1]
#query_str = 'today'
# Top 'n' documents as result
topN = int(sys.argv[2])
#topN = 10

with ix.searcher(weighting=scoring.Frequency) as searcher:
    query = QueryParser("content",schema=ix.schema).parse(query_str)
    results = searcher.search(query,limit=topN)
    for i in range(topN):
        print(results[i]['title'], str(results[i].score),results[i]['textdata'])
