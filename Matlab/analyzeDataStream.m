function features = analyzeDataStream(streamTag, streamData, streamTime)
    if ~isempty(streamData)
        switch(streamTag)
            case GSR_TAG

            case BVP_TAG

            case IBI_TAG

            case HR_TAG

            case TMP_TAG

            case ACC_TAG

        end
    else
        features = [];
    end
            
end