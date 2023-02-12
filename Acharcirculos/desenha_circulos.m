function [circle] = desenha_circulos(centro, raio, tam_img)
dimx = tam_img(2);
dimy = tam_img(1);
circle(1:dimy, 1:dimx) = 0;
for theta=1:360
    pt = centro + raio * [cos(theta*pi/180)
        sin(theta*pi/180)];
    xp = pesquisa(pt(1), 1, dimx, 1);
    yp = pesquisa(pt(2), 1, dimy, 1);
    if ((xp ~= 0) & (yp ~= 0))
        circle(yp, xp) = 1.0;
    end
end

