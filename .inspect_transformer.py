import inspect
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_neo4j import Neo4jGraph

print('LLMGraphTransformer:', LLMGraphTransformer)
print('Methods:')
for name in dir(LLMGraphTransformer):
    if not name.startswith('_'):
        print(' ', name)

try:
    print('\nLLMGraphTransformer.__init__ signature:', inspect.signature(LLMGraphTransformer))
except Exception as e:
    print('Could not get signature for LLMGraphTransformer:', e)

print('\nNeo4jGraph.add_graph_documents:')
print(Neo4jGraph.add_graph_documents)
try:
    print('Signature:', inspect.signature(Neo4jGraph.add_graph_documents))
except Exception as e:
    print('Could not get signature for add_graph_documents:', e)
