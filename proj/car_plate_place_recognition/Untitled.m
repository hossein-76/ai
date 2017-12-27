clear all
close all
clc
im0=imread('D:\projects\ai\ai\Project\small sample\small sample\13.jpg');
figure(1),imshow(im0);
im1=rgb2gray(im0);
figure(2),imshow(im1);
im2=edge(im1,'roberts',0.18,'both');
figure(3),imshow(im2);
mat=[1;1;1];
im3=imerode(im2,mat);
figure(4),imshow(im3);
mat=strel('rectangle',[25,25]);
im4=imclose(im3,mat);
figure(5),imshow(im4);
im5=imdilate(im4,strel('diamond',1));
im6=imerode(im5,strel('diamond',1));
im7=imfill(im6,'holes');
[m n]=size(im7);
im8=bwlabel(im7);
im9=bwareaopen(im8,2000);
figure(6),imshow(im9);
reg=regionprops(im9,'Area','Extent','BoundingBox','Image','Orientation','Centroid');
index=(find([reg.Area] == max([reg.Area])));
im10=reg(index).Image;
figure(7),imshow(im10);
x1=floor(reg(index).BoundingBox(1));
x2=ceil(reg(index).BoundingBox(3));
y1=ceil(reg(index).BoundingBox(2));
y2=ceil(reg(index).BoundingBox(4));
bou=[y1 x1 y2 x2];
im11=imcrop(im0(:,:,:),[x1,y1,x2,y2]);
figure(8),imshow(im11);
im12=imcrop(im1(:,:),[x1,y1,x2,y2]);
figure(9),imshow(im12);
imwrite(im11, 'D:\projects\ai\ai\Project\small sample\small sample\1113.jpg');