class phone1 :
    def detail(self):
        print ('I am phone1')
class phone2(phone1):
    def details (self):
        print('I am phone2')

apple=phone2()
apple.detail()
apple.details()