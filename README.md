# wawplay
what a wonderful playground!

https://packaging.python.org/tutorials/packaging-projects/

Anaconda Prompt
cd wawplay
python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel

register on test.pypi.org
python -m pip install --user --upgrade twine

python -m twine upload --repository testpypi dist/*
    user: andreipit
    pwd: from chrome (test.pypi.org)
    View at:
    https://test.pypi.org/project/wawplay/0.0.2/

