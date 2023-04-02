% Þýða letterdef.txt yfir í letters.txt
% Snið letterdef.txt:
% A
% x1 x2...
% y1 y2...
% cx cy radíus theta1 theta2
% cx cy radíus theta1 theta2
%   (bókstafur, x,y-hnit strika, bogar)
% B
% ...
[x,y] = deal({});
f = fopen('letterdef.txt');
fo = fopen('stafrof.txt', 'w');
lin = fgetl(f);
k = 0;
broddstafir = 'ÁÉÍÓÚÝ';
while true
  %if isempty(lin), continue, end
  assert(isletter(lin(1)))
  if lin == "acute"
    xacute = str2num(fgetl(f));
    yacute = str2num(fgetl(f));
    lin = fgetl(f);
    if isempty(lin), lin = fgetl(f); end
  end
  k = k + 1;
  letter(k) = lin(1);
  x{k} = str2num(fgetl(f));
  y{k} = str2num(fgetl(f));
  assert(length(x)==length(y));
  if feof(f), break, end
  lin = fgetl(f);
  while ~isempty(lin) && ~isletter(lin(1))
    arc = str2num(lin);
    [cx, cy, r, a1, a2] = matsplit(arc);
    a = linspace(a1, a2, ceil(a2-a1));
    X = cx + r*cosd(a);    
    Y = cy + r*sind(a);
    x{k} = [x{k} nan X];
    y{k} = [y{k} nan Y];
    if feof(f), break, end
    lin = fgetl(f);
  end
  j = find(letter(k) == 'AEIOUY');
  if ~isempty(j)
    k = k + 1;
    letter(k) = broddstafir(j);
    x{k} = [x{k-1} nan xacute];
    y{k} = [y{k-1} nan yacute];
  end
  if feof(f), break, end
  if isempty(lin), lin = fgetl(f); end
end
fclose(f);

for k=1:length(letter)
 fprintf(fo, '%s\n', letter(k));
 fprintf(fo, '%.4f ', x{k}); fprintf(fo, '\n');
 fprintf(fo, '%.4f ', y{k}); fprintf(fo, '\n');
end
fclose(fo);
