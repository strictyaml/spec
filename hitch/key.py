from hitchstory import StoryCollection, HitchStoryException
from commandlib import CommandError
from pathquery import pathquery
from engine import Engine
from hitchrun import DIR, expected
import hitchbuildpy
from path import Path


class ReferenceParser(object):
    def __init__(self, paths):
        self._paths = paths
    
    def ensure_built(self):
        self._virtualenv = hitchbuildpy.VirtualenvBuild(
            name="py{0}".format("3.7.0"),
            base_python=hitchbuildpy.PyenvBuild("3.7.0").with_build_path(
                self._paths.share
            ),
        ).with_packages("ipython", "q").with_build_path(self._paths.gen)
        self._virtualenv.ensure_built()
    
    def lex_to_json(self, string):
        if Path("/tmp/lex").exists():
            Path("/tmp/lex").remove()
        self._virtualenv.bin.python("lex.py", string).in_dir(DIR.project / "reference").run()
        return Path("/tmp/lex").text()

    


def _parser():
    parser = ReferenceParser(DIR)
    parser.ensure_built()
    return parser


def _stories(parser, rewrite=False):
    return StoryCollection(
        pathquery(DIR.project / "examples").ext("story"),
        Engine(parser, rewrite=rewrite)
    )



@expected(HitchStoryException)
def bdd(*keywords):
    """
    Run story with name containing keywords.
    """
    _stories(_parser()).shortcut(*keywords).play()


@expected(HitchStoryException)
def rbdd(*keywords):
    """
    Run story with name containing keywords.
    """
    _stories(_parser(), rewrite=True).shortcut(*keywords).play()


@expected(HitchStoryException)
def regression():
    """
    Run all stories
    """
    _stories().ordered_by_name().play()


@expected(CommandError)
def rerun():
    """
    Rerun last example code block with specified version of python.
    """
    from commandlib import Command
    Command(DIR.gen.joinpath("py{0}".format("3.7.0"), "bin", "python"))(
        DIR.gen.joinpath("working", "examplepythoncode.py")
    ).in_dir(DIR.gen.joinpath("working")).run()
