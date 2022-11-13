import ast
from pathlib import Path

def ast_walk( thing, indent="" ):
    for node in thing:
        print( f"{indent}{node}" )
        try:
            ast_walk( node.body, indent + " " )
        except AttributeError:
            pass

if __name__ == "__main__":
    ast_walk( ast.parse( Path( __file__ ).read_text() ).body )
