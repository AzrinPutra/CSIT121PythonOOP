#Dictionary

def test1():
    data = {'csit121': 'oo programming',
            'csit115': 'database',
            'csit1=213': 'java'}
    nested_list = [['csit121', 'oo programming']]

    # 3 common methods
    #1
    print('keys')   
    for v in data.keys():
        print(v)

    #2 
    print('Value')
    for v in data.values():
        print(v)

    #3
    print('Key-value pairs')
    for mod, name in data.items():
        print(mod,name)

def test2():
    data = {'csit121': {'name': 'oo programming', 'credits': 6},
            'csit115': {'name': 'database', 'credits': 3}
           }
    for mod in data.keys():
        print(mod)
        print(data[mod])
        print(data[mod]['name'])    #Calling out name key value
        print(data[mod]['credits']) #Calling out credit key value

def test3():
    scores = {}
    #Setting keys into the dictionary
    scores['Alice'] = 80
    scores['Jones'] = 68
    print(scores)
    scores['Alice'] = 50
    print(scores)

def test4():
    scores = {'s1':[60,50,26],
              's2':[60],
              's3':[2,42,65,78,81,95]} #list representing the values of scores while s1 is the key

    for id, values in scores.items():
        ave_scores = sum(values) / len(values)
        print(id,values)
        print("Average score")
        print(id,ave_scores)


def main():
    test1()
    #test2()
    #test3()
    #test4()

main()