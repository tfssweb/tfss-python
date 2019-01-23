from WCCreator import *

class CSVWordCreator(WCCreator):
    titlename=''
    def __init__(self,fn,ignwl,ttn,ignor_blow_num):
        WCCreator.__init__(self,fn,ignwl,ignor_blow_num)
        self.titlename=ttn

    def get_frequent_words(self):
        csv_titleItems = pd.read_csv(self.filename, encoding='utf-8')[self.titlename]
        frequentWord=self.jieba_words(csv_titleItems)
        return frequentWord
