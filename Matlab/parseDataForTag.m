function [streamData, streamTime] = parseDataForTag(streamTag, dataPackage)
    % get data size
    packageSize = size(dataPackage);
    dataSamples = packageSize(1);
    % instantiate index array, used for sorting by tags
    indexArray = zeros(1,dataSamples);
    
    for i = 1:dataSamples
        % get the ith row of the str cell, i.e the string in it
        dataStr = dataPackage{i,1};
        % split the string at every whitespace
        str = strsplit(dataStr);
        % get the first part, the head of the row so to speak, we use it as
        % identifier for each row as it holds the name of the datastream
        strHead = str{1,1};
        % fill index array with values according to the row tag
        switch (strHead)
            case streamTag
            indexArray(i) = 1;
        end         
    end
       
    streamCell = dataPackage(indexArray == 1);
    streamSize = size(streamCell);
    streamSamples = streamSize(1);

    streamData = zeros(1,streamSamples);
    streamTime = zeros(1,streamSamples);

    for j = 1:streamSamples
    % get rows
    streamStr = streamCell{j,1};
    % split the row after every whitespace
    streamSplit = strsplit(streamStr);
    % for converting reasons we need to exchange the ',' with a '.'
    % find the position of the ',' in the data string
    posData = strfind(streamSplit{1,3}, ',');
    strData = streamSplit{1,3};
    % exchange the ',' with a '.'
    strData(posData) = '.';
    % same as above for the time string
    posTime = strfind(streamSplit{1,2}, ',');
    strTime = streamSplit{1,2};
    strTime(posTime) = '.';
    % finallly we can extract time and data values into double arrays
    streamData(1,j) = str2double(strData);
    streamTime(1,j) = str2double(strTime);
    end

    if ~isempty(streamTime)
        streamTime = streamTime - streamTime(1);  
    end   
end