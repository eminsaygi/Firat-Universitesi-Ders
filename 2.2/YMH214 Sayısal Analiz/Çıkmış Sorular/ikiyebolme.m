function ikiyebolme %bisection method Ve her  editör ile yazdığımda buraya function yazmam gerekiyor
clc;clear all;
a =0.6;b=0.8;
x=[a:0.01:b]; %bu aralıkta, ortadaki sayı hata payı gibi bir şey
y=f(x);
it=1;
if f(a)*f(b)>0 % 0 dan büyükse
    fprintf("x^3-10*x^2+5 fonksiyonun (%4.2f,%4.2f) aralığında kökü yok",a,b);
    
else 
    m=(a+b)/2;
    while(abs(f(m))>eps)&((b-a)/2>eps)
        plot(a,0,"or"); % çizginisi çizin
        line([a a],[0,f(a)],[1 1], "Marker","*","LineStyle","-","Color","m");
        hold on; % değişiklikleri tut
        plot(b,0,"or");
        line([a a],[0,f(a)],[1 1], "Marker","*","LineStyle","-","Color","m");
        hold on; it=it+1; %tut ve iterasyonu tamamla
        if f(a)*f(m)<0 b=m;
        elseif f(m)*f(b)<0 a=m;
        end
        m=(a+b)/2;
        
    end
end 
plot(x,y);
xlabel("x kısmı");
ylabel("y kısmı");
title("x^3-10*x^2+5=0 denkleminin kökü",num2str(m))
grid on
fprintf("x^3-10x^2+5=0 denkleminin kökü %6.4f dir ve iterasyon %6.4f dir",m,it);

function y=f(x);
y=x.^3-10*x.^2+5;