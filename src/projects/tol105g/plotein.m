function plotein(~)
  set(0,'defaultaxesticklabelinterpreter', 'latex');
  figure(1)
  clf
  set(gcf,'position',[300, -700, 750, 650]);
  axis equal
  [X,Y] = deal(3);
  lw = 3;
  if nargin > 0
    theta1 = pi/6;
    theta2 = theta1 + pi/2;
    a1 = [cos(theta1), sin(theta1)];
    a2 = [cos(theta2), sin(theta2)];
  else
    a1 = [1,0];
    a2 = [0,1];
  end
  ex = X*1.2;
  ey = Y*1.2;
  u = [2,3];
  axis([0,X*1.1,0,Y*1.1]);
  hold on
  set(gca,'defaulttextinterpreter','latex','defaulttextfontsize',36)
  set(gca,'linewidth',lw*0.8,'fontsize',36)
  grid on
  ax = gca();
  ax.YAxisLocation = 'origin';
  o = [0,0];
  cosys();
  set(ax, 'ticklen',[0.01, 0.01], 'tickdir', 'both')
  set(ax, 'units', 'centim')
  set(ax, 'position', [7,3,16,16]);
  set(ax, 'xtick', 0:X, 'ytick', 0:Y);
  axis(axis)
  LW = lw*1.6;
  or(o,a1,LW)
  or(o,a2,LW)
  or(o,u,LW)
  dx = 0.07;
  if nargin == 0
    dx = 0.07; dy = 0;
    text(a1(1)+dx, a1(2)+dy, "$e_1$", 'vert', 'bottom', 'horiz', 'left');
    text(a2(1)+dx, a2(2)+dy, "$e_2$", 'vert', 'bottom', 'horiz', 'left');
    text(0.5, u(2),"$u = (2,3) = 2e_1 + 3e_2$", 'vert', 'bottom')
  else
    dx1 = 0.07;
    dx2 = -0.07;
    s1 = '$a_1 = (\frac{\sqrt{3}}{2}, \frac{1}{2})$';
    s2 = '$a_2 = (-\frac{1}{2}, \frac{\sqrt{3}}{2})$';
    text(a1(1) + dx1, a1(2), s1, 'vert', 'mid', 'horiz', 'left');
    text(a2(1) + dx2, a2(2), s2, 'vert', 'mid', 'horiz', 'right');
    axis([-1.2,X*1.1,0,Y*1.1])
    R1 = a1*0.2;
    R2 = a2*0.2;
    Rx = [R1(1) R1(1)+R2(1) R2(1)];
    Ry = [R1(2) R1(2)+R2(2) R2(2)];
    plot(Rx, Ry, 'color', rgb('FireBrick'), 'linew', lw);
    text(u(1), u(2),"$u$", 'vert', 'bottom', 'horiz', 'center')
    set(ax, 'xtick', -1:X, 'ytick', 0:Y);
  end
  set(gcf,'color','w')
  function or(a, b, lw, c)
    d = (b - a)*(1 - 0.06/norm(b-a));
    if nargin < 4, c = rgb('firebrick'); end
    arrow(a, b, 'color', c, 'linew', 1, 'tipangle',20, 'length',20);
    arrow(a, a + d, 'color', c, 'linew', lw, 'ends', 'none');    
    %plot([a(1),b(1)], [a(2),b(2)], 'color', c, 'linew', lw);
  end
  
  function cosys()
    or(o, [ex, 0], lw, 'k');
    or(o, [0, ey], lw, 'k');
    dd = 0.04;
    text(3*dd, ey, "$y$", 'vert','mid','horiz','left')
    text(ex, dd, "$x$", 'vert','bot','horiz','center')
  end
end