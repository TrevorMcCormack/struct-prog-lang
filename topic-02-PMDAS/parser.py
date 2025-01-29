from tokenizer import tokenize

"""
parser.py -- implement parser for simple expressions

Accept a string of tokens, return an AST expressed as stack of dictionaries
                                     (Abstract Syntax Tree)
"""

"""
   # simple_expression = number | "(" expression ")" | "-" simple_expression
   # factor = simple_expression

    factor = <number>
    term = factor { "*" | "/" factor }
    arithmetic_expression = term { "+" | "-" term }
    expression = arithmetic_expression
"""

def parse_factor(tokens):
    """
    factor = <number>
    """
    token = tokens[0]
    if token["tag"] == "number":
        return { 
            "tag" : "number",
            "value" : token["value"]
        } , tokens[1:]
    raise Exception(f"Unexpected token '{token['tag']}' at position '{token['position']}'")



def test_parse_factor():
    """
    factor = <number>
    """
    print("Testing parse_factor()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        assert ast == {'tag': 'number', 'value': int(s)}
        assert tokens[0]['tag'] == None 


def parse_term(tokens):
    """
    term = factor { "*" | "/" factor }
    """
    node, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        tag = tokens[0]["tag"]
        # tokens = tokens[1:] shortcut by putting the slicing in the function call
        right_node, tokens = parse_factor(tokens[1:])
        node = { "tag" : tag, "left" : node, "right" : right_node }
    return node, tokens


def test_parse_term():
    """
    term = factor { "*" | "/" factor }
    """
    print("Testing parse_term()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        assert ast == {'tag': 'number', 'value': int(s)}
        assert tokens[0]['tag'] == None 
    tokens = tokenize("2*4")
    ast, tokens = parse_term(tokens)
    assert ast == {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}

    tokens = tokenize("2*4/6")
    ast, tokens = parse_term(tokens)
    assert ast == {'tag': '/', 'left': {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}, 'right': {'tag': 'number', 'value': 6}}
    """
    AST:
                                 "/"
                            /            \
                        "*"               6
                      /     \
                     2       4
    """
    #print(ast)
    #exit(0)


def test_parse_expression():
    """
    expression = term { "+" | "-" term }
    """
    print("Testing parse_expression()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        assert ast == {'tag': 'number', 'value': int(s)}
        assert tokens[0]['tag'] == None 
    tokens = tokenize("2*4")
    ast, tokens = parse_term(tokens)
    assert ast == {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}

    tokens = tokenize("2*4/6")
    ast, tokens = parse_term(tokens)
    assert ast == {'tag': '/', 'left': {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}, 'right': {'tag': 'number', 'value': 6}}
    
    tokens = tokenize("1+2*4")
    ast, tokens = parse_expression(tokens)
    assert ast == {'tag': '+', 'left': {'tag': 'number', 'value': 1}, 'right': {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}}

    #print(ast)
    #exit(0)


def parse_expression(tokens):
    """
    expression = term { "+" | "-" term }
    """
    node, tokens = parse_term(tokens)
    while tokens[0]["tag"] in ["+", "-"]:
        tag = tokens[0]["tag"]
        # tokens = tokens[1:] shortcut by putting the slicing in the function call
        right_node, tokens = parse_term(tokens[1:])
        node = { "tag" : tag, "left" : node, "right" : right_node }

    return node, tokens

if __name__ == "__main__":
    test_parse_factor()
    test_parse_term()
    test_parse_expression()
    print("Done")