temp = int(input())
string = input()
string = "".join(sorted(string))
n = len(str(int(string)))
n = temp - n
print(string[n] + "0"*n + "".join(string[n+1:]))
        
    