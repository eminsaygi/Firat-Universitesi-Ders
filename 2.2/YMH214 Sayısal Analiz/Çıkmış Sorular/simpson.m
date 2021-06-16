clear all;close all;clc;
fprintf('f(x)=(x^3+1) fonksiyonun Simpson yöntemi ile yaklaşık çözümünü bulma\n');
a=-1;
b=3;
n=2;
h=(b-a)/n;
toplam=0;
for x0=a:h:b-h
x1=(x0+(x0+h))/2;
x2=x0+h;
fx0=(x0^3+1);
fx1=(x1^3+1);
fx2=(x2^3+1);
toplam=toplam+h/6*(fx0+4*fx1+fx2)
end
disp(' toplam');
disp([toplam])
