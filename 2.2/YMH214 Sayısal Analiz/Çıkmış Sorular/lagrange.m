clear all;close all;clc;
xdeger=[2 3 5];
ydeger=[5 7 8];
x=4;
n=length(xdeger);
L=ones(n,n);

for i=1:n
    for j=1:n
        if(i~=j)
            L(i,:)=L(i,:).*(x-xdeger(j))/(xdeger(i)-xdeger(j));
        end
    end
    y =0;
    for i=1:n
        y=y+ydeger(i)*L(i,:);
    end
end
y