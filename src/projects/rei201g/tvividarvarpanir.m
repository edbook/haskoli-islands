function a
  clf
  set(gcf, 'position', [115, 621, 1551, 275])
  x1 = [0 3 5 7 1 0];
  y1 = [4 4 0 0 12 12];
  x2 = [0 2.3 0];
  y2 = [5.4 5.4 10];
  x = [negrefl(x1) nan negrefl(x2)];
  y = [refl(y1) nan refl(y2)];
  x = x*0.8;
  y = y - 5.5;
  xy = [x;y];
  set(gcf, 'color', 'w')
  plt(xy, 1, 'Upphafleg mynd')
  plt(rot30(xy) + [0;1.3], 2, 'Snúningur um 45°');
  plt(scale(xy), 3, 'Skölun um 1.5 í x');
  plt(shear(xy), 4, 'Skekking um 25°');
  plt(rflctx(xy) + [0; 0.6], 5, 'Speglun um x-ás');
  tightaxis(1,5,[0 10 0 0])
end

function xy = rflctx(xy)
  A = [1 0; 0 -1];
  xy = A*xy;
end

function xy = shear(xy)
  a = 25;
  A = [1 sind(a); 0 1];
  xy = A*xy;
end

function xy = scale(xy)
  A = [1.5 0; 0 1];
  xy = A*xy;
end

function xy = rot30(xy)
  a = -45;
  A = [cosd(a) sind(a); -sind(a) cosd(a)];
  xy = A*xy;
end

function plt(xy, i, s)
  c = rgb('darkred');
  subplot(1,5,i);
  plot(xy(1,:), xy(2,:), 'color', c, 'linew', 3);
  axis([-8.5, 8.5, -7, 7]);
  axis off
  y = ylim(); y0 = y(1);
  text(0, y0, s, 'horiz', 'center', 'vert', 'mid', 'fontsize', 32, ...
    'fontw', 'bold', 'color', c);
end

function x = negrefl(x)
  x = [x -fliplr(x) x(1)];
end

function x = refl(x)
  x = [x fliplr(x) x(1)];
end
