%% Load a pretrained model if you dont want to train it right now
clc;
clear;
close;
load('net.mat');
%% 
dataSetDir=fullfile("C:\Users\KIIT\Downloads\imgs\cloudImages\swimseg");
imageDir=fullfile(dataSetDir,'Testing');
labelDir=fullfile(dataSetDir,'Testing_segments');
imds=imageDatastore(imageDir);
labelIDs=[0 255];classNames=["sky" "clouds"];
pxds=pixelLabelDatastore(labelDir,classNames,labelIDs);
pxdsTruth=semanticseg(imds,net,'MiniBatchSize',5,"WriteLocation",tempdir);
metrics = evaluateSemanticSegmentation(pxds,pxdsTruth);
%% View 5 images and predictions
for i=1:5
    nos=80+i-1;
    img=readimage(imds,nos);
    gt=readimage(pxds,nos);
    C=semanticseg(img,net);
    mask=C=='clouds';
    gt=gt=='clouds';
    figure
    montage({img,mask,gt},'Size',[1 3])
    title('Image: '+string(nos)+" Real img/Predicted/GT");
end
clear nos

%% Worst detected image
imageIoU = metrics.ImageMetrics.MeanIoU;
[minIoU, worstImageIndex] = min(imageIoU);
minIoU = minIoU(1);
worstImageIndex = worstImageIndex(1);
worstTestImage = readimage(imds,worstImageIndex);
worstTrueLabels = readimage(pxdsTruth,worstImageIndex);
worstPredictedLabels = readimage(pxds,worstImageIndex);

worstTrueLabelImage = im2uint8(worstTrueLabels == classNames(1));
worstPredictedLabelImage = im2uint8(worstPredictedLabels == classNames(1));

worstMontage = cat(4,worstTestImage,worstTrueLabelImage(:,:,[1 1 1]),worstPredictedLabelImage(:,:,[1 1 1]));
worstMontage = imresize(worstMontage,4,"nearest");
figure
montage(worstMontage,'Size',[1 3])
title(['Test Image vs. Truth vs. Prediction. IoU = ' num2str(minIoU) ' Img no. ' num2str(worstImageIndex)]);

%% Best image
[maxIoU, bestImageIndex] = max(imageIoU);
maxIoU = maxIoU(1);
bestImageIndex = bestImageIndex(1);

bestTestImage = readimage(imds,bestImageIndex);
bestTrueLabels = readimage(pxdsTruth,bestImageIndex);
bestPredictedLabels = readimage(pxds,bestImageIndex);

bestTrueLabelImage = im2uint8(bestTrueLabels == classNames(1));
bestPredictedLabelImage = im2uint8(bestPredictedLabels == classNames(1));

bestMontage = cat(4,bestTestImage,bestTrueLabelImage(:,:,[1 1 1]),bestPredictedLabelImage(:,:,[1 1 1]));
bestMontage = imresize(bestMontage,4,"nearest");
figure
montage(bestMontage,'Size',[1 3])
title(['Test Image vs. Truth vs. Prediction. IoU = ' num2str(maxIoU)])

%% Making GT from Labeler
[imds,pxds]=pixelLabelTrainingData(gTruth);
p=readimage(pxds,1);
p(p~='clouds')='sky';
img=p=='clouds';
imshowpair(img,readimage(imds,1),'montage');
imwrite(img,'gt.png');