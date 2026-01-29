import importlib, inspect
m = importlib.import_module('langchain_neo4j')
cls = getattr(m, 'Neo4jGraph')
print('Class:', cls)
print('Module file:', inspect.getsourcefile(cls))
try:
    sig = inspect.signature(cls)
except Exception:
    sig = inspect.signature(cls.__init__)
print('Call signature:', sig)
print('\n__init__ source (first 2000 chars):')
try:
    src = inspect.getsource(cls.__init__)
    print(src[:2000])
except Exception as e:
    print('Could not get source:', e)
print('\nAvailable attrs:')
print([a for a in dir(cls) if not a.startswith('_')][:200])
