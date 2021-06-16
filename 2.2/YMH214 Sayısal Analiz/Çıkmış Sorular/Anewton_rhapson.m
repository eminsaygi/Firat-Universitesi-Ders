function newton_rhapson
clc;clear all;
a=1.6;b=3;
xx=[a:0.01:b];
y = f(xx);
it=1;
x(it)=a;
while abs (f(x(it)))>eps
    if abs (df(x(it)))<eps
        disp('Program türev sıfır durumunda hesaplanamaz')
        break;
    else
        line([x(it) x(it)-f(x(it))/df(x(it))],[f(x(it)),0], [1,1],'Marker','*','LineStyle','-','Color','m');
        hold on;
        x(it+1)=x(it)-f(x(it))/df(x(it));
        it=it+1;
    end
end
plot(xx,y);
xlabel('x');
ylabel('y');
title(['tan(\pi-x)-x=0 denkleminin kökü ',num2str(x(it))])
grid on
fprintf('tan(pi-x)-x=0 denkleminin kökü %6.4f dir ve iterasyon %6.4f dir',x(it),it)
function y =f(x)
y = tan(pi-x)-x;
function y = df(x)
y= -(1+(tan(pi-x)).^2)-1;