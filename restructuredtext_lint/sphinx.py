# Load in our dependencies
BUILTIN_DOMAINS = None
try:
    # Import all known sphinx domains
    # See: https://github.com/sphinx-doc/sphinx/tree/1.3/sphinx/domains
    from sphinx.domains import BUILTIN_DOMAINS
except ImportError:
    pass

from .utils import EmptyDirective, get_empty_role


# Define our constants
#   Default/base roles and directives for Sphinx
# See: http://sphinx-doc.org/markup/para.html
# And: http://sphinx-doc.org/markup/toctree.html#directive-toctree
# And: https://github.com/sphinx-doc/sphinx/blob/1.3/sphinx/directives/other.py

# TODO: Is this really neecessary? We should be able to leverage BUILTIN_DOMAINS

BASE_SPHINX_ROLES = ('ctype',)
BASE_SPHINX_DIRECTIVES = ('autosummary', 'centered', 'currentmodule',
                          'deprecated', 'hlist', 'include', 'index',
                          'literalinclude', 'no-code-block', 'seealso',
                          'toctree', 'todo', 'versionadded', 'versionchanged')


def get_sphinx_domains():
    """Helper to retrieve domains from Sphinx"""
    if BUILTIN_DOMAINS is None:
        raise RuntimeError('`restructuredtext-lint` tried to import `BUILTIN_DOMAINS` from `sphinx.domains` '
                           '(`from sphinx.domains import BUILTIN_DOMAINS`) at the initial load time but was unable to.'
                           'Please verify `sphinx` is installed properly.')
    return BUILTIN_DOMAINS


def get_directive_names():
    """Retrieve existing all possible directive names from Sphinx

    Raises a ``RuntimeError`` if sphinx is not importable.

    :rtype list: List of names for `directives` within Sphinx
    """
    # Get all the domains directives and roles and insert them on a copy
    sphinx_directives = list(BASE_SPHINX_DIRECTIVES)
    sphinx_domains = get_sphinx_domains()
    for name, domain_class in sphinx_domains.items():
        domain_directives = getattr(domain_class, 'directives', [])

        # Ensure that we also use the name prefixed version as well
        # for example :py:func: and :func: are equivalent and we need to make
        # sure we register both kinds.
        sphinx_directives.extend(domain_directives)
        if name != 'std':
            sphinx_directives.extend('{domain}:{item}'.format(domain=domain_class.name,
                                                              item=item)
                                     for item in domain_directives)

    # Return our list of directives
    return sphinx_directives


def get_roles_names():
    """Retrieve existing all possible directive names from Sphinx

    Raises a ``RuntimeError`` if sphinx is not importable.

    :rtype list: List of names for `roles` within Sphinx
    """

    # Get all the domains directives and roles and insert them on a copy
    sphinx_roles = list(BASE_SPHINX_ROLES)
    sphinx_domains = get_sphinx_domains()
    for name, domain_class in sphinx_domains.items():
        domain_roles = getattr(domain_class, 'roles', [])

        # Ensure that we also use the name prefixed version as well
        # for example :py:func: and :func: are equivalent and we need to make
        # sure we register both kinds.
        sphinx_roles.extend(domain_roles)
        if name != 'std':
            sphinx_roles.extend('{domain}:{item}'.format(domain=domain_class.name,
                                                         item=item)
                                for item in domain_roles)

    # Return our list of roles
    return sphinx_roles

def get_empty_directives_roles():
    """Helper to retrieve empty directives and roles for Sphinx

    :rtype dict: Container for empty directives/roles `{directives, roles}`
    """
    EmptyDirective()
    get_empty_role()
    pass
