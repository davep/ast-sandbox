import ast, pathlib, pathlib as pl
from pathlib import Path

def ast_walk( node, indent="" ):
    if isinstance( node, ast.AST ):
        print( f"{indent}{node.__class__.__name__}" )
        for field in node._fields:
            value = getattr( node, field )
            if value is not None:
                print( f"{indent}{field}" )
                ast_walk( value, indent + " " )
    elif isinstance( node, list ):
        for child in node:
            ast_walk( child, indent + " " )
    else:
        print( f"{indent}{node}" )

if __name__ == "__main__":
    ast_walk( ast.parse( Path( __file__ ).read_text() ).body )
