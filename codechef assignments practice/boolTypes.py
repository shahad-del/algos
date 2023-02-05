int('5')

bool('True') = True
bool('0') = False
bool('') = False

bool('34234') = True
bool([]) = False # test this
bool({}) = False # test this
bool(()) = False # test this

bool([1]) = True 
bool({1: 34}) = True
bool((1)) = True                                                                             
bool(['-1','2']) = True
bool([0,0,0]) = True


all([0,0,0]) = False
all([1,1,0]) = False