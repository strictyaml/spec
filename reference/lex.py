from re import compile


LEXER_RULES = {
    "COLONSPACE": compile(r"\:\s"),
    "COLON": compile(r"\:"),
    "TEXT": compile(r"([^\n\:]+)"),
    "INDENT": compile(r"\n\s+"),
    "NEWLINE": compile(r"\n"),
}


class Token(object):
    def __init__(self, pos, tokentype, text):
        self.pos = pos
        self.tokentype = tokentype
        self.text = text

    def as_dict(self):
        return {
            "type": self.tokentype,
            "text": self.text,
            "pos": self.pos
        }


class StrictYAMLLexer(object):
    def from_source(self, text):
        self.buf = text
        self.current_pos = 0

    def token(self):
        if self.current_pos >= len(self.buf):
            return None
        else:            
            for token_type, regex in LEXER_RULES.items():
                match = regex.match(self.buf, self.current_pos)
                if match:
                    self.current_pos = match.end()
                    return Token(self.current_pos, token_type, match.group())
            
            raise Exception("No lexer rule found")
            

    def tokens(self):
        while True:
            token = self.token()
            if token is None:
                break
            yield token
        


if __name__ == '__main__':
    import sys
    import json
    lexer = StrictYAMLLexer()
    lexer.from_source(sys.argv[1])

    with open("/tmp/lex", "w") as handle:
        handle.write(
            json.dumps(
                [
                    token.as_dict() for token in
                    lexer.tokens()
                ],
                indent=4,
                sort_keys=True,
            )
        )
