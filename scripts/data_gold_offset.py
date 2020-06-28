import io
import re

def dataOffset():

    goldOffset = io.open('C:\\Users\\53238\\Desktop\\gold_offset.txt', 'w', encoding='utf-8')
    with open("C:\\Users\\53238\\Desktop\\gold_split_remake.txt" ,'r', encoding='utf-8') as f :
        for line in f:
            # 计算offset
            startPosition = 0
            endPosition = 0

            offsetList = []
            for index in line:
                endPosition += 1
                if index == ' ':
                    # 记录start与end
                    offset = str(startPosition) + ',' + str(endPosition)
                    offsetList.append(offset)
                    # 复位
                    startPosition = endPosition
                    endPosition -= 1
            inputStr = ';'.join(offsetList)
            goldOffset.write(inputStr)
            goldOffset.write('\n')
dataOffset()