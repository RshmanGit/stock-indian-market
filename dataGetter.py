import quandl
import datetime
import pickle

class dataGetter:

    global key
    global ticker

    def __init__(self,ticker):
        with open('../apiKey.txt','r') as keyfile:
            self.key = keyfile.read().replace('\n','')
        self.ticker = ticker

    def getData(self):
        global data
        quandl.ApiConfig.api_key = self.key
        date = datetime.datetime.now()
        enddate = ("%s-%s-%s" % (date.year,date.month,date.day))
        ticker = 'NSE/'+self.ticker
        try:
            print('[+] Quandl request')
            self.data = quandl.get(ticker , start_date='2011-05-14', end_date=enddate)
            print('[+] Quandl request pulled')

        except:
            print('[-] Quandl request failed')

        try:
            filename = '../'+self.ticker+'rawdata.p'
            print('[+] Dumping data to pickle file: ')
            pickle.dump(self.data, open(filename,'wb'))
            print('[+] Dumping data success')

        except:
            print('[-] Dumping failed')

    def retData(self):
        filename = '../'+self.ticker+'rawdata.p'
        data = []
        try:
            print('[+] Loading data from pickle file: ')
            data = pickle.load(open(filename,'rb'))
            print('[+] Data loaded')
        except:
            print('[-] Loading data failed')

        return data
