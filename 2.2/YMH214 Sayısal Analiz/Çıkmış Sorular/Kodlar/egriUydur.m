clear all;clc;close all;
x=[5 10 15 20 25 30 35 40 45 50]; y=[16 25 32 33 38 36 39 40 42 42];
a2=polyfit(x,y,2); % 2.dereceden polinomun katsayıları bulunur
disp('a2 Katsayıları:'), disp (a2)

xi=linspace (5, 50, 101); % x aralığı
yi2=polyval (a2, xi); % 2. dereceden pol.un aldığı değerler hesaplanıyor

plot (x, y, 'ro', 'linewidth',2), hold on % verilen datalar çizdiriliyor
plot (xi, yi2,'b', 'linewidth', 2) % uydurlan eğri çizdiriliyor
grid on
xlabel('x'), ylabel('y'), title('y=-0.0155X^2+1.3458x+12.1667')
