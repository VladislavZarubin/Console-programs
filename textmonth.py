# function declaration 
def get_month(language, number):
    '''This function gets language and number of month and return month name'''
    ru =['январь', 'февраль', 'март', 'апрель','май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    en =['january', 'february', 'march', 'april','may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    if language == 'en':
        return en[number-1]
    if language == 'ru':
        return ru[number-1]

# data input
lan = input()
num = int(input())

# call function
print(get_month(lan, num))
