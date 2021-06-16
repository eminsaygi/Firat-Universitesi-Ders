clear all;close all;clc;
fprintf('f(x)=sin(2xt) fonk türevini al');
syms x t
diff(sin(2*x*t),t) % t'ye göre türev aldım