function res=match(dat,incr,i,j,delay)
    if delay==0
        dat(1,:)=[];
    else
        dat(end-delay+1:end,:)=[];
        incr(1:delay-1,:)=[];
    end
    res=sum(dat(:,i)==incr(:,j))/size(dat,1);
    if res<0.5
        res=-1+res;
    end
end