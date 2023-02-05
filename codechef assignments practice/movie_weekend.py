tests = int(input())
first_list = []
for i in range (tests):
    no_of_movies = int(input())
    length_of_movies = list(map(int,input().split()))
    rating_of_movies = list(map(int,input().split()))
    for  i in range(len(length_of_movies)):
        first_list.append(length_of_movies[i]*rating_of_movies[i])
    sorted_list = sorted(first_list)
    if sorted_list.count(sorted_list[-1]) == 1:
        index = first_list.index(sorted_list[-1])
        print(index+1)
    elif sorted_list.count(sorted_list[-1]) > 1:
        sorting_list = sorted(rating_of_movies)
        if sorting_list.count(sorting_list[-1]) == 1:
            know_index = rating_of_movies.index(sorting_list[-1])
            print(know_index+1)
        else:
            maximum_no = max(rating_of_movies)
            known_index = rating_of_movies.index(maximum_no)
            print(known_index +1)



