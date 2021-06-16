clear all; close all; clc; format('long','g');
fprintf('20x1+x2-2x3=17.85 3x1+20x2-x3=-18 2x1-3x2+20x3=25 denkleminin Gauss ile çözümü \n')
fprintf('');
i=1;
y(i)=0;z(i)=0;x(i)=0;
errorx=9999;
while 3>i
    x(i+1)=(17-y(i)+2*z(i))/20;
    y(i+1)=(-18-3*x(i+1)+z(i))/20;
    z(i+1)=(25-2*x(i+1)+3*y(i+1))/20;
    errorx(i+1)=abs(x(i+1)-x(i))/x(i+1)*100;
    errory(i+1)=abs(y(i+1)-x(i))/y(i+1)*100;
    errorz(i+1)=abs(z(i+1)-x(i))/z(i+1)*100;
    i=i+1;
end
disp('                   x                   error(%)');
disp([x',errorx'])
disp('                   y                   error(%)');
disp([y',errory'])
disp('                   z                   error(%)');
disp([z',errorz'])