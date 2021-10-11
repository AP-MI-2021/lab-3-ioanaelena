#cea mai lunga subsecventa : 3. nr de semne alternative
def get_longest_alternating_signs(lst) :
    lst=[1,2,3,-4,-5,6,7,-8,12,13,9,10,54]
    #fie k=cea mai lunga subsecventa de nr pozitive si p pentru nr negative
    p=0
    max2=0
    max=0
    k=0
    for index in range (0,len(lst)-1) :
        for index2 in range (1,len(lst)) :
            if index>0 :
                if index2>0 :
                    k+=1
            if k>max :
                max=k
            if index<0 :
                if index2<0 :
                    p+=1
            if p>max2 :
                max2=p
    if max>max2 :
        return max
    else :
        return max2

def test_get_longest_alternating_signs() :
    assert get_longest_alternating_signs(1,2,3,-4,-5,6,7,-8,12,13,9,10,54) == [5]

#cea mai lunga subsecventa : 17. media nr nu depaseste o valoare citita
def get_longest_average_below(lst, average: float ) :
    lst=[2,5,8,1,3,4,6,7,9]
    n=80
    max=0
    for index in range (0,len(lst)) :
        nr=0
        nr2=0
        p=1
        while average<=n :
            p*=index
            nr+=1
            nr2+=1
            average=float(p/nr)
        if nr>max :
            max=nr
    index+=1

def test_get_longest_average_below()
    assert get_longest_average_below(2,5,8,1,3,4,6,7,9) == [3]






