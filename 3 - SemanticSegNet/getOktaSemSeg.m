function [cent,okta] = getOktaSemSeg(img)  
    net=load('net.mat');
    %Find the percentage of white pixels and scale it down to okta units
    bin=semanticseg(img,net);
    bin=bin=='clouds';
    cent=length(bin(bin==1))/length(bin(:)) *100;
    okta=round(cent*0.08);
    disp("% Cloud cover: "+string(cent)+"% Okta: "+string(okta));
end
