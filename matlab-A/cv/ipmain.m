clear all; close all; clc

%%img load
rgbimg = imread('./mandrill.png');
%display
figure(1);
imshow(rgbimg);
title('Mandraill IMG')

[r,c] = size(rgbimg,[1,2]);

%%HST
figure (2);
grayimg = imread('pout.tif');
subplot(1,2,1); imshow(grayimg); title('original');
subplot(1,2,2); imhist(grayimg); title('hist org');

enhanced = histeq(grayimg);

figure(3);
subplot(1,2,1); imshow(enhanced); title('enhanced');
subplot(1,2,2); imhist(enhanced); title('hist enhanced');

gray = rgb2gray(rgbimg);

H = [-1 0 1;
    -1 0 1;
    -1 0 1];

H1 = H';

H2 = fspecial('gaussian', [15,15],10);

M = conv2(gray, H);

figure(4);
subplot(1,2,1); imshow(gray); title('gray');
subplot(1,2,2); imshow(abs(M),[]); title('converged');

M1 = conv2(gray, H1);

figure(5);
subplot(1,2,1); imshow(gray); title('gray');
subplot(1,2,2); imshow(abs(M1),[]); title('converged');

M = conv2(gray, H);

figure(4);
subplot(1,2,1); imshow(gray); title('gray');
subplot(1,2,2); imshow(abs(M),[]); title('converged');

M2 = conv2(gray, H2);

figure(6);
subplot(1,2,1); imshow(gray); title('gray');
subplot(1,2,2); imshow(abs(M2),[]); title('converged');
