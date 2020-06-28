import io
import json

def paresJson():

    jsonOffset = io.open('C:\\Users\\53238\\Desktop\\json_offset.txt', 'w', encoding='utf-8')
    jsonFile = io.open('C:\\Users\\53238\\Desktop\\response.txt', 'r' ,encoding='utf-8')

    index_dic = json.load(jsonFile)
    dic = index_dic['content']
    # print(dic)
    num = 0
    for contentIndex in dic:
        # print(contentIndex)
        num += 1
        terms_dic = contentIndex['term_vectors']['content']['terms']
        offsetList = []
        # 每个分词term的循环 
        for index in terms_dic:
            tokens_dic = terms_dic[index]['tokens']
            # 把start与end记录在一起，并且对start做排序
            for record in tokens_dic:
                start = record['start_offset']
                end = record['end_offset']
                offset = str(start) + ',' + str(end)
                offsetList.append(offset)
            # print(tokens_dic)
        inputStr = ';'.join(offsetList)
        jsonOffset.write(inputStr)
        jsonOffset.write('\n')
        # print(offsetList)

    print(num)

paresJson()