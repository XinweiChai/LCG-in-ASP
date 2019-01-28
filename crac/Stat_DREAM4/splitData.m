function dataSplit=splitData(dat,lines)
dataSplit=zeros(lines,size(dat,2),ceil(size(dat,1)/lines));
for i=1:ceil(size(dat,1)/lines)
    dataSplit(:,:,i)=dat((i-1)*lines+1:i*lines,:);
end
end