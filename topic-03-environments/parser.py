from tokenizer import tokenize

"""
parser.py -- implement parser for simple expressions

Accept a string of tokens, return an AST expressed as stack of dictionaries
<<<<<<< HEAD
                                     (Abstract Syntax Tree)
=======
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
"""

"""
    factor = <number> | <identifier> | "(" expression ")"
    term = factor { "*"|"/" factor }
    expression = term { "+"|"-" term }
    statement = <print> expression | expression
"""

<<<<<<< HEAD
=======

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
def parse_factor(tokens):
    """
    factor = <number> | <identifier> | "(" expression ")"
    """
    token = tokens[0]
    if token["tag"] == "number":
<<<<<<< HEAD
        return {
            "tag":"number",
            "value": token["value"]
        }, tokens[1:]
    if token["tag"] == "identifier":
        return {
            "tag": "identifier",
            "value": token["value"]
        }, tokens[1:]
=======
        return {"tag": "number", "value": token["value"]}, tokens[1:]
    if token["tag"] == "identifier":
        return {"tag": "identifier", "value": token["value"]}, tokens[1:]
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
    if token["tag"] == "(":
        ast, tokens = parse_expression(tokens[1:])
        assert tokens[0]["tag"] == ")"
        return ast, tokens[1:]
<<<<<<< HEAD
    raise Exception(f"Unexpected token '{token['tag']}' at position {token['position']}.")
=======
    raise Exception(
        f"Unexpected token '{token['tag']}' at position {token['position']}."
    )

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

def test_parse_factor():
    """
    factor = <number> | <identifier> | "(" expression ")"
    """
<<<<<<< HEAD
    print("Testing parse_factor()")

    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        assert ast == {'tag': 'number', 'value': int(s)}
        assert tokens[0]['tag'] == None 
    for s in ["(1)","(22)"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        s_n = s.replace("(","").replace(")","")
        assert ast=={'tag': 'number', 'value': int(s_n)}
        assert tokens[0]['tag'] == None 
    tokens = tokenize("(2+3)")
    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': '+', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 3}}

    tokens = tokenize("(x+3)")
    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': '+', 
                   'left': {'tag': 'identifier', 'value': "x"}, 
                   'right': {'tag': 'number', 'value': 3}}

    tokens = tokenize("x")
    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': 'identifier', 'value' : "x"}


    for s in ["(1)", "(22)"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        s_n = s.replace("(", "").replace(")", "") # remove parenthesis
        assert ast == {'tag': 'number', 'value': int(s_n)}
        assert tokens[0]['tag'] == None 

    tokens = tokenize("(2+3)*4")
    ast, tokens = parse_factor(tokens)
    assert ast == {'tag': '+', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 3}}

=======
    print("testing parse_factor()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        assert ast == {"tag": "number", "value": int(s)}
        assert tokens[0]["tag"] == None
    for s in ["(1)", "(22)"]:
        tokens = tokenize(s)
        ast, tokens = parse_factor(tokens)
        s_n = s.replace("(", "").replace(")", "")
        assert ast == {"tag": "number", "value": int(s_n)}
        assert tokens[0]["tag"] == None
    tokens = tokenize("(2+3)")
    ast, tokens = parse_factor(tokens)
    assert ast == {
        "tag": "+",
        "left": {"tag": "number", "value": 2},
        "right": {"tag": "number", "value": 3},
    }
    tokens = tokenize("x")
    ast, tokens = parse_factor(tokens)
    assert ast == {"tag": "identifier", "value": "x"}
    tokens = tokenize("(x+3)")
    ast, tokens = parse_factor(tokens)
    print(ast)
    assert ast == {
        "tag": "+",
        "left": {"tag": "identifier", "value": "x"},
        "right": {"tag": "number", "value": 3}
    }
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f


def parse_term(tokens):
    """
<<<<<<< HEAD
    term = factor { "*" | "/" factor }
=======
    term = factor { "*"|"/" factor }
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
    """
    node, tokens = parse_factor(tokens)
    while tokens[0]["tag"] in ["*", "/"]:
        tag = tokens[0]["tag"]
<<<<<<< HEAD
        # tokens = tokens[1:] shortcut by putting the slicing in the function call
        right_node, tokens = parse_factor(tokens[1:])
        node = { "tag" : tag, "left" : node, "right" : right_node }
=======
        right_node, tokens = parse_factor(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
    return node, tokens


def test_parse_term():
    """
<<<<<<< HEAD
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
=======
    term = factor { "*"|"/" factor }
    """
    print("testing parse_term()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_term(tokens)
        assert ast == {"tag": "number", "value": int(s)}
        assert tokens[0]["tag"] == None
    tokens = tokenize("2*4")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "tag": "*",
        "left": {"tag": "number", "value": 2},
        "right": {"tag": "number", "value": 4},
    }
    tokens = tokenize("2*4/6")
    ast, tokens = parse_term(tokens)
    assert ast == {
        "tag": "/",
        "left": {
            "tag": "*",
            "left": {"tag": "number", "value": 2},
            "right": {"tag": "number", "value": 4},
        },
        "right": {"tag": "number", "value": 6},
    }
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f


def parse_expression(tokens):
    """
    expression = term { "+"|"-" term }
    """
    node, tokens = parse_term(tokens)
<<<<<<< HEAD
    while tokens[0]["tag"] in ["+","-"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_term(tokens[1:])
        node = {"tag":tag, "left":node, "right":right_node}
=======
    while tokens[0]["tag"] in ["+", "-"]:
        tag = tokens[0]["tag"]
        right_node, tokens = parse_term(tokens[1:])
        node = {"tag": tag, "left": node, "right": right_node}
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

    return node, tokens


def test_parse_expression():
    """
<<<<<<< HEAD
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
    tokens = tokenize("1+(2+3)*4")
    ast, tokens = parse_expression(tokens)
    assert ast == {'tag': '+', 'left': {'tag': 'number', 'value': 1}, 'right': {'tag': '*', 'left': {'tag': '+', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 3}}, 'right': {'tag': 'number', 'value': 4}}}
=======
    expression = term { "+"|"-" term }
    """
    print("testing parse_expression()")
    for s in ["1", "22", "333"]:
        tokens = tokenize(s)
        ast, tokens = parse_expression(tokens)
        assert ast == {"tag": "number", "value": int(s)}
        assert tokens[0]["tag"] == None
    tokens = tokenize("2*4")
    ast, tokens = parse_expression(tokens)
    assert ast == {
        "tag": "*",
        "left": {"tag": "number", "value": 2},
        "right": {"tag": "number", "value": 4},
    }
    tokens = tokenize("1+2*4")
    ast, tokens = parse_expression(tokens)
    assert ast == {
        "tag": "+",
        "left": {"tag": "number", "value": 1},
        "right": {
            "tag": "*",
            "left": {"tag": "number", "value": 2},
            "right": {"tag": "number", "value": 4},
        },
    }
    tokens = tokenize("1+(2+3)*4")
    ast, tokens = parse_expression(tokens)
    assert ast == {
        "tag": "+",
        "left": {"tag": "number", "value": 1},
        "right": {
            "tag": "*",
            "left": {
                "tag": "+",
                "left": {"tag": "number", "value": 2},
                "right": {"tag": "number", "value": 3},
            },
            "right": {"tag": "number", "value": 4},
        },
    }

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

def parse_statement(tokens):
    """
    statement = <print> expression | expression
    """
    if tokens[0]["tag"] == "print":
        value_ast, tokens = parse_expression(tokens[1:])
<<<<<<< HEAD
        ast = {
            'tag':'print',
            'value': value_ast
        }
=======
        ast = {"tag": "print", "value": value_ast}
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

    else:
        ast, tokens = parse_expression(tokens)
    return ast, tokens

<<<<<<< HEAD
=======

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
def test_parse_statement():
    """
    statement = <print> expression | expression
    """
    print("testing parse_statement()")
    tokens = tokenize("1+(2+3)*4")
    ast, tokens = parse_statement(tokens)
<<<<<<< HEAD
    assert ast == {'tag': '+', 'left': {'tag': 'number', 'value': 1}, 'right': {'tag': '*', 'left': {'tag': '+', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 3}}, 'right': {'tag': 'number', 'value': 4}}}
    tokens = tokenize("print 2*4")
    ast, tokens = parse_statement(tokens)
    assert ast == {'tag': 'print', 'value': {'tag': '*', 'left': {'tag': 'number', 'value': 2}, 'right': {'tag': 'number', 'value': 4}}}

=======
    assert ast == {
        "tag": "+",
        "left": {"tag": "number", "value": 1},
        "right": {
            "tag": "*",
            "left": {
                "tag": "+",
                "left": {"tag": "number", "value": 2},
                "right": {"tag": "number", "value": 3},
            },
            "right": {"tag": "number", "value": 4},
        },
    }
    tokens = tokenize("print 2*4")
    ast, tokens = parse_statement(tokens)
    assert ast == {
        "tag": "print",
        "value": {
            "tag": "*",
            "left": {"tag": "number", "value": 2},
            "right": {"tag": "number", "value": 4},
        },
    }
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f


def parse(tokens):
    ast, tokens = parse_statement(tokens)
    return ast

<<<<<<< HEAD
=======

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
if __name__ == "__main__":
    test_parse_factor()
    test_parse_term()
    test_parse_expression()
    test_parse_statement()
    print("done.")
