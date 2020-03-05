

def frequency_analysis(message):
    frequencies = dict({})
    for ch in message:
        if ch in frequencies:
            frequencies[ch] += 1
        else:
            frequencies[ch] = 1
    return frequencies


msg = """ХБЮЖХЛЖЮЩЫБХЛЖДЛЖЗХПНЫЯЛЖЫЖЗПДЯЛГХЛЦЫПЫШИЛЮЛВХФБХЖСЛЩЫБХЗСЛЫ
ЯЛЦРБДЛЖДЧЫПНЫГГДЛГЫМЫШДЛХЛЖЮЩЫЗСЛЦЫЭЛЩЫБХЛЖХВЮЛЭГХЫЗЫЛЩЫБДЛ
ГЫБЫШАДЫЛПХЭЛЩПИШДЯЛДГХЛЕПХЧЩХЛЖИГИБХЛГДЖЛЧЛАГЮШИЛАДЗДПИУЛЖЫ
ЖЗПХЛМЮЗХБХЛГДЛЗХВЛГЫЛДАХЭХБДЖСЛГЮЛАХПЗЮГДАЛГЮЛЖЗЮНАДЧ"""

frequencies = frequency_analysis(msg)

for (char, count) in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
    print(f'\'{char}\': {count}')