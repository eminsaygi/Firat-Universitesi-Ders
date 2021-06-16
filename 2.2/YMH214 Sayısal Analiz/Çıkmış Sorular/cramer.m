clear all;close all;clc
fprintf(' 2x+y+z=3, x-y-z=0, x+2y+z=0 denkleminin köklerini bul\n');
A = [2 1 1; 1 -1 -1; 1 2 1]
b = [3; 0; 0]
Ax = [3 1 1 ; 0 -1 -1; 0 2 1]
Ay = [2 3 1; 1 0 -1; 1 0 1]
Az = [2 1 3; 1 -1 0; 1 2 0]
detA=det(A)
x=det(Ax)/detA
x=det(Ay)/detA
x=det(Az)/detA
