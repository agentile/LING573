from distutils.core import setup
from distutils.dist import DistributionMetadata

# Patch distutils if it can't cope with the "classifiers" keyword (prior to Python 2.3.0).
if not hasattr(DistributionMetadata, 'classifiers'):
    DistributionMetadata.classifiers = None

setup(
            name = "Pattern",
         version = "2.5",
     description = "Web mining module for Python.",
         license = "BSD",
          author = "Tom De Smedt",
    author_email = "tom@organisms.be",
             url = "http://www.clips.ua.ac.be/pages/pattern",
        packages = [
        "pattern",
        "pattern.web", 
        "pattern.web.cache", 
        "pattern.web.feed", 
        "pattern.web.imap", 
        "pattern.web.json", 
        "pattern.web.oauth", 
        "pattern.web.pdf", 
        "pattern.web.soup",
        "pattern.db", 
        "pattern.text",
        "pattern.text.de",
        "pattern.text.de.parser",
        "pattern.text.de.inflect",
        "pattern.text.en",
        "pattern.text.en.parser", 
        "pattern.text.en.inflect", 
        "pattern.text.en.wordlist",
        "pattern.text.en.wordnet", 
        "pattern.text.en.wordnet.pywordnet",
        "pattern.text.es",
        "pattern.text.es.parser", 
        "pattern.text.es.inflect", 
        "pattern.text.fr",
        "pattern.text.fr.parser",
        "pattern.text.fr.inflect",
        "pattern.text.nl",
        "pattern.text.nl.parser",
        "pattern.text.nl.inflect",
        "pattern.vector",
        "pattern.vector.svm",
        "pattern.graph"
    ],
    package_data = {
        "pattern"                   : ["*.js"],
        "pattern.web.cache"         : ["tmp/*"],
        "pattern.web.feed"          : ["*"],
        "pattern.web.json"          : ["*"],
        "pattern.web.pdf"           : ["*.txt", "cmap/*"],
        "pattern.web.soup"          : ["*"],
        "pattern.text.de.parser"    : ["*.txt", "*.xml"],
        "pattern.text.de.inflect"   : ["*.txt"],
        "pattern.text.en.parser"    : ["*.txt", "*.xml"],
        "pattern.text.en.inflect"   : ["*.txt"],
        "pattern.text.en.wordlist"  : ["*.txt"],
        "pattern.text.en.wordnet"   : ["*.txt", "dict/*"],
        "pattern.text.en.wordnet.pywordnet" : ["*"],
        "pattern.text.es.parser"    : ["*.txt", "*.xml"],
        "pattern.text.es.inflect"   : ["*.txt"],
        "pattern.text.fr.parser"    : ["*.txt", "*.xml"],
        "pattern.text.fr.inflect"   : ["*.txt"],
        "pattern.text.nl.parser"    : ["*.txt", "*.xml"],
        "pattern.text.nl.inflect"   : ["*.txt"],
        "pattern.vector"            : ["*.txt"],
        "pattern.vector.svm"        : ["*"],
        "pattern.graph"             : ["*.js", "*.csv"],
    },
    py_modules = [
        "pattern.metrics",
        "pattern.text.search"
    ],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: Dutch",
        "Natural Language :: English",
        "Natural Language :: French",
        "Natural Language :: German",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: Markup :: HTML"
    ]
)