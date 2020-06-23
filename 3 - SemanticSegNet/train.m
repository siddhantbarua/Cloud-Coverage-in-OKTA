%% Load Image dataset

dataSetDir=fullfile("C:\Users\KIIT\Downloads\imgs\cloudImages\swimseg");
imageDir=fullfile(dataSetDir,'images');
labelDir=fullfile(dataSetDir,'GTmaps');
imds=imageDatastore(imageDir);   %Datastore of VIS Images
labelIDs=[0 255];classNames=["sky" "clouds"];
pxds=pixelLabelDatastore(labelDir,classNames,labelIDs); %Datastore of GT
clear dataSetDir imageDir labelDir
%% Create CNN Layers

numFilters=16;
filterSize=3;
numClasses=2;
layers=[
    imageInputLayer([600 600 3])
    convolution2dLayer(filterSize,numFilters,'Padding',1)
    reluLayer()
    maxPooling2dLayer(2,'Stride',2)
    convolution2dLayer(filterSize,numFilters/2,'Padding',1)
    reluLayer()
    maxPooling2dLayer(2,'Stride',2)
    convolution2dLayer(filterSize,numFilters/2,'Padding',1)
    reluLayer()
    maxPooling2dLayer(2,'Stride',2)
    convolution2dLayer(filterSize,numFilters/2,'Padding',1)
    transposedConv2dLayer(3,numFilters,'Stride',2,'Cropping','same');
    convolution2dLayer(filterSize,numFilters/2,'Padding',1);
    transposedConv2dLayer(3,numFilters,'Stride',2,'Cropping','same');
    convolution2dLayer(filterSize,numFilters,'Padding',1);
    transposedConv2dLayer(3,numFilters,'Stride',2,'Cropping','same');
    convolution2dLayer(1,numClasses);
    softmaxLayer()
    pixelClassificationLayer()
 ];

 %% Train the network
opts=trainingOptions('sgdm','InitialLearnRate',1e-3,'MaxEpochs',5,'MiniBatchSize',10,"Plots","training-progress");
trainingData=pixelLabelImageDatastore(imds,pxds);
net=trainNetwork(trainingData,layers,opts);

%% Confusion Matrix
pxdsTruth=semanticseg(imds,net,'MiniBatchSize',5,"WriteLocation",tempdir);
metrics=evaluateSemanticSegmentation(pxdsTruth,pxds);
normConfMatData = metrics.NormalizedConfusionMatrix.Variables;
figure
h = heatmap(classNames,classNames,100*normConfMatData);
h.XLabel = 'Predicted Class';
h.YLabel = 'True Class';
h.Title = 'Normalized Confusion Matrix (%)';
