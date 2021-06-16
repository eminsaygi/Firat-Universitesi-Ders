function lu_matlab_soltion
clc;clear all;warning off;
A=[1 2 5; -1 0 2; 2 1 3];b=[2;0;1];
[L,U,P] = lu(A);b=P*b;
[n m]=size (A);y=zeros (n,1);x=zeros (n,1);
for i=1:n
y(i)=b(i)-L(i,1:i-1)*y(1:i-1);
end
for i=n:-1:1
x (i)=(y(i)-U(i,i+1:n)*x(i+1:n))/U(i,i);
end
fprintf('%5s %3s\n','çözüm','-x-');
fprintf('%12.8f\n',x)
