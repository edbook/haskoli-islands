var ('x y r n'); r = 1; inside = 0; points = []
n = 100  ## Try changing this! This is the number of shots the estimate is based on
### Shoot randomly into the square:
for i in range(0,n):
    [x,y]=[random(),random()]
    points.append([x,y])
    
### If a shot lands inside the circle, make a note of it
    if (y <= sqrt((r^2)-(x^2))):
        inside += 1
        
### Approximate pi based on the fraction of shots that landed in the circle
### Area of circle = pi*r^2; Area of square = (2*r)^2 = 4*r^2
### Shots in circle / Shots in square = (pi*r^2)/(4*r^20 = pi()/4
piapprox = 4*(inside / n)
estimate = "Með því að nota "
estimate += str(n)
estimate += " punkta, fæst að pi er um það bil "
estimate += str(piapprox.n())
show(estimate)
### Graph the solution
circle = []
for i in range(0,1000):
    x = i/1000
    y = sqrt((r^2)-(i/1000)^2)
    circle.append([x,y])
graph = list_plot(points)
graph += list_plot(circle,color='red',figsize=[5,4],plotjoined=true)
show(graph)

