from Function_operation import Operations



class Program:
    

    def main():
        file = open('Text.txt','rt')
        text = file.read()

        print("1.Хотите ли вы ввести значения K и N?\n2.Или используем данные по-умолчанию? ")
        number = int(input())
        if(number != 2):
            print("Введите значение K: ")
            K= int(input())
            print("Введите значение N: ")
            N= int(input())

        else:
            K=10
            N=4
        word = Operations.NumbersOfWords(text)
        print(word)
        Operations.AverageNumOfWordsInSent(text)    
        Operations.MedianeNum(text)
        print('\nПовторяющиеся буквенные N-грамы:')
        words_Dict = Operations.wordsDict(word,N)
        sorted_Dict = Operations.getsortedDict(words_Dict)
        Operations.printDict(sorted_Dict,K)
        
        

        

Program.main()