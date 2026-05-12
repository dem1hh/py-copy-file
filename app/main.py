def copy_file(command: str) -> None:

    file = command.split()
    if len(file) != 3:
        return
    if file[0] != "cp":
        return
    fst_file = file[1]
    snd_file = file[2]
    if fst_file == snd_file:
        return

    try:
        with open(fst_file, "r") as fd:
            f = fd.read()
        with open(snd_file, "w") as sn:
            sn.write(f)
    except FileNotFoundError:
        return
