# Load in our dependencies
# DEV: Use `absolute_import` to remove confusion about where `sphinx` comes from
from __future__ import absolute_import

# Define placeholder for memoization
memo_map = {}

# Define our constants
#   Default/base roles and directives for Sphinx
#   http://sphinx-doc.org/markup/para.html
#   http://sphinx-doc.org/markup/toctree.html#directive-toctree
#   https://github.com/sphinx-doc/sphinx/blob/1.3/sphinx/directives/other.py

# TODO: Is this really neecessary? We should be able to leverage BUILTIN_DOMAINS

BASE_SPHINX_ROLES = ('ctype',)
BASE_SPHINX_DIRECTIVES = ('autosummary', 'centered', 'currentmodule',
                          'deprecated', 'hlist', 'include', 'index',
                          'literalinclude', 'no-code-block', 'seealso',
                          'toctree', 'todo', 'versionadded', 'versionchanged')


def get_builtin_domains():
    """Helper to retrieve domains from Sphinx"""
    # Attempt to load memoized BUILTIN_DOMAINS
    if memo_map.get('_BUILTIN_DOMAINS') is not None:
        return memo_map['_BUILTIN_DOMAINS']

    # Otherwise, import Sphinx's builtin domains
    #   https://github.com/sphinx-doc/sphinx/tree/1.3/sphinx/domains
    # DEV: We lazy load this to avoid loading Sphinx directives prematurely
    from sphinx.domains import BUILTIN_DOMAINS
    memo_map['_BUILTIN_DOMAINS'] = BUILTIN_DOMAINS
    return memo_map['_BUILTIN_DOMAINS']


def register_builtin_domain(key):
    """Register a specific builtin domain to `docutils

    :param str key: Name of builtin domain (e.g. `c`, `cpp`, `py`)
        https://github.com/sphinx-doc/sphinx/blob/1.3/sphinx/domains/__init__.py#L285-L292
    """
    # https://github.com/sphinx-doc/sphinx/blob/1.3/sphinx/domains/python.py#L582-L622
    domain = get_builtin_domains()[key]
    domain_name = domain.name
    for directive_name in domain.directives:
        # TODO: Import in docutils `register_directive` and use that
        pass
    # # http://repo.or.cz/w/docutils.git/blob/1976ba91eff979abc3e13e5d8cb68324833af6a0:/docutils/parsers/rst/directives/__init__.py#l134  # noqa
    # if directives:
    #     for directive in directives:
    #         # register_directive(name, directive)
    #         rst_directives.register_directive(directive['name'], directive['directive'])
    # # http://repo.or.cz/w/docutils.git/blob/1976ba91eff979abc3e13e5d8cb68324833af6a0:/docutils/parsers/rst/roles.py#l146  # noqa
    # if roles:
    #     for role in roles:
    #         # register_local_role(name, role_fn)
    #         rst_roles.register_local_role(role['name'], role['role_fn'])


def register_builtin_domains():
    """Register all Sphinx builtin domains to `docutils`"""
    for key in get_builtin_domains():
        register_builtin_domain(key)
