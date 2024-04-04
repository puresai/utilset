# utilset

```sh
mkdir tests
touch setup.py
```
test
> python3 -m unittest tests/*

deploy
```
pip3 install build
pip3 install twine
pip3 install setuptools wheel

python3 setup.py  check

python3 -m build
```


python3 -m twine upload dist/*
