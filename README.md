##In order to run Karel program you need:

1. Python 3.9+
2. stanfordkarel python package
3. pytest python package
4. pytest-timeout python package

## Installing python and related packages using conda

### Set up local environment

In the directory with wall_cleaning.py using command line run:

```
conda create -p .venv python=3.9

```

This will prepare python environment in the folder called .venv. You need to activate the environment before you can 
start using it. For this run:

```
conda activate ./.venv 
```

## Installing related packages

After you created **and activated** your environment execute the following commands:

```
pip install stanfordkarel
pip install pytest
pip install pytest-timeout
```
## Running Karel tests

You can check your solution by running Karel program with two public worlds. For this in the wall_cleaning.py you can 
change name of the world to `5x5_move_beepers` and `10x15_move_beepers`:

```python
if __name__ == '__main__':
    run_karel_program("5_by_5_move_beepers")
```

You can also check your implementation with reference solution by running tests. 

In order to run public tests in command line execute:

```
pytest test/move_beepers_test.py
```

In order to run private tests in command line execute:
```
pytest test/private_move_beepers_test.py
```