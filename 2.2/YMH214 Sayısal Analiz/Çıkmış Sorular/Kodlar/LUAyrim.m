function[L U]=LUAyrim(A)
A=[1 2 5;-1 0 2;2 1 3];
b=[2;0;1];
clc;
[n m]=size(A);
if m~=n
disp('Program kare matris içindir!')
else
U=zeros(n);L=eye(n);
U(1,1:n)=A(1,1:n) ;L(1:n,1)=A(1:n,1)/U(1,1);
for i=2:n
for j=i:n
U(i,j)=A(i,j)-L(i,1:1-1)*U(1:1-1,j);
end
for j=i+1:n
L(j,i)=(A(j, i)-L(j,1:i-1)*U(1:i-1,i))/U(i,i) ;
end
%L (i+1:n,i)=L(i+1:n,i)/U(i,i);
end
end

function soltion
clc;clear all;warning off;
A=[1 2 5; -1 0 2; 2 1 3];b=[2;0;1];
[L U]=lu_ayrim(A) ;
[n m]=size(A) ;y=zeros (n,1);x=zeros (n,1);
for i=1:n
y(i)=b(i)-L(i,1:i-1)*y(1:i-1);
end
for i=n:-1:1
x(i)=(y(i)-U(i,i+1:n)*x(i+1:n))/U(i, i);
end
fprintf('%5s %3s\n', 'Çözüm','-x-');
fprintf('%12.8f\n',x)
