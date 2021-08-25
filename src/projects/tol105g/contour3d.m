function c = contour3d(C, z0, varargin)
  % CONTOUR3D(C, Z0) teiknar hæðarlínur fyrir "contour matrix" C í planinu z=z0.
  % CONTOUR3D(..., 'par', val,...) sendir 'par' og val áfram í plot3
  % C = CONTOUR3D(...) skilar vigri með handföngum á hæðarlínurnar
  hold on
  i = 1;
  k = 1;
  cm = rainbow;
  ncm = length(cm);
  zrange = getrange(C);
  while i < length(C)
    level = C(1,i);
    if isempty(zrange)
      color = 'k';
    else
      stdlevel = (level - zrange(1))/diff(zrange);
      colidx = 1 + stdlevel*(ncm - 1);
      color = interp1(1:ncm, cm, colidx);
    end
    n = C(2,i);
    x = C(1,i+(1:n));
    y = C(2,i+(1:n));
    i = i + n + 1;
    z = z0*ones(size(x));
    dnam = num2str(level);
    if k==1, dnam = "f(x,y) = " + dnam; end
    c(k) = plot3(x,y,z,'color',color, varargin{:},'DisplayName',dnam);
    lev(k) = level;
    k = k+1;
  end
  [~,I] = unique(lev);
  c = c(I);
end

function levrange = getrange(C)
  % skilar vigru með minnsta og stærsta level í C
  i = 1;
  levrange = [C(1,i), C(1,i)];
  while i < length(C)
    levrange(1) = min(levrange(1), C(1,i));
    levrange(2) = max(levrange(2), C(1,i));
    n = C(2,i);
    i = i + n + 1;
  end
end
