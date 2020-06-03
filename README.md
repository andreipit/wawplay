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

download wheel/tar.gz and install manually:
    Anaconda Prompt
    conda activate D:\progs\conda\cvenv04_default
    cd download
    pip install wawplay-0.0.2-py3-none-any.whl # same result1
    or
    pip install wawplay-0.0.2.tar.gz # same result2
    * pip list => wawplay 0.0.2
