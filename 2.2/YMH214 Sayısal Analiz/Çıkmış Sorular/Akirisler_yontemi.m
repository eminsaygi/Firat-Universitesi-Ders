function kirisler_yontemi
clc;clear all;
it =1;
x(it)=-2.6;
it = it+1;
x(it)=-2.4;
xx=[x(1):0.01:-1.98];
y=f(xx);
while abs(f(x(it)))>0.001
    x(it+1)=(x(it  -1)*f(x(it))-x(it)*f(x(it-1)))/(f(x(it))-f(x(it-1)));
    line([x(it-1) x(it+1)],[f(x(it-1)),f(x(it+1))], [1,1],'Marker','*','LineStyle','-','Color','m');
    hold on;
    it = it+1;
end
plot(xx,y);
xlabel('x');
ylabel('y');
title(['x.^3-3*x+2=0 denkleminin kökü ',num2str(x(it))])
grid on
fprintf('x.^3-3*x+2=0 denkleminin kökü %6.4f dir ve iterasyon %6.4f dir',x(it),it);
function y=f(x);
y=x.^3-3*x+2;