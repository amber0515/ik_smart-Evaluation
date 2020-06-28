import io

def dataTrans():

    textFile = io.open('C:\\Users\\53238\\Desktop\\789_split.txt', 'w', encoding='utf-8')
    with open("C:\\Users\\53238\\Desktop\\789.txt" ,'r', encoding='utf-8') as f :
        num = 0
        strr = ''
        for line in f:
            strr += line
            if '\n' in line:
                num += 1
                if num % 10 == 0:
                    textFile.write(strr.replace('\n', ''))
                    textFile.write("\n")
                    strr = ''

dataTrans()