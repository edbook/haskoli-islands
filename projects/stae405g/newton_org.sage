x = var('x');             # declare the variable for function
f(x)=x^2-1;        # change this to whatever function you like
df=diff(f,x);             # Sage will compute the derivative of f 
NewtonIt(x)=x-(f/df)(x);  # Newton's Iterative Formula which we are calling "NewtonIt"
n=4
p = 3
a = 0
b = 3
m=p
M=p
print 'x_0 =  %.4g' % p
allPlots = plot(f(x),(x,a,b))
allPlots +=text( '\n$x_{%d}$' % (0,),(p,0),color='red',vertical_alignment='top')
for i in range(n):
    pnew = N(NewtonIt(p))
    #allPlots += line([(p,f(x=p)),(pnew,0)],color='red',linestyle="-",thickness=0.5)
    allPlots += line([(a,df(x=p)*(a-pnew)),(b,df(x=p)*(b-pnew))],color='green',linestyle="-",thickness=0.5)
    allPlots += point((p,f(x=p)))
    allPlots += point((pnew,0))
    allPlots +=text( '\n$x_{%d}$' % (i+1,),(pnew,0),color='red',vertical_alignment='top')
    p = pnew
    m = min(m,p)
    M = max(M,p)
    print 'x_%d =  %.4g' % (i+1,p)

#allPlots += plot(f(x),(x,m,M))
show(allPlots)