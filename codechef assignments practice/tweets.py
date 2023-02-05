tweets,clicks = map(int,input().split())
n = tweets
my_lists = list([0]*tweets)
print(my_lists)
for i in range(clicks):
        # user_input = str(input())
        for i in range(clicks):
                user_input = (input('').split())
                # user_input.split()
                if user_input[0].upper() == 'CLOSEALL':
                        print('0')
                        my_lists = list([0]*tweets)#list(0*len(my_lists))
                        # for i in my_lists:
                        #         i = 0
                        continue
                position = int(user_input[1])
                try:
                        if my_lists[position-1]== 0:
                                my_lists[position-1]=1
                        else:
                                my_lists[position-1]=0
                        
                except(IndexError):
                        print('tweet does not exist')#
                except Exception as e:
                        print('unexpected error', e.__class__)

                # # my_lists[user_input-1] = 0 if my_lists[user_input-1] is 1 else 0
                # number = 1
                count = 0
                for i in my_lists:
                        if i == 1:
                                count +=1
                        # number_of_ones = my_lists.count(1)
                print(count, my_lists)


