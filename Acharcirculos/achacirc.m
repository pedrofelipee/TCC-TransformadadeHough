
rbv = 1
dist = 40
im = imread('teste2.png');
figure(1);
subplot(1,3,1);
imshow(im);
title('Imagem Original');
imc = rgb2gray(im);
subplot(1,3,2);
imshow(imc);
title('Tons de Cinza');
limiar = [0.1 0.45];
imb = edge(im(:,:,1), 'canny', limiar);
subplot(1,3,3);
imshow(imb);
title('Bordas');
xbv = 1:dist:size(imb, 2);
ybv = 1:dist:size(imb, 1);
himg = thc(imb, xbv, ybv, rbv);
figure(2);
contourf(himg(:,:,1)); colorbar;
title('Projecao da THC');
figure(3);
surfc(himg(:,:,1));


