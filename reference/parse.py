from lex import StrictYAMLLexer

class Node(object):
    def __init__(self, nodetype, text):
        self.nodetype = nodetype
        self.text = text
        self._value = None
        
    def set_value(self, node):
        self._value = node
        
    def __repr__(self):
        return "<parse.Node: type={}, text={}>".format(
            self.nodetype,
            self.text.__repr__(),
        )

    def as_dict(self):
        item = {
            "type": self.nodetype,
            "text": self.text,
        }
        if self._value is not None:
            item["value"] = self._value.as_dict()
        return item


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
        line_position = 0
        current_node = None
        value_mode = False
        
        node_stack = []
        key_stack = []
        
        for token in self.lex_tokens:
            if token.tokentype == "NL":
                indent_level = 0
                current_node = None
                
                

            if token.tokentype == "NL_INDENT":
                indent_level = len(token.text.lstrip("\n")) / 2
                
            
            if token.tokentype == "TEXT":
                if token.text.startswith("#"):
                    toks.append(Node("COMMENT", token.text.rstrip("#")))
                if token.text.startswith("-"):
                    toks.append(Node("LI", token.text.lstrip("- ")))
                else:
                    key_stack.append(token.text)

            if token.tokentype in ("COLON", "COLON_SPACE"):
                key_stack.append(":")
                    
                    
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
