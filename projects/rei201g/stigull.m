%stigul_skyring()
clf
synidaemi()
set(gcf,'color','w')
shg

function synidaemi()
  z0 = -8;
  azim = -15;
  elev = 20;
  f = @(x,y) x.^2 + x.*y + y.^2 - 3*x;
  x = linspace(-3, 7, 100);
  y = linspace(-6, 4, 100);
  Z = flotur(f, x, y, z0, azim, elev);
  c = contours(x, y, Z, 6, z0);
  legend(c, 'location', 'SouthEastOutside', 'autoupdate', 'off')
  pt3d(2,-1,-8,'color', 'k', 'markersize', 40)
  txt3d(2,-1,-7.8,'p ','color','k','fontsize',22,'vert','mid','horiz','right')
end

function stigul_skyring()
  z0 = 0;
  azim = -25;
  elev = 30;
  f = @(x,y) 2 + 3*x.*exp(-x.^2-y.^2);
  [x,y] = deal(linspace(-2,2,100));
  Z = flotur(f, x, y, z0, azim, elev);
  c = contours(x,y,Z,9,z0);
  [ar,lin] = orvar(f, 0.6);
  set(ar, 'DisplayName', 'stigull')
  set(lin, 'DisplayName', 'snertill')
  set(ar, 'visible', 'on')
  lg = legend([c, ar, lin], 'fontsize', 16);
  set(lg, 'linewidth', 1, 'location', 'southeastoutside', 'autoupdate', 'off');
  text(-2.5,2,4.4,'f(x,y) = 2 + 3x exp(–x² – y²)     ', 'fontsize', 25)
end

function Z = flotur(f, x,y, z0, azim, elev)
  clf  
  [X,Y] = meshgrid(x,y);
  Z = f(X,Y);
  surfl(x,y,Z);
  z1 = gca().ZLim(2);
  e = [min(x), max(x), min(y), max(y), z0, z1];
  colormap(gray)
  shading interp
  hold on
  border(X, Y, Z, 2.0)
  axis(e);
  setax(z0, azim, elev);
  box on
end

function c = contours(x,y,Z, n, z0)
  %[X,Y] = meshgrid(x,y);
    lev = roundticks(Z, 'inside', n);
  C = contourc(x,y,Z,lev);
  c = contour3d(C, z0, 'linewidth', 2.5);
end

function border(X,Y,Z,lw)
  % Plot thicker line at border of surface
  function cf = circfer(x)
    cf = [x(1,:) x(:,end)' fliplr(x(end,:)) flipud(x(:,1))'];
  end
  cx = circfer(X);
  cy = circfer(Y);
  cz = circfer(Z);
  plot3(cx,cy,cz,'k','linew',lw)
end

function setax(z0, azim, elev)
  % adjust axes settingsx
  ax = gca();
  ax.FontSize = 16;
  xlabel('x', 'fontsize', 20);
  ylabel('y', 'fontsize', 20);
  grdclr = 0.3;
  ax.GridColor = grdclr*[1 1 1];
  ax.GridAlpha = grdclr;
  ax.LineWidth = 2.0;
  ax.TickLength = [0.01, 0.01];
  ax.View = [azim, elev];
  e = axis();
  ax.XTick = e(1):e(2);
  ax.YTick = e(3):e(4);
  ax.ZTick = e(5):4:e(6);
end

function [ar,lin] = orvar(fun, a)
  blue = rgb('MediumBlue');
  syms x y t
  syms p [1 2]
  z = zlim();
  z = [0,4];
  f(x,y) = fun(x,y);
  c = 2.6;
  b = solve(f(a,y) - c);
  b = double(b(b<0));
  fp = f(a,b);
  g = gradient(f);
  gp = g(a,b);
  u = gp/norm(gp);
  L(t) = fp + dot(gp,u)*t;
  tz(1) = solve(L(t) - z(1));
  tz(2) = solve(L(t) - z(2));
  %t2 = solve(L(t) - z(2));
  px = a + tz*u(1);
  py = b + tz*u(2);
  axlim = axis();
  lin = plot3(px, py, z+0.007, 'color', blue, 'linew', 3.5);
  set(lin, 'clipping', 'off');
  axis(axlim)
  pt3d(a,b,fp, 'color', blue, 'markersize',40)
  pt3d(a,b,0.0001, 'color', blue, 'markers', 40);
  p = double([a,b,0.01]);
  pg = double([gp', 0.01]);
  mag = rgb('dodgerblue');
  arrow(p, p + pg, 'linew', 1, 'color', mag, 'length',14, 'tipangle', 22, 'baseangle',60);
  arrow(p, p + pg, 'linew', 4, 'color', mag, 'length',0);
  ar = plot3(a,b,0, 'linew', 4, 'color', mag);
  set(gcf,'defaulttextfontsize', 25);
  %set(gcf,'defaulttextInterpreter', 'latex');
  txt3d(a,b,0,'p = (a,b) ','vert', 'mid', 'horiz', 'right', 'fontw', 'bold')
  txt3d(a+0.02,b,fp,' (a,b,f(p))', 'vert', 'mid', 'horiz', 'left', 'fontw', 'bold')
  a,b,'gradient:',double(gp)
end

function pt3d(x, y, z, varargin)
  % Plot a point slightly towards camera
  cp = get(gca,'CameraPosition');
  p = [x,y,z];
  r = 0.1*(cp - p)/norm(cp - p);
  plot3(x+r(1), y+r(2), z+r(3), '.', varargin{:});
end

function txt3d(x, y, z, txt, varargin)
  cp = get(gca,'CameraPosition');
  p = [x,y,z];
  r = 0.5*(cp - p)/norm(cp - p);
  tx=text(x+r(1), y+r(2), z+r(3), txt, varargin{:});
  set(tx,'clipping', 'off')
end