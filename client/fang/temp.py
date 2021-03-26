import json


def get_text(i):
    ff = open(f'data/{i+1}.json', 'r', encoding='utf-8')
    text = ff.read()
    ff.close()
    return list(json.loads(text))


with open('data/all.json', 'w', encoding='utf-8') as f:
    text = []
    for i in range(11):
        text += get_text(i)
    f.write(json.dumps(text, ensure_ascii=False, indent=2))
