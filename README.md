In order to run Karel program you need:

1. Python 3.9+
2. stanfordkarel python package
3. pytest python package
4. pytest-timeout python package

To install related packages run:

```
pip install stanfordkarel
pip install pytest
pip install pytest-timeout
```

In order to run public tests in command line run:

```
pytest test/move_beepers_test.py
```

In order to run private tests in command line run:
```
pytest test/private_move_beepers_test.py
```