function [cont] = pesquisa(valor, a, n, d,varargin)
cont = ((valor - a)/d) + 1;
cont = round(cont);
if ((cont < 1) | (cont > n))
    if (nargin == 4)
        cont = 0;
    elseif (cont < 1)
        cont = 1;
    elseif (cont > n)
        cont = n;
    end
end
