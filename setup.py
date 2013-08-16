from setuptools import setup, find_packages

setup(
    name='collective.behavior.localskin',
    version='1.0.0',
    description='Dexterity behavior to enable a local theme skin',
    long_description=(open('README.rst').read() + '\n' +
                      open('CHANGES.rst').read()),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python',
    ],
    keywords='',
    author='Asko Soukka',
    author_email='asko.soukka@iki.fi',
    url='https://github.com/collective/collective.behavior.localskin/',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective.behavior.localskin'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
       'collective.behavior.localregistry',
       'plone.app.registry',
       'plone.app.theming>=1.1',
       'plone.behavior',
       'plone.directives.form',
       'plone.registry',
       'Products.CMFCore',
       'Products.CMFPlone>=4.2',
       'setuptools',
       'zope.component',
       'zope.i18nmessageid',
       'zope.interface',
       'zope.schema',
    ],
    extras_require={'test': [
        'plone.app.testing',
    ]},
    entry_points='''
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    '''
)
