from datetime  import datetime

hour=datetime.now().hour
if 6<=hour<=9:
    print("Good moring")
elif 10<=hour<=13:
    print("Good afternoon")
elif 15<=hour<=16:
    print("Good eve")
elif 21<=hour<=24:
    print("Good night")
else:
    print("your not on earth")