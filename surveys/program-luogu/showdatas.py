import json


def read_data():
    with open("submitdata.json", "r") as file:
        string = file.read()
    
    return json.loads(string)


def calc_number(number: int, count: int) -> str:
    res: float = number / count * 100
    string: str = f"{res :.2f}"
    return string.rjust(5, "0")


def show_datas(datas):
    count: int = datas["count"]
    print(f"总人数：{count}")

    print("\n难度系数占比：")
    difficult_dict: dict[str, str] = {
        "very-easy": "非常简单", 
        "easy": "比较简单", 
        "same": "不相上下", 
        "difficult": "比较困难", 
        "very-difficult": "非常困难", 
    }
    for item in ("very-easy", "easy", "same", "difficult", "very-difficult"):
        number: int = datas["difficult"][item]
        print(f"{difficult_dict[item]}：{calc_number(number, count)}%")
    
    print("\n语言占比：")
    for item in ("C", "C++", "Java", "Python", "C#", "Go", "JavaScript", "TypeScript", "VisualBasic", "Julia", "VBScript", "F#", "PHP", "Pascal", "Haskell", "Swift", "Ruby", "Perl", "Lua", "Scala", "R", "Kotlin", "Other"):
        number: int = datas["language"][item]
        print(f"{item.rjust(11)}：{calc_number(number, count)}%")
    
    print("\n重构意义占比：")
    refactoring_dict: dict[str, str] = {
        "none": "毫无意义", 
        "little": "意义极小", 
        "less": "意义较小", 
        "have": "有些意义", 
        "more": "意义较大", 
        "lot": "意义极大", 
        "full": "必须去做", 
    }
    for item in ("none", "little", "less", "have", "more", "lot", "full"):
        number: int = datas["refactoring"][item]
        print(f"{refactoring_dict[item]}：{calc_number(number, count)}%")
    
    print("\n想做的事占比：")
    what_to_do_dict: dict[str, str] = {
        "games": "      游戏", 
        "tools": "  实用工具", 
        "websites-fore": "  网页前端", 
        "websites-back": "  网页后端", 
        "servers": "    服务器", 
        "datas": "数据分析师", 
        "science": "  科学领域", 
        "math": "  数学领域", 
        "softwares": "  软件设计", 
        "systems": "  操作系统", 
        "algorithms": "算法工程师", 
        "languages": "  编程语言", 
        "hobby": "  业余爱好", 
        "work": "  帮助工作", 
        "other": "      其他", 
    }
    for item in ("games", "tools", "websites-fore", "websites-back", "servers", "datas", "science", "math", "softwares", "systems", "algorithms", "languages", "hobby", "work", "other"):
        number: int = datas["what-to-do"][item]
        print(f"{what_to_do_dict[item]}：{calc_number(number, count)}%")
    

if __name__ == "__main__":
    show_datas(read_data())
