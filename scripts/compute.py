import io

class SegmenterEvaluation :

    # 读入文件
    goldOffset = io.open('C:\\Users\\53238\\Desktop\\gold_offset.txt', 'r')
    participleOffset = io.open('C:\\Users\\53238\\Desktop\\response_offset.txt', 'r')
    # 写入文件
    reportFile = io.open('C:\\Users\\53238\\Desktop\\report.txt', 'w', encoding = 'utf-8')


    # 统计黄金标准单词个数，统计正确分词的个数
    def goldTotalCount(self):
        num = 0
        rightNum = 0
        participleNum = 0
        goldList = []
        participleList = []

        participleComputeList = []
        participleLineList = []
        for line in SegmenterEvaluation.participleOffset:
            # 分词list
            participleList = list(line.split(';'))
            participleLineList.append(participleList)
            participleNum = len(participleList)
            participleComputeList.append(participleNum)


        goldComputeList = []
        rightComputeList = []
        lineNum = 0
        for line in SegmenterEvaluation.goldOffset:
            # 黄金标准list
            goldList = list(line.split(";"))
            num = len(goldList)
            goldComputeList.append(num)
            # 对比黄金list和分词list
            rightNum = 0
            # line中的每个元组
            for goldIndex in goldList:
                participleList = participleLineList[lineNum]
                # 有问题，要找到对应line的index元组
                for participleIndex in participleList:
                    if participleIndex == goldIndex:
                        rightNum += 1
            rightComputeList.append(rightNum)
            lineNum += 1
        

        # 公式计算
        size = len(participleComputeList)
        recallList = []
        precisionList = []
        fScoreList = []
        errorScoreList = []
        for i in range(size):
            
            strr1 = "num: " + str(i) + '\n'
            goldTotalCount = goldComputeList[i]
            rightCount = rightComputeList[i]
            errorCount = participleComputeList[i] - rightCount
            # errorCount = goldComputeList[i] - rightCount
            # print("goldTotalCount: " + str(goldTotalCount) + ", " + "rightCount: " + str(rightCount) + ", " + "errorCount: " + str(errorCount))
            strr2 = "goldTotalCount: " + str(goldTotalCount) + ", " + "rightCount: " + str(rightCount) + ", " + "errorCount: " + str(errorCount) + '\n'

            recallScore = rightCount / goldTotalCount
            precisionScore = rightCount / (rightCount + errorCount)
            fScore = (2*precisionScore*recallScore) / (precisionScore + recallScore)
            errorScore = errorCount / goldTotalCount
            recallList.append(recallScore)
            precisionList.append(precisionScore)
            fScoreList.append(fScore)
            errorScoreList.append(errorScore)

            # print("recallScore: " + str(recallScore) + ", " + "fScore: " + str(fScore) + ", " + "errorScore: " + str(errorScore))
            strr3 = "recallScore: " + str(recallScore) + ", " + "precisionScore: " + str(precisionScore) + ", "+ "fScore: " + str(fScore) + ", " + "errorScore: " + str(errorScore) + '\n'

            SegmenterEvaluation.reportFile.write(strr1)
            SegmenterEvaluation.reportFile.write(strr2)
            SegmenterEvaluation.reportFile.write(strr3)

        # 计算平均召回率、精准率、平均分值、平均错误率
        recallSum = 0
        precisionSum = 0
        fScoreSum = 0
        errorSum = 0
        for i in range(size):
            recallSum += recallList[i]
            precisionSum += precisionList[i]
            fScoreSum += fScoreList[i]
            errorSum += errorScoreList[i]
        recallAvg = recallSum / size
        print(recallAvg)
        precisionAvg = precisionSum / size
        print(precisionAvg)
        fScoreAvg = fScoreSum / size
        print(fScoreAvg)
        errorAvg = errorSum / size
        print(errorAvg)

a = SegmenterEvaluation ()
a.goldTotalCount()