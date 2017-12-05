from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A simple lightweight python wrapper for the Microsoft Cognitive Services based on usage for machine learning."
VERSION = '0.0.1'
LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    "Programming Language :: Python :: 3",
    'Topic :: Software Development :: Libraries :: Python Modules',
]

KEYWORDS = ['Microsoft', 'Cognitive Services', 'API', 'Search']

INSTALL_REQUIRES = [
    'requests',
]

setup(
    name='py-ms-cognitive-ml',
    packages = find_packages(),
    version=VERSION,
    author=u'Oliver Reid',
    author_email='reiol787@student.otago.ac.nz',
    url='https://github.com/beardo01/py-ms-cognitive-ml',
    license='MIT',
    keywords=KEYWORDS,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    test_suite='nose.collector',
    tests_require=['nose'],
)
