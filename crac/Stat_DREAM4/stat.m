clear ; close all; clc;
%data = load('insilico_size10_1_nonoise_proteins_timeseries.tsv');
%data = load('insilico_size10_1_noexpnoise_proteins_timeseries.tsv');
data = load('insilico_size10_1_timeseries.tsv');
%  data = load('insilico_size10_1_nonoise_timeseries.tsv');
data(:,1) = [];
%  data(:,8:10)=[];% remains to be modified
period=21;

dat_sets=splitData(data,period);

dat_sets(1:10,:,:)=[];

incr = dat_sets(2:end,:,:)-dat_sets(1:end-1,:,:);
for i=1:size(dat_sets,3)
    dat_disc(:,:,i)=discretization(dat_sets(:,:,i),2);
    
end

incr_discr=incr>0;
threshold=0.6;
maxDelay=2;
n_comp=size(data,2);
tempData0=dat_sets;
tempData1=dat_sets;
tempData0(dat_disc==1)=NaN;
tempData1(dat_disc==0)=NaN;


note=[];
step=2;
for k=1:size(dat_sets,3)
    sample=tempData0(:,:,k);
    increment = incr(:,:,k);
    for delay=0:maxDelay
        cor=zeros(n_comp,n_comp);
        for i=1:n_comp
            for j=1:n_comp
                if i~=j && ttest2(dat_sets(1:end,i,k),dat_sets(1:end,j,k))==1
                    tempMat=sample;
                    tempMat(:,[i,j])=[];
                    for m=1:step:size(tempMat,2)
                        if size(tempMat,2)-m<=step
                            if mod(size(tempMat,2),step)==0
                                realStep=step-1;
                            else
                                realStep=mod(size(tempMat,2),step)-1;
                            end
                        else
                            realStep=step-1;
                        end
                        if delay==0
                            
                            tempCor= partialcorr(sample(1:end,i),sample(1:end,j),tempMat(1:end,m:m+realStep),'type','Spearman','rows','pairwise');% better performance?
%                             tempCor= partialcorr(sample(2:end,i),increment(1:end,j),tempMat(2:end,m:m+realStep),'type','Spearman','rows','pairwise');
                        else
                            tempCor= partialcorr(sample(1:end-delay,i),sample(delay+1:end,j),tempMat(1:end-delay,m:m+realStep),'type','Spearman','rows','pairwise');
%                             tempCor= partialcorr(sample(1:end-delay,i),increment(delay:end,j),tempMat(1:end-delay,m:m+realStep),'type','Spearman','rows','pairwise');
                        end
                        
                        if abs(tempCor)>abs(cor(i,j))
                            cor(i,j)=tempCor;
                        end
                        %                  cor(i,j)= partialcorr(sample(1:end-delay,i),increment(delay:end,j),increment(delay:end,[1:j-1,j+1:end]));
                        if abs(cor(i,j))>threshold
                            note=[note;i j sign(cor(i,j)) delay cor(i,j)];
                        end
                    end
                    
                end
            end
        end
    end
end
temp=tabulate(cellstr(num2str(note(:,1:3))));
sortrows(temp,-size(temp,2))
%find(abs(cor)>0.6)