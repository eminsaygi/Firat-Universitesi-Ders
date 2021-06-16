clear all;close all;clc
fprintf('f(x)=e^(-x)-x denkleminin köklerini bul\n');
x1=0;
tol=0.01;
for x1=0:0.01:1 
    y=x1;
    yy=exp(-x1);
plot(x1,y,'r*',x1,yy,'b.')
hold on
grid on
xlabel('x')
ylabel('y')
text(0.5,0.8,'*y=x')
text(0.5,0.75,'+y=e^(-x)')
end
x1=0;
fprintf('Iter   x1      x2      Ea      ear         \n')
for i=1:50
    x2=exp(-x1);
    Ea=abs(x2-x1);
    ear=Ea/abs(x2);
    fprintf('%4.1f %7.4f %7.4f %7.4f %7.4f\n',i,x1,x2,Ea,ear);
    if abs(x2-x1)<tol
        break;
    else
        x1=x2;
    end
end
disp('Denkklemin koku');
disp([x2])
   