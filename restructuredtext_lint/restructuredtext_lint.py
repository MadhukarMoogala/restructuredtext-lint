import docutils
from docutils.parsers.rst import Parser

def run(content, filepath=None, **kwargs):
    parser = Parser()
    settings = docutils.frontend.OptionParser(
                    components=(docutils.parsers.rst.Parser,)
                    ).get_default_values()
    document = docutils.utils.new_document(filepath, settings=settings)
    print parser.parse(content, document)
    return []
