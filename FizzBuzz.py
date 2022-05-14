for num in range(1, 101):
    string = ''

    # ここから記述

    # 15の倍数
    if (num % 3) == 0 and (num % 5) == 0:
        string = "FizzBuzz"

    # 5の倍数
    elif (num % 5) == 0:
        string = "Buzz"

    # 3の倍数
    elif (num % 3) == 0:
        string = "Fizz"

    # それ以外  
    else:
        string = str(num)
    
    # ここまで記述

    print(string)