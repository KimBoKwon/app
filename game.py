import json

def di(name):
    dic = {
        "name" : name,
        "level" : 1,
        "hp" : 100,
        "weapon" : ["칼", "도끼", "삽"],
        "skill" : ["찌르기", "던지기", "치기"]
    }
    with open('static/save.txt', 'w', encoding='utf-8') as f: 
        json.dump(dic, f, ensure_ascii = False, indent=4)
    # print("{0}님 반갑습니다. level{1}이고 hp{2}으로 게임을 시작하겠습니다.".format(dic["name"], dic["level"], dic["hp"]))
    return dic

def save_game(filename, di):
    f = open(filename, "w", encoding="utf-8")
    for key in di:
        print("%s:%s" % (key, di[key]))
        f.write("%s:%s\n" % (key, di[key]))
    f.closse()