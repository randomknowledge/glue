try:
    from setuptools import setup
    kw = {'entry_points':
          """[console_scripts]\nglue = glue:main\n""",
          'zip_safe': False}
except ImportError:
    from distutils.core import setup
    kw = {'scripts': ['glue.py']}


def check_requirements(requires):
    """
    :param requires:
        List of requirements. If a list item is itself a list, this function checks if
        any item of this list is already installed (in order) and uses this as requirement.
        If non is installed the first item of the list is used.
    :return: List of requirements
    """
    requirements = []
    import pkg_resources
    for line in requires:
        if isinstance(line, list):
            is_installed = False
            for req in line:
                try:
                    pkg_resources.require(req)
                    requirements.append(req)
                except pkg_resources.DistributionNotFound:
                    pass
                except pkg_resources.VersionConflict:
                    pass
                else:
                    is_installed = True
            if not is_installed:
                requirements.append(line[0])
        else:
            requirements.append(line)
    return requirements

setup(
    name='glue',
    version='0.3-rk',
    url='http://github.com/randomknowledge/glue',
    license='BSD',
    author='Jorge Bastida',
    author_email='me@jorgebastida.com',
    description='Glue is a simple command line tool to generate CSS sprites.',
    long_description=('Glue is a simple command line tool to generate CSS '
                      'sprites using any kind of source images like '
                      'PNG, JPEG or GIF. Glue will generate a unique PNG '
                      'file containing every source image and a CSS file '
                      'including the necessary CSS classes to use the '
                      'sprite.'),
    py_modules=['glue'],
    platforms='any',
    install_requires=check_requirements([
        ['Pillow==1.7.8', 'PIL==1.1.7'],
    ]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    **kw
)
