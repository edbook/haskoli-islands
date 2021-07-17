# Nál af einingarlengd er hent á blað með tveimur samsíða línum
# og lengdin á milli línanna er 1.
# Gefið að miðja nálarinnar lendi á milli línanna, hverjar eru líkurnar
# á að nálin öll lendi á milli línanna?
# 
# Hendum n nálum að handahófi og athugum. Hvert kast ákvarðast
# af miðju nálarinnar u (af samhverfu ástæðum er nóg að hugsa um að 
# miðjan lendi á bilinu [0,0.5]) og hornið v sem er á bilinu [0,pi/2]
#
# Nálin lendir á milli línanna ef 
#       2u <= sin(v)
#
# Sjá nánar http://en.wikipedia.org/wiki/Buffon%27s_needle

n=1000;
u = rand(1,n)/2;
v = rand(1,n)*pi/2;

p = sum(2*u <= sin(v))/n # rétt svar er 2/pi, sem er u.þ.b. 0.63662
