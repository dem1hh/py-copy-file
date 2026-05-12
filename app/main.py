def copy_file(command: str) -> None:

    parts_file = command.split()
    if len(parts_file) != 3:
        return
    if parts_file[0] != "cp":
        return
    fst_file = parts_file[1]
    snd_file = parts_file[2]
    if fst_file == snd_file:
        return

    try:
        with open(fst_file, "r") as fd:
            cop_file = fd.read()
        with open(snd_file, "w") as sn:
            sn.write(cop_file)
    except FileNotFoundError:
        return
