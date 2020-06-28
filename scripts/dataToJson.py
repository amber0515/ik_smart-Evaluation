# -- coding:UTF-8 --
import io
import json

def hello():
    jsonFile = io.open('C:\\Users\\53238\\Desktop\\pku_test_gold.json', 'w', encoding='utf-8')
    with open("C:\\Users\\53238\\Desktop\\789.txt" ,'r', encoding='utf-8') as f :
        num = 0
        strr = ''
        for line in f:
            strr += line
            if '\n' in line:
                num += 1
                if num % 10 == 0:
                    print("===here===")
                    # num转成str
                    iddint = int(num / 10)
                    idd = str(iddint)
                    jsonFile.write('{"index":{"_index":"test-iksmart-article","_type":"_doc","_id":' + idd + '}}')
                    jsonFile.write('\n')
                    jsonFile.write('{ "content":"'+ strr.replace('\n', '') +'"}')
                    jsonFile.write('\n') 
                    # 拼凑完成将strr清空
                    strr = ''
                print("===123===")

hello()