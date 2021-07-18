def bracketing(a,f,s=0.01,m=2):
    b = a + s

    fa=f(a)
    fb=f(b)
    if fa > fb :
        c=b+s
        fc=f(c)
        while fc < fb :
                fb=fc
                b=c
                s=s*m
                c=c+s
                fc=f(c)
        bracketing =[a,c]
        
    
    if fb > fa:
            a=b-s
            c=a-s
            fc=f(c)
            while fc < fa :
            
                    fa=fc
                    a=c
                    s=s*m
                    c=c-s
                    fc=f(c)
                    
            bracketing = [c,b]

    return bracketing

f= lambda x:(x+2)**2
b= bracketing(1,f)
print (b)