import json


difficult_valid = ("very-easy", "easy", "same", "difficult", "very-difficult")
language_valid = ("C", "C++", "Java", "Python", "C#", "Go", "JavaScript", "TypeScript", "VisualBasic", "Julia", "VBScript", "F#", "PHP", "Pascal", "Haskell", "Swift", "Ruby", "Perl", "Lua", "Scala", "R", "Kotlin", "Other")
refactoring_valid = ("none", "little", "less", "have", "more", "lot", "full")
algorithm_valid = ("never", "hardly-ever", "sometimes", "usually", "always")
what_to_do_valid = ("games", "tools", "websites-fore", "websites-back", "servers", "datas", "science", "math", "softwares", "systems", "algorithms", "languages", "hobby", "work", "other")


def check(value: str, valid: tuple[str, ...]):
    if value not in valid:
        raise RuntimeError(f"Value \"{value}\" is invalid. ")


def check_all(values: list[str], valid: tuple[str, ...]):
    for value in values:
        check(value, valid)


def get_values() -> dict[str, list[str] | str]:
    uid: str = input("Uid: ")
    try:
        _ = int(uid)
    except ValueError:
        raise RuntimeError(f"String \"{uid}\" is not an integer.")
    difficult: str = input("Difficult: ")
    check(difficult, difficult_valid)
    language: list[str] = input("Language: ").split(", ")
    check_all(language, language_valid)
    refactoring: str = input("Refactoring: ")
    check(refactoring, refactoring_valid)
    algorithm: str = input("Algorithm: ")
    check(algorithm, algorithm_valid)
    what_to_do: list[str] = input("What-to-do: ").split(", ")
    check_all(what_to_do, what_to_do_valid)
    say: str = input("Say: ")
    return {
        "uid": uid, 
        "difficult": difficult, 
        "language": language, 
        "refactoring": refactoring, 
        "algorithm": algorithm, 
        "what-to-do": what_to_do, 
        "say": say, 
    }


def write_data(datas: dict[str, list[str] | str]):
    with open("submitdata.json", "r") as file:
        already_str = file.read()
    
    already = json.loads(already_str)
    already["count"] += 1
    items = ("difficult", "language", "refactoring", "algorithm", "what-to-do")
    for item in items:
        data = datas[item]
        if type(data) is str:
            already[item][data] += 1
        else:
            for ele in data:
                already[item][ele] += 1
    if datas["uid"] in already["uid"]:
        raise RuntimeError(f"Uid {datas["uid"]} already exist. ")
    already["uid"].append(datas["uid"])
    if datas["say"] != "":
        already["say"].append(datas["say"])
    
    with open("submitdata.json", "w") as file:
        file.write(json.dumps(already, indent=4))


if __name__ == "__main__":
    write_data(get_values())
