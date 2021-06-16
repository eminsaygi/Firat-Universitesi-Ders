clc;clear all;
a=1.6;b=3;
x=[a:0.01:b];
y=f(x);
it=1;
if f(a)*f(b) >0
    fprintf('(tan(\pi-x)-x=0) denkleminin (%4.2, %4.2f) aralığında kökü yoktur',a,b)
else
m=(a*f(b)-b*f(a))/(f(b)-f(a));
while abs (f (m))>0.001
    line ([a b],[f(a) f(b)],[1 1], 'Marker','*','LineStyle','-', 'Color','m');
    hold on;
    it=it+1;
    if f(a)*f(m) <0 b=m;
    else if
         f(m) *f (b) <0 a=m;
        end
        m=(a*f(b)-b*f(a))/(f(b)-f(a));
end
plot (x,y);
xlabel('x');
ylabel('y');
title(['tan(\pi-x) -x=0 denklemini koku num2 str (m)'])
grid on
fprintf('tan (pi-x) -x=0 denkleminin kökü %6.4f dir ve iterasyon %6.4f dir',m,it)
end
function y=f(x)
y-tan (pi-x) -x;
