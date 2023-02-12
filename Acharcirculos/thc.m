function [himg] = thc(imb, xbv, ybv, rbv)
xnb = size(xbv, 2);
ynb = size(ybv, 2);
rnb = size(rbv, 2);
xa = xbv(1);
ya = ybv(1);
xd = xbv(2) - xa;
yd = ybv(2) - ya;
[linhas, colunas] = find(imb);
acumuladorTH(1:ynb, 1:xnb, 1:rnb) = 0;
for bcont = 1:size(linhas, 1)
    xp = colunas(bcont);
    yp = linhas(bcont);
    for rcount = 1:rnb
        raio = rbv(rcount);
        rsqr = raio * raio;
        xinic = pesquisa(xp-(raio/sqrt(2)), xa,xnb, xd, 1);
        xfim = pesquisa(xp+(raio/sqrt(2)), xa,xnb, xd, 1);
        yinic = pesquisa(yp-(raio/sqrt(2)), ya,ynb, yd, 1);
        yfim = pesquisa(yp+(raio/sqrt(2)), ya,ynb, yd, 1);
        for xcont = xinic:xfim
            xc = xbv(xcont);
            xsqr = (xp - xc)*(xp - xc);
            if (rsqr >= xsqr)
                ysqrt = sqrt(rsqr - xsqr);
                yc = yp + ysqrt;
                ycount = pesquisa(yc, ya, ynb, yd);
                if (ycount ~= 0)
                    acc_count = acumuladorTH(ycount,xcont, rcount);
                    acumuladorTH(ycount, xcont, rcount)= acc_count + 1;
                end
                yc = yp - ysqrt;
                ycount = pesquisa(yc, ya, ynb, yd);
                if (ycount ~= 0)
                    acc_count = acumuladorTH(ycount,xcont, rcount);
                    acumuladorTH(ycount, xcont, rcount)= acc_count + 1;
                end
            end
        end
        for ycont = yinic:yfim
            yc = ybv(ycont);
            ysqr = (yp - yc)*(yp - yc);
            if (rsqr >= ysqr)
                xsqrt = sqrt(rsqr - ysqr);
                xc = xp + xsqrt;
                xcont = pesquisa(xc, xa, xnb, xd);
                if (xcont ~= 0)
                    acc_count = acumuladorTH(ycont,xcont, rcount);
                    acumuladorTH(ycont, xcont, rcount)= acc_count + 1;
                end
                xc = xp - xsqrt;
                xcont = pesquisa(xc, xa, xnb, xd);
                if (xcont ~= 0)
                    acc_count = acumuladorTH(ycont,xcont, rcount);
                    acumuladorTH(ycont, xcont, rcount)= acc_count + 1;
                end
                
            end
        end
    end
end
for rcount = 1:rnb
    himg(:, :, rcount) = imresize(acumuladorTH(:, :, rcount), yd, 'bicubic');
    himg(:, :, rcount) = himg(:, :,rcount)/max(max(himg(:, :, rcount)));
end
