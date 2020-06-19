function [cent,okta] = getOktaHis(y,x)
    % Getting the Image from IMD Site
    [gif,map]=webread("https://mausam.imd.gov.in/Satellite/Converted/IR1.gif");
    okta=zeros(1,12);
    cent=okta;str="";
    for i=1:12
        img=gif(:,:,:,i);
        img=ind2rgb(img,map);
        I = rgb2hsv(img);
        % X is LONGITUTE
        % Y is LATITUDE
        mask = (I(:,:,1) >= 0.000 ) & (I(:,:,1) <= 0.987) & ...
            (I(:,:,2) >= 0.000 ) & (I(:,:,2) <= 0.324) & ...
            (I(:,:,3) >= 0.342 ) & (I(:,:,3) <= 1); 

        % Either Name of city or a given Coordinates
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
            str=city+" Cloud cover %";
        end
        newy=round(1112.285714-18.96714286*y-0.07357142857*y^2);
        newx=round(-899.428571+20.273929*x-8.29857e-4*x^2);
        cityimg=mask(newy-10:newy+10,newx-10:newx+10);

        % Debug
%         imshow(img);hold on;
%         plot(newx,newy,'rs','MarkerSize',20);
%         figure;imshow(cityimg);
        %

        cent(i)=length(cityimg(cityimg==1))/length(cityimg(:)) *100;
        okta(i)=round(cent(i)*0.08);
    end
    bar(cent);
    ylim([0 100]);
    title(str);
    xlabel("Last 6 hours");
    ylabel("% Cloud Cover");
end
