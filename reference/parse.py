from lex import StrictYAMLLexer

class Node(object):
    def __init__(self, nodetype, text):
        self.nodetype = nodetype
        self.text = text
        
        
    def __repr__(self):
        return "<parse.Node: type={}, text={}>".format(
            self.nodetype,
            self.text.__repr__(),
        )

    def as_dict(self):
        return {
            "type": self.nodetype,
            "text": self.text,
        }


class StrictYAMLParser(object):
    def __init__(self):
        pass
    
    def from_source(self, text):
        lexer = StrictYAMLLexer()
        lexer.from_source(text)
        self.lex_tokens = list(lexer.tokens())
    
    def tokens(self):
        toks = []
        indent_level = 0
        for token in self.lex_tokens:
            if token.tokentype == "TEXT" and token.text.startswith("#"):
                toks.append(Node("COMMENT", token.text.rstrip("#")))
                            
        return toks


if __name__ == '__main__':
    import sys
    import json
    parser = StrictYAMLParser()
    parser.from_source(sys.argv[1])

    with open("/tmp/parse", "w") as handle:
        handle.write(
            json.dumps(
                [
                    token.as_dict() for token in
                    parser.tokens()
                ],
                indent=4,
                sort_keys=True,
            )
        )
