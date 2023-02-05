alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
tests = int(input())
for i in range(tests):
    str1 = input().lower()
    str2 = input().lower()
    
    if len(str1)== len(str2):
        # if '?' in str1 and '?' in str2:
            isvalid = False
            for i in range(len(str1)):
                if str1[i] == str2[i] or str1[i]=='?' and str2[i] != str1[i] or str1[i] == '?' and str2[i] == '?' or str1[i] != str2[i] and str2[i] == '?':
                    # print('yes')
                    isvalid = True
                else:
                    #  print('no')
                    isvalid= False
                    break
            if isvalid :
                print('NO')
            else:
                print('YES')