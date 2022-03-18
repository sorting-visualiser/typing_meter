# Build and Run

If you want to understand how typing meter works or want to debug an issue, you'll want to get the source, build it, and run it locally.

## Getting the Source

First, fork the typing meter repository so that you can make a pull request. Clone your fork locally and then you can navigate to the directory where you've cloned the repository.
```
git clone https://github.com/<<<your-github-account>>>/typing_meter.git
cd where-you-cloned-    
```

## Running in Development Mode

Once you have a local copy of typing_meter cloned, you can directly run typing_meter in Development Mode.
```
python -m typing_meter [OPTION]... [FILE]...
```
You'll need [windows_curses](https://pypi.org/project/windows-curses/) installed for running typing_meter on windows.
You can install it by running the following command.
```
pip install windows_curses
```

## Installing from Source

You can install the module directly from sources by running the following command.
```
python setup.py install
```

## Building documentation

Install [Sphinx](https://github.com/sphinx-doc/sphinx) and [Read the Docs Sphinx Theme](https://github.com/readthedocs/sphinx_rtd_theme) by running the following command.
```
pip install sphinx sphinx_rtd_theme
```
To build the docs locally, run -
```
python setup.py build_sphinx
```
The HTML pages are built in `build\sphinx\html`.
