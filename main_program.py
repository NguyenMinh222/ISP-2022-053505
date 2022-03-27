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
        words_dict = Operations.Dict_Words(word,N)
        sorted_dict = Operations.getsorted_dict(words_dict)
        Operations.show_dict(sorted_dict,K)
       

        

Program.main()
