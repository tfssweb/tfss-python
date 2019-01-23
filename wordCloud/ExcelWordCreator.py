from WCCreator import *

class ExcelWordCreator(WCCreator):
    titlename=''
    def __init__(self,fn,ignwl,ttn,ignor_blow_num):
        WCCreator.__init__(self,fn,ignwl,ignor_blow_num)
        self.titlename=ttn

    def get_frequent_words(self):
        excel_titleItems = pd.read_excel(self.filename, encoding='utf-8')[self.titlename]
        frequentWord=self.jieba_words(excel_titleItems)
        return frequentWord
