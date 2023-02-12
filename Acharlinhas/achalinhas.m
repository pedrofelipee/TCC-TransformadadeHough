
im = imread('imagem1.png');
im = rgb2gray(im);
im = double(im)/255; 


figure(1)
imb = edge(im);
imshow(imb);
title ('Imagem original')
theta = (0:179)';
[R,xp] = radon(imb, theta);


figure(2)
imagesc(theta,xp,R), colorbar;
xlabel ('theta (graus)'), ylabel ('rho (pixels do centro)')
title('Dominio da TH');
plt=1;
