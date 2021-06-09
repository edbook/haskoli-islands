n=1000;
x=2*rand(n,1); % Veljum n punkta af handahófi á bilinu [0,2]
f=@(x) x.^2 - x.^3/2 + x/10;
medf = sum(f(x))/n; % Meðalgildi f
heildi = medf*2 % Heildið er margfeldi meðalgildisins og billengdarinnar
