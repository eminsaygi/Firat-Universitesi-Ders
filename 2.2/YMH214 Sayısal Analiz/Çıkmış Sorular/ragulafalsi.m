clear all;close all;clc
fprintf('f(x)=x^3-2 denkleminin köklerini bul\n');
a=1;
b=2;
tol=0.00001;
fprintf('\n iter   a        b       xr      y(xr)\n')
for i=1:50
    fonka=a^3-2;
    fonkb=b^3-2;
    xr=(a*fonkb-b*fonka)/(fonkb-fonka);
    fonkxr=xr^3-2;
    fprintf('%4.1f %7.4f %7.4f %7.4f %7.4f \n', i,a,b,xr,fonkxr);
    if abs(fonkxr)<tol
        break;
    end
    if fonka*fonkxr<0
        b=xr;
        fonkb=fonkxr;
    else
        a=xr;
        fonka=fonkxr;
    end
end
disp('Iterasyon Sayısı')
i
disp('Denklemin kökü');
format long
xr
disp('Fonksiyonun kökteki değeri')
fonkxr
