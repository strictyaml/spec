from hitchstory import StoryCollection, HitchStoryException
from pathquery import pathquery
from engine import Engine
from hitchrun import DIR, expected
import hitchbuildpy


class ReferenceParser(object):
    def __init__(self, paths):
        self._paths = paths
    
    def ensure_built(self):
        self._virtualenv = hitchbuildpy.VirtualenvBuild(
            name="py{0}".format("3.7.0"),
            base_python=hitchbuildpy.PyenvBuild("3.7.0").with_build_path(
                self._paths.share
            ),
        ).with_build_path(self._paths.gen)
        self._virtualenv.ensure_built()
    
    def lex_to_json(self, string):
        return self._virtualenv.bin.python("lex.py", string).in_dir(DIR.project / "reference").output()

    


def _parser():
    parser = ReferenceParser(DIR)
    parser.ensure_built()
    return parser

def _stories(parser):
    return StoryCollection(pathquery(DIR.project / "examples").ext("story"), Engine(parser))

@expected(HitchStoryException)
def bdd(*keywords):
    """
    Run story with name containing keywords.
    """
    _stories(_parser()).shortcut(
        *keywords
    ).play()


@expected(HitchStoryException)
def regression():
    """
    Run all stories
    """
    _stories().ordered_by_name().play()
