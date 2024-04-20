def abs_path_from_project(relative_path: str):
    import qa_guru_HW20_emulator
    from pathlib import Path

    return (
        Path(qa_guru_HW20_emulator.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
