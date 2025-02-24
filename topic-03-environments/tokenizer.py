import re

<<<<<<< HEAD
# define patterns for tokens

=======
# Define patterns for tokens
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
patterns = [
    [r"print","print"],
    [r"\d*\.\d+|\d+\.\d*|\d+", "number"],
    [r"[a-zA-Z_][a-zA-Z0-9_]*", "identifier"],  # identifiers
    [r"\+", "+"],
    [r"\-", "-"],
    [r"\*", "*"],
    [r"\/", "/"],
    [r"\(", "("],
    [r"\)", ")"],
<<<<<<< HEAD
    [r"\s+", "whitespace"],
    [r".", "error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0])
=======
    [r"\s+","whitespace"],
    [r".","error"]
]

for pattern in patterns:
    pattern[0] = re.compile(pattern[0]) 
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

def tokenize(characters):
    tokens = []
    position = 0
    while position < len(characters):
        for pattern, tag in patterns:
            match = pattern.match(characters, position)
            if match:
                break
        assert match
<<<<<<< HEAD
        # process errors
        if tag == "error":
            raise Exception("Syntax error")

        token = { 
            "tag" : tag,
            "position" : position,
            "value" : match.group(0)

=======
        # (process errors)
        if tag == "error":
            raise Exception("Syntax error")
        token = {
            "tag":tag,
            "position":position,
            "value":match.group(0)
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
        }
        if token["tag"] == "number":
            if "." in token["value"]:
                token["value"] = float(token["value"])
            else:
                token["value"] = int(token["value"])
        if token["tag"] != "whitespace":
            tokens.append(token)
        position = match.end()
    # append end-of-stream marker
<<<<<<< HEAD
    tokens.append ({
        "tag" : None,
        "position" : position,
        "value" : None
    })
    return tokens


=======
    tokens.append({
        "tag":None,
        "value":None,
        "position":position
    })
    return tokens

>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
def test_simple_token():
    print("test simple token")
    examples = "+-*/()"
    for example in examples:
<<<<<<< HEAD
        t = tokenize(example) [0]
=======
        t = tokenize(example)[0]
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
        assert t["tag"] == example
        assert t["position"] == 0
        assert t["value"] == example

<<<<<<< HEAD

def test_number_token():
    print("test number tokens")
    for s in ["1", "11"]:
=======
def test_number_token():
    print("test number tokens")
    for s in ["1","11"]:
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == int(s)
    for s in ["1.1","11.11","11.",".11"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "number"
        assert t[0]["value"] == float(s)


def test_multiple_tokens():
    print("test multiple tokens")
    tokens = tokenize("1+2")
<<<<<<< HEAD
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, 
                      {'tag': '+', 'position': 1, 'value': '+'}, 
                      {'tag': 'number', 'position': 2, 'value': 2}, 
                      {'tag': None, 'position': 3, 'value': None}
                      ]

=======
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, {'tag': '+', 'position': 1, 'value': '+'}, {'tag': 'number', 'position': 2, 'value': 2}, {'tag': None, 'value': None, 'position': 3}]
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

def test_whitespace():
    print("test whitespace")
    tokens = tokenize("1 + 2")
<<<<<<< HEAD
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, 
                      {'tag': '+', 'position': 2, 'value': '+'}, 
                      {'tag': 'number', 'position': 4, 'value': 2}, 
                      {'tag': None, 'position': 5, 'value': None}
                      ]
    

def test_keywords():
    print("test keywords")
=======
    assert tokens == [{'tag': 'number', 'position': 0, 'value': 1}, {'tag': '+', 'position': 2, 'value': '+'}, {'tag': 'number', 'position': 4, 'value': 2}, {'tag': None, 'value': None, 'position': 5}]

def test_keywords():
    print("test keywords...")
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
    for keyword in [
        "print",
    ]:
        t = tokenize(keyword)
        assert len(t) == 2
        assert t[0]["tag"] == keyword, f"expected {keyword}, got {t[0]}"
        assert "value" not in t

def test_identifier_tokens():
<<<<<<< HEAD
    print("test identifier tokens")
=======
    print("test identifier tokens...")
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f
    for s in ["x", "y", "z", "alpha", "beta", "gamma"]:
        t = tokenize(s)
        assert len(t) == 2
        assert t[0]["tag"] == "identifier"
        assert t[0]["value"] == s



def test_error():
<<<<<<< HEAD
    print("test errors")
    try:
        t = tokenize("$1+2")
        assert False, "should have raised an error for an invalid character"
    except Exception as e:
        assert "Syntax error" in str(e), f"Unexpected exception: {e}"
    
=======
    print("test error")
    try:
        t = tokenize("$1+2")
        assert False, "Should have raised an error for an invalid character."
    except Exception as e:
        assert "Syntax error" in str(e),f"Unexpected exception: {e}"
>>>>>>> ceebb1e3177c356998007d9f770a97e950df577f

if __name__ == "__main__":
    test_simple_token()
    test_number_token()
    test_multiple_tokens()
    test_whitespace()
    test_keywords()
    test_identifier_tokens()
    test_error()