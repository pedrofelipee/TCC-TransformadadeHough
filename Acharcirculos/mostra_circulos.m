function [circimg] = mostra_circulos(img,himg, rbv)
imsize = size(img);
circ(1:imsize(1), 1:imsize(2)) = 0;
for rcont = 1:size(rbv,2)
    bwh = imbinarize(himg(:,:,rcont), 0.67);
    bwh = imdilate(bwh, ones(3, 3));
    bwh = imerode(bwh, ones(3, 3));
    bwh = bwlabel(bwh);
    stat = regionprops(bwh, 'Centroid');
    for c = 1:size(stat,1)
        centro = stat(c).Centroid;
        circ = circ + desenha_circulo(centro, rbv(rcont), imsize);
    end
end
circimg = im2double(img);
circimg(:,:,1) = circimg(:,:,1) + circ;
circimg(:,:,2) = circimg(:,:,2) + circ;
circimg(:,:,3) = circimg(:,:,3) + circ;
circimg = imadjust(circimg, [0 1], [0 1]);

