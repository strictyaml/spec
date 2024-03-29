from re import compile


LEXER_RULES = (
    ("COLON_SPACE", compile(r"\: ")),
    ("COLON", compile(r"\:")),
    ("NL_INDENT", compile(r"\n\s+")),
    ("TEXT", compile(r"([^\n\:]+)")),
    ("NL", compile(r"\n")),
)


class Token(object):
    def __init__(self, pos, tokentype, text):
        self.pos = pos
        self.tokentype = tokentype
        self.text = text
    
    
    def __repr__(self):
        return "<lex.Token: pos={}, type={}, text={}>".format(
            self.pos,
            self.tokentype,
            self.text.__repr__(),
        )

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
            for token_type, regex in LEXER_RULES:
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
