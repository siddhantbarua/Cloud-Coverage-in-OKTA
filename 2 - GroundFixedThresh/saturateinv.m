function [bin] = saturateinv(img)
hsv=rgb2hsv(img);   %Convert to HSV color space
gray=hsv(:,:,2);   % 2nd Channel is Saturation channel
gray=1-gray;        % Invert Saturation
bin=imbinarize(gray);   % Threshold
end