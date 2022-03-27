from collections import Counter
import re
import statistics as st


class Operations:

    @staticmethod
    def NumbersOfWords(text):
        words=text.split()
        
        word_list=[]#тут наш список

        for word in words:
           clear_word = ""#в эту переменную помещаем только буквы
           for letter in word:
              if letter.isalpha():
                  clear_word += letter.lower()#превращаем все слова в нижний регистр

           word_list.append(clear_word)

        words1= Counter(word_list)
        return words1
   
    @staticmethod
    def AverageNumOfWordsInSent(text):
        text2 = re.sub(r'[.!?]\s',r'|',text)
        NumOfSent = len(text2.split('|'))
        AV= len(text.split())/NumOfSent
        return print('\nВ этом тексте {} предложения'.format(NumOfSent),'\n\nСреднее количество слов в предложении: ',round(AV,2))
    
    @staticmethod
    def MedianeNum(text):
        word_lens=[]
        for word in text.split():
            word_lens.append(len(word))
        medianenum=st.median(word_lens)
        return print("\nМедианное количество слов: ", medianenum)
    
    @staticmethod
    def Dict_Words(word,n):
        dict_words = {}
        for word111 in word:
            if len(word111)==n:
                if word111 in dict_words:
                    dict_words[word111] = dict_words[word111]+1
                else:
                    dict_words[word111]=1
        return dict_words

    @staticmethod
    def getsorted_dict(init_dict: dict):
        sorted_dict = dict(sorted(init_dict.items(),reverse=True,key=lambda x:x[1]))
        return sorted_dict

    @staticmethod
    def show_dict(dict,k):
        counter = 0
        for  kol in dict:
            if(counter<k):
                print(kol.ljust(20),dict[kol])
                counter=counter+1
 
   