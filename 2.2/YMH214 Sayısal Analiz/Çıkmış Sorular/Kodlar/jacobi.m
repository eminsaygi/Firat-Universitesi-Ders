clear all;close all;clc
fprintf('x^2-2*x-y=0.5 ve x^2+4*y^2=4  denkleminin köklerini bul\n');
x0=0;
y0=0;
E=1.0E-4;
fprintf('i      x1      y1      errorx        errory  \n')
for i=1:100
    x1=(x0^2-y0+0.5)/2;
    y1=sqrt((4-x0^2)/4);
    errorx=abs(x1-x0);
    errory=(abs(y1-y0));
    fprintf('%4.1f %7.4f %7.4f %7.4f   %7.4f \n\n', i,x1,y1,errorx,errory);
    if abs(x1-x0)<E & abs(y1-y0)<E
        break;
    else
        x0=x1;
        y0=y1;
    end
end
disp('Denklem kök')
disp([x1,y1])