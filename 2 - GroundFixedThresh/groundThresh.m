function [cent,okta] = groundThresh(img)  
    bin=saturateinv(img);
    %Find the percentage of white pixels and scale it down to okta units
    cent=length(bin(bin==1))/length(bin(:)) *100;
    okta=round(cent*0.08);
    disp("% Cloud cover: "+string(cent)+"% Okta: "+string(okta));
end
