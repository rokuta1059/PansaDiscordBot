import random
import json


def select_one(index):
    """
    망언을 하나 랜덤하게 또는 지정된 번호의 망언 json 을 반환 한다
    :param index: 주어진 번호 (0인 경우 랜덤, 그 외의 숫자인 경우 해당하는 번호의 망언)
    :return: 선택된 망언 json
    """
    data = json.loads(open("pansadb/absurd/diary.json", encoding='utf8').read())
    if index == 0:
        return data[str(random.randint(1, len(data)))]
    else:
        if index > len(data):
            return None
        else:
            return data[str(index)]

def find_name(name):
    """
    망언을 한 사람의 이름을 기준으로 망언을 검색한다
    해당하는 망언의 이름이 일치하는 경우 해당 망언의 번호를 저장한 후
    번호가 저장된 배열을 return 한다
    :param name: 검색하려는 망언을 한 사람의 이름
    :return: 해당 검색 결과의 망언 번호 list
    """
    num_list = []
    data = json.loads(open("pansadb/absurd/diary.json", encoding='utf8').read())
    for i in range(1, len(data) + 1):
        if name in data[str(i)]['name']:
            num_list.append(i)
    return num_list

def find_description(content):
    """
    망언의 설명과 내용을 기준으로 망언을 검색한다
    해당하는 망언의 설명과 내용에 검색하는 값이 포함된 경우 해당 망언의 번호를 저장한 후
    번호가 저장된 배열을 return 한다
    :param content: 검색하려는 망연 내용
    :return: 해당 검색 결과의 망언 번호 list
    """
    num_list = []
    data = json.loads(open("pansadb/absurd/diary.json", encoding='utf8').read())
    for i in range(1, len(data) + 1):
        if content in data[str(i)]['description'] or content in data[str(i)]['absurd']:
            num_list.append(i)
    return num_list

def add_absurd(absurd, name, description):
    """
    망언을 추가한다
    JSON 파일에 추가하려는 망언을 저장한다
    :param absurd: 망언 내용
    :param name: 망언을 한 사람
    :param description: 망언 설명
    :return: 추가된 해당 망언의 JSON
    """
    data = json.loads(open("pansadb/absurd/diary.json", encoding='utf8').read())
    tmp = {
        'absurd': absurd,
        'name': name,
        'description': description,
        'number': len(data) + 1
    }
    with open('diary.json', 'w', encoding='UTF8') as saveFile:
        json.dump(data, saveFile, indent='\t', ensure_ascii=False)

    return tmp

def change_absurd(absurd, name, description, num):
    """
    망언을 수정한다
    해당하는 번호의 망언을 수정하고 저장한다
    :param absurd: 수정하려는 망언 내용
    :param name: 수정하려는 망언을 한 사람
    :param description: 수정하려는 망언 설명
    :param num: 수정하려는 망언 번호
    :return: 수정된 해당 망언의 JSON
    """
    data = json.loads(open("pansadb/absurd/diary.json", encoding='utf8').read())
    data[str(num)] = {
        'absurd': absurd,
        'name': name,
        'description': description,
        'number': num
    }
    with open('diary.json', 'w', encoding='UTF8') as saveFile:
        json.dump(data, saveFile, indent='\t', ensure_ascii=False)

    return data[str(num)]
