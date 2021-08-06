# Reiknar rúmmálið af hlutunum í [0,1]x[0,1]x[0,1] í R^3
# sem uppfyllir bæði
#          x^2 + sin(y)<=z   (f)
#          x-z+exp(y)<=1     (g)
# Skilgreinum n punkta í [0,1]^3 af handahófi
n=1000;

x = rand(1,n);
y = rand(1,n);
z = rand(1,n);

# n-vigur þar sem x^2+sin(y)<=z er uppfyllt (1 satt, 0 ósatt)
f = (x.^2 + sin(y)<=z);
# n-vigur þar sem x-z+exp(y)<=1 er uppfyllt (1 satt, 0 ósatt)
g = (x-z+exp(y)<=1);

# f&g er vigur þeirra sem punkta sem uppfylla bæði skilyrðin,
# hlutfalla þeirra margfaldað við rúmmál tenginsins (sem er 1) gefur okkur
# rúmmál hlutarins
V = sum(f & g)/n
