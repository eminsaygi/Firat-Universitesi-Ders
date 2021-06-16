clear all;close all;clc;
y0=2;
a=0;
b=1;
n=2;
h=(b-a)/2;
for x0=0:h:1
    k1=h*(x0+y0);
    k2=h*(x0+0.5*h+y0+k1*0.5);
    y1=y0+k2;
    plot(x0,y0,'--r*');
    hold on
    grid on
    xlabel('x0');
    ylabel('y0');
    y0=y1
end

