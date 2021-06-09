var('x')
@interact
def _(f = -x^2/3+1, a = float(0), b = float(1), x0 = 0, N=(5,(1..10))):
	allPlots = plot( f(x), (x, a, b) )
	allPlots += plot( x, (x, a, b), color = 'black')
	steps = 0
	while steps<N:
		allPlots += line([(x0,x0),(x0,f(x=x0))], color='red', linestyle = "-.", thickness=3)
		allPlots += list_plot( [(x0,f(x=x0))] , size = 50)
		allPlots += line([(x0,f(x=x0)), (f(x=x0),f(x=x0))], color='red', linestyle = "-.", thickness=3)
		allPlots += list_plot( [ (f(x=x0) , f(x=x0)) ] , size = 50)
		steps = steps+1
		x0=f(x=x0)
	show(allPlots)
