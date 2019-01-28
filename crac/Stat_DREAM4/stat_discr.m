clear ; close all; clc;
%data = load('insilico_size10_1_nonoise_proteins_timeseries.tsv');
%data = load('insilico_size10_1_noexpnoise_proteins_timeseries.tsv');
data = load('insilico_size10_1_timeseries.tsv');
%  data = load('insilico_size10_1_nonoise_timeseries.tsv');
data(:,1) = [];
%  data(:,8:10)=[];% remains to be modified
period=21;

dat_sets=splitData(data,period);
incr = dat_sets(2:end,:,:)-dat_sets(1:end-1,:,:);
for i=1:size(dat_sets,3)
    dat_disc(:,:,i)=discretization(dat_sets(:,:,i),2);
    
end
incr_discr=incr>0;
threshold = 0.75;
maxDelay=5;
matchedPairs=zeros(size(data,2));
result=[];
for i=1:size(dat_sets,3)
    for delay=0:maxDelay
        for j=1:10
            for k=1:10
                if j~=k
                    temp=match(dat_disc(:,:,i),incr_discr(:,:,i),j,k,delay);
                    if abs(temp)>threshold
                        matchedPairs(j,k)=temp;
                        result=[result;j,k,temp,delay];
                    end
                end
            end
        end
    end
end
