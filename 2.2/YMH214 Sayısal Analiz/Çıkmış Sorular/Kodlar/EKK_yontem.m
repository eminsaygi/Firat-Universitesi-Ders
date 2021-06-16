clc; clear all; close all;

x=[0 1 2 4 7];
y=[1 4 7 13 22];

fx=(sum(y)/length(y))*ones(1,5)

plot(x,y,'k o',x,fx,'r')
legend('verilen','hesaplanan')