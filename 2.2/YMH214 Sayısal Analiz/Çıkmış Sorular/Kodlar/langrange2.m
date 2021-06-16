clear all;close all;clc;
x=[2 3 5];
y=[5 7 8];
n=length(x)
f=zeros(n,n)
for i=1:n
    L=1;
    for j=1:n
        if i~=j
            L=conv(L,poly(x(j)))/(x(i)-x(j));
        end
    end
    f(i,:)=L*y(i);
end
f
P=sum(f)