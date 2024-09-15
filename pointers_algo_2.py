seq = input()



dict_quotes = {')': '(',']': '[','}': '{'}


stack = []

answer = 'yes'

for symbol in seq:

    if symbol in dict_quotes.values():
    
        stack.append(symbol)

    else:
    
        if not stack or stack[-1] != dict_quotes[symbol]:
        
            answer = 'no'
            
            break
         
        else:
             
            stack.pop()


if stack:

    answer = 'no'


print(answer)

new_stack = []

        



          


                  
    
    
    

    
    

            


    
    