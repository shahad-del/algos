tests = int(input())
results = []
for i in range(tests):
    words = input()
    if len(words) % 2 == 0:
        firstpart, secondpart = words[:len(words)//2], words[len(words)//2:]
        if (firstpart) == (secondpart) or firstpart == (secondpart)[::-1] or firstpart[::-1] == secondpart:
           results.append('yes')
        else:
           results.append('No') 
    elif len(words) % 2 != 0:
        y = len(words)//2
        firstpart,secondpart = words[:y],words[-y:]
        if (firstpart) == (secondpart) or firstpart == (secondpart)[::-1] or firstpart[::-1] == secondpart:
           results.append('yes')
        else:
           results.append('No')
for i in results:
    print(i)