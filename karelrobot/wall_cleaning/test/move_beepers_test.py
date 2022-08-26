from pathlib import Path

import pytest
from stanfordkarel.karel_application import StudentCode
from stanfordkarel.karel_program import KarelProgram, KarelException


def execute_karel_code(code_file: Path, world_name: str = "", expected_error: str = "") -> None:
    world_name = world_name or code_file.stem
    karel = KarelProgram(world_name)
    try:
        student_code = StudentCode(code_file)
    except (SyntaxError, RuntimeError) as e:
        assert str(e) == expected_error
        return

    student_code.inject_namespace(karel)
    try:
        student_code.mod.main()
        assert karel.compare_with(KarelProgram(f"{world_name}_end")), \
            "Resulting world did not match expected result."
    except (KarelException, NameError) as e:
        assert str(e) == expected_error


@pytest.mark.timeout(10)
@pytest.mark.parametrize("world_name", ("5x5_move_beepers", "10x15_move_beepers"))
def test_move_beepers(world_name: str) -> None:
    execute_karel_code(Path("wall_cleaning.py"), world_name)
