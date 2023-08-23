from decouple import  config
my_money = config('MY_MONEY',default = 1000,cast = int)