clear all;close all;clc
fprintf(' 2x+8y+2z=14   x+6-z=13 2x-y+2z=5  denkleminin köklerini bul\n');
A=[2 8 2; 1 6 -1;2 -1 2];
%[2 8 2
% 1 6 -1
% 2 -1 2]
b=[14;13;5];
[n,~]=size(A);
x=zeros(n,1);
A
for i=1:n-1
    m= A(i+1:n,i)/A(i,i)
    A(i+1:n,:)=A(i+1:n,:)-m*A(i,:)
    b(i+1:n,:)=b(i+1:n,:)-m*b(i,:)
end
x(n,:)=b(n,:)/A(n,n);
for i=n-1:-1:1
    x(i,:)=(b(i,:)-A(i,i+1:n)*x(i+1:n,:))/A(i,i);
end
x
