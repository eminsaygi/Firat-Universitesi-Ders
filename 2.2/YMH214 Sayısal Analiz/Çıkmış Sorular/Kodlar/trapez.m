clear all;close all;clc;
fprintf('f(x)=(x+1/x)^2 fonksiyonun trapez yöntemi ile yaklaşık çözümünü bulma\n');
a=1;
b=2;
n=2;
h=(b-a)/n;
toplam=0;
for x=a:h:b-h
y=(x+1/x)^2;
toplam=toplam+h/2*((x+1/x)^2+((x+h)+1/(x+h))^2);
end
disp(' toplam');
disp([toplam])
