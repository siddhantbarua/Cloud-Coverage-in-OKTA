function [cent,okta] = getOkta(y,x)
    
    % Getting the Image from IMD Site
    img=webread("https://mausam.imd.gov.in/Satellite/3Dasiasec_ir1.jpg");

    %If no internet connection then use a downloaded image
    %     img=imread('3Dasiasec_ir1.jpg');
    
    %Convert the rgb image to hsv channel
    I = rgb2hsv(img);
    % X is LONGITUTE
    % Y is LATITUDE
    
    % Consider only the given range inside to be clouds, rest is ground
    mask = (I(:,:,1) >= 0.000 ) & (I(:,:,1) <= 0.987) & ...
        (I(:,:,2) >= 0.000 ) & (I(:,:,2) <= 0.324) & ...
        (I(:,:,3) >= 0.342 ) & (I(:,:,3) <= 1); 

    % Either Name of city or a given Coordinates
    
    %Find the city and get its coordinates
    if ~exist('x','var')
        city=y;
        cities=getCities('cities.csv');
        if(size(cities(cities.city_name==city,:),1)<1)
            cent=0;okta=0;
            disp("City not Found");
            return
        end
        x=cities(cities.city_name==city,:).longitude;
        y=cities(cities.city_name==city,:).latitude;
    end
    
    %Change to coordinates to pixel values
    newy=round(1112.285714-18.96714286*y-0.07357142857*y^2);
    newx=round(-899.428571+20.273929*x-8.29857e-4*x^2);
    
    %Crop the image surrounding the given city to find cloud cover
    cityimg=mask(newy-10:newy+10,newx-10:newx+10);
    
    % Debug
%     imshowpair(img,mask,'montage');hold on;
% %   plot(newx,newy,'rs','MarkerSize',70);
%     figure;imshow(cityimg);
    %
    
    %Find the percentage of white pixels and scale it down to okta units
    cent=length(cityimg(cityimg==1))/length(cityimg(:)) *100;
    okta=round(cent*0.08);
    disp("% Cloud cover: "+string(cent)+"% Okta: "+string(okta));
end
