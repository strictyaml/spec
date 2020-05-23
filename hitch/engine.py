from hitchstory import GivenDefinition, GivenProperty, InfoDefinition, InfoProperty
from hitchstory import BaseEngine, validate, no_stacktrace_for
from strictyaml import CommaSeparated, Str, Int
from templex import Templex
import json

class Engine(BaseEngine):
    given_definition = GivenDefinition(string=GivenProperty(Str()))

    #info_definition = InfoDefinition(jiras=InfoProperty(schema=CommaSeparated(Str())))

    def __init__(self, parser, rewrite=False):
        self._parser = parser
        self._rewrite = rewrite

    def set_up(self):
        pass

    @no_stacktrace_for(AssertionError)
    def lexed_as(self, example_json):
        try:
            Templex(example_json).assert_match(self._parser.lex_to_json(self.given['string']))
        except AssertionError:
            if self._rewrite:
                self.current_step.update(string=example_json)
            else:
                raise

    def tear_down(self):
        pass
