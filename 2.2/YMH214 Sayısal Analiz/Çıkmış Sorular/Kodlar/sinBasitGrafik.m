clear all;close all;clc
fprintf('e^x -5sin(pi*x/2) denkleminin köklerini bul\n');
f=exp(x)-5*sin(pi*x/2);
plot(x,f,'b','linewidth',2)
grid on