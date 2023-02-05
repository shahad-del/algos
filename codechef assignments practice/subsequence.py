index_of_subsequence = []
index_of_sequence = []

tests = int(input())
for i in range(tests):
    no_integers_sequence = int(input())
    numbers_in_sequence = list(map(str,input().split()))
    no_subsequence = int(input())
    numbers_in_subsequence= list(map(str,input().split()))
    for x in numbers_in_subsequence:
        if x in numbers_in_sequence:
            index_of_sequence.append(numbers_in_sequence.index(x))
            index_of_subsequence.append(numbers_in_subsequence.index(x))
        else:
            print('no')
    if (sorted(index_of_sequence) == index_of_sequence) and (sorted(index_of_subsequence) == index_of_subsequence) :
        print('yes')
    else:
        print('no')

    index_of_sequence = []
    index_of_subsequence = []