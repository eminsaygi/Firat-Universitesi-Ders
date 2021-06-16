clear all;close all;clc;
x=-2:0.1:2;
y=exp(x);
fig=figure();
set(fig,'color','white')
plot(x,y,'linewidth',2)
grid on
xlabel('x')
ylabel('y')
N=1;
tay=0*y;
for n=0:N
    tay=tay+(x.^n)/factorial(n);
end
hold on
plot(x,tay,'r-','Linewidth',2)
legend('fonksiyon','Taylor serisi')