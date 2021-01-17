'''
N школьников делят K яблок поровну, не делящийся остаток остается в корзинке.
Сколько яблок достанется каждому школьнику?
'''
number_of_schoolboys = int(input())
number_of_an_apple = int(input())

print(number_of_an_apple % number_of_schoolboys)
