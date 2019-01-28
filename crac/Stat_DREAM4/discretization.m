function index=discretization(dat,lvl)
index = zeros(size(dat));
if lvl~=fix(lvl) || lvl<2
    return;
end
mu=mean(dat);
for i=1:size(dat,2)
    index(:,i)=(dat(:,i)>=mu(i));
end
% remains to complete the cases of lvl>2
end
