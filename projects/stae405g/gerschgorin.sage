# Benedikt Magnusson, 2016. CC-BY-SA.

from scipy import linalg
#pretty_print(html('<h2>Skífusetning Gerschgorins</h2>'))
@interact
def Gerschgorin(Ain = input_box(default='[[10,1,1/10,0],[-1,9,0,1],[1,0,2,3/10],[-.5,0,-.3,1]]', type = str,width=40, label = 'A = '),rows=checkbox(True, label='Línugeisli (blátt)'),cols=checkbox(False, label='Dálkgeisli (rautt)')):
    A = sage_eval(Ain)
    size = len(A)
    pretty_print(html('$A = ' + latex(matrix(RealField(10),A))+'$'))
    A = matrix(RealField(10),A)

    centers = [(real(q),imag(q)) for q in [A[i][i] for i in range(size)]]
    radii_row = [sum([abs(A[i][j]) for j in range(i)+range(i+1,size)]) for i in range(size)]
    radii_col = [sum([abs(A[j][i]) for j in range(i)+range(i+1,size)]) for i in range(size)]
    x_min = min([centers[i][0]-radii_row[i] for i in range(size)]+[centers[i][0]-radii_col[i] for i in range(size)])
    x_max = max([centers[i][0]+radii_row[i] for i in range(size)]+[centers[i][0]+radii_col[i] for i in range(size)])
    y_min = min([centers[i][1]-radii_row[i] for i in range(size)]+[centers[i][1]-radii_col[i] for i in range(size)])
    y_max = max([centers[i][1]+radii_row[i] for i in range(size)]+[centers[i][1]+radii_col[i] for i in range(size)])

    eigs = [CDF(x) for x in linalg.eigvals(A.numpy())]
    eigpoints = points([(real(q),imag(q)) for q in eigs],pointsize = 17, rgbcolor = (0,0,0),legend_label='Eigingildi')
    centers = [(real(q),imag(q)) for q in [A[i][i] for i in range(size)]]
    centerpoints = points(centers,pointsize=20,marker='*',rgbcolor = (1,0,1),legend_label=u'Miðja')
    ft = eigpoints+centerpoints
    radii_row = [sum([abs(A[i][j]) for j in range(i)+range(i+1,size)]) for i in range(size)]
    radii_col = [sum([abs(A[j][i]) for j in range(i)+range(i+1,size)]) for i in range(size)]
    scale = max([(x_max-x_min),(y_max-y_min)])
    scale = 7/scale
    row_circles = sum([circle(centers[i],radii_row[i],fill=True, alpha = .3) for i in range(size)])
    col_circles = sum([circle(centers[i],radii_col[i],fill=True, rgbcolor = (1,0,0), alpha = .3) for i in range(size)])
    if cols:
        ft = ft + col_circles
    if rows: 
        ft = ft + row_circles
    ft.show()
    
#show(html("<a rel='license' href='http://creativecommons.org/licenses/by-sa/3.0/'><img alt='Creative Commons License' height='15' style='border-width:0' src='https://i.creativecommons.org/l/by-sa/3.0/80x15.png' /></a> by <a href='http://wiki.sagemath.org/interact/calculus#Root_Finding_Using_Bisection'>William Stein</a>"))
