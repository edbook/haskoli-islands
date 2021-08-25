function roundstd
  n = 10
  for i=0:n
    for j=0:i
      for k=0:j
        for l=0:k
          for m=0:0
            x = [i,j,k,l];
            a = norm(x);
            even = all(mod(x,2)==0);
            y = fliplr(x);
            if a == n, [y, a], end
          end
        end
      end
    end
  end
end