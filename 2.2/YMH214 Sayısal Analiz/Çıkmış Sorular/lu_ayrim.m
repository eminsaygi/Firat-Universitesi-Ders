clear all;close all;clc;
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
