import dataGetter

class nnDataCreator:

    global getter
    global data
    global trainData
    global testData
    global new_data
    global keys

    def __init__(self, ticker):
        self.getter = dataGetter.dataGetter(ticker)
        self.getter.getData()
        self.data = self.getter.retData()
        self.trainData = [{}]
        self.testData = [{}]
        self.keys = []
        for i in self.data:
            self.keys.append(i)

    def trainTestDataCreator(self):
        data = self.data
        trainDataLen = int(len(data)*0.8)
        testDataLen = int(len(data)*0.2)

        for i in range(trainDataLen):
            tempdict = {}
            for j in data:
                tempdict[j] = data[j][i]
            self.trainData.append(tempdict)

        for i in range(testDataLen, len(data)):
            tempdict = {}
            for j in data:
                tempdict[j] = data[j][i]
            self.testData.append(tempdict)

        print("[+]Created trainData and testData")

    def new_dataCreator(self):
        self.new_data = []
        data = self.trainData
        for i in range(len(data)-7):
            tempdict = {}
            templist = []
            for j in range(7):
                for k in data[j]:
                    templist.append(data[i+j][k])
            tempdict['label'] = templist
            templist = []
            for k in data[i]:
                templist.append(data[i+7][k])
            tempdict['target'] = templist
            self.new_data.append(tempdict)

        for i in self.new_data:
            print("----------------------")
            print(i)

abc = nnDataCreator('BSLGOLDETF')
abc.trainTestDataCreator()
abc.new_dataCreator()
