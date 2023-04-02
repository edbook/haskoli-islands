m = 500;
C = 1/500;
n = 100;
n = 200;
m = m*C;
n = n*C;
F1 = 3000;
F2 = -2500;
f = [zeros(1,5), F1*ones(1,10),F2*ones(1,15),zeros(1,20)];
%f = 1000*ones(1,10);
f = f*C;
A = [1 1; 0 1-n/m];
B = [0; 1/m];
tmax = length(f);
Ah = A^2;
Bh = [0 1;1 0.6];
xh = [0 0]';
for k = 1:tmax/2
  t = 2*k;
  u = [f(t) f(t-1)]';
  xh(:,end+1) = Ah*xh(:,end) + Bh*u;
end
x = [0 0]';
for t=1:tmax
  x(:,end+1) = A*x(:,end) + B*f(t);
end
p = x(1,:);
v = x(2,:);
T = 0:tmax;
set(gcf,'defaultaxesfontsize',27,'defaultaxeslinewidth',2)
set(gcf,'defaultlinelinewidth',4);
T1 = [0,5, 5,15,15,30,30,50];
f1 = [0,0,F1,F1,F2,F2, 0, 0];

subplot(1,3,1), plot(T1,f1/1000); ylim([-3, 3.5]);
grid on; xlabel('tími (s)'); ylabel('kraftur (kN)')
set(gca,'ytick',-3:3);

subplot(1,3,2), plot(T,p); ylim([-100,250]);
grid on; xlabel('tími (s)'); ylabel('staðsetning (m)')
set(gca,'ytick', -100:50:250);

subplot(1,3,3), plot(T,v); %axis([0,50,-30,30])
grid on; xlabel('tími (s)'); ylabel('hraði (m/s)');
%set(gca,'ytick',-30:10:30);

set(gcf,'color','w')
tightaxis(1,3,20,10)