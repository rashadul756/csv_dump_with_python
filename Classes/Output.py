class OutputClass():

    def fail(self, data):
        data.to_csv('./Output/fail.csv', mode='a', header=False)

    def duplicate(self, data):
        data.to_csv('./Output/duplicate.csv', mode='a', header=False)

    def success(self, data):
    	data.to_csv('./Output/success.csv', mode='a', header=False)


output = OutputClass()