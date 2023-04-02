function plotspan()
  figure(1)
  clf
  set(gcf,'position',[50,500,700,700]);
  [X,Y,Z] = deal(3);
  lw = 3;
  ex = X*1.3;
  ey = Y*1.2;
  ez = Z*1.1;
  axis([0,X,0,Y,0,Z]);
  view(120,20);
  hold on
  box on
  set(gca,'linewidth',lw,'fontsize',24)
  grid on
  fs = 24;
  ax = gca();
  o = [0,0,0];
  finishbox()
  cosys();
  set(ax,'ticklen',[0,0.02])
  set(gca,'position',[0.13,0.11,0.74,0.80]);
  [PX,PY] = deal([0,X,X,0]);
  PZ = [0,0,Z,Z];
  patch(PX,PY,PZ,rgb('wheat'),'FaceAlpha',0.5, 'linew', lw)
  u = [1,1,0];
  v = [0,0,1];
  w = 3*u + 2*v;
  dx = 0.08;
  txt(u, "u", dx, dx, 'r');
  txt(v, "v", dx, 0, 'r');
  txt(w, "3u + 2v", dx, 0);
  or(u), or(v), or(w)
  set(gcf,'color','w')
  
  function txt(a, s, dx, dz, p)
    s = s + " = (" + a(1) + "," + a(2) + "," + a(3) + ")";
    if nargin == 4
      text(a(1), a(2) + dx, a(3) - dz, s, 'fontsize', fs);
    else
      text(a(1), a(2) - dx, a(3) - dz, s, 'fontsize', fs, 'horiz', 'right');
    end
  end
  
  function or(a)
    sh = [0.0001, 0, 0];
    arrow(sh, a + sh, 'color', rgb('darkred'), 'linew', 5);
  end
  
  function finishbox()
    plot3([X,X,0],[0,Y,Y],[Z,Z,Z],'k','linew',lw)
    plot3([X,Y],[X,Y],[0,Z],'k','linew',lw);
    ax.XTick = 0:X;
    ax.YTick = 0:Y;
    ax.ZTick = 0:Z;
  end
  
  function cosys()
    arrow(o, [ex, 0, 0], 'linew', lw);
    arrow(o, [0, ey, 0], 'linew', lw);
    arrow(o, [0, 0, ez], 'linew', lw);
    dd = 0.08;
    text(0, dd, ez+dd, 'z', 'fontsize',fs)
    text(0, ey-0.5*dd, -1.5*dd, 'y', 'fontsize', fs)
    text(ex+0.5*dd, 0, -1.5*dd, 'x', 'fontsize', fs)
  end
end