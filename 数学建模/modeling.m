function PP = modeling(micro)
m = size(micro,1);
% p = zeros(m,1);
ws = 0.2722;
wr = 0.7278;
S  = micro(:,9);
Vine = micro(:,12);
% Vine_1 = table2array(Vine);
Verify_purchase = micro(:,13);
% Verify_purchase_1 = table2array(Verify_purchase);
S1 = table2array(S);
% syms i;
k=1/log(m);
rp = micro(:,18);
rs = micro(:,20);
rp1 = table2array(rp);
rs1 = table2array(rs);
ep = 0;
for j = 1:m
    ep = ep+rp1(j,1)*log(rp1(j,1));
end
es = 0;
for j = 1:m
    es = es + rs1(j, 1)* log(rs1(j,1));
end
ep = ep * (-k);
es = es * (-k);
fp = 1 - ep;
fs = 1 - es;
R = fp/(fp+fs).*rp1 + fs/(fp+fs) .* rs1;
P = ws.*S1 + wr .* R;

Helpful_votes = micro(:,10);
Total_votes = micro(:,11);
Helpful_votes_1 = table2array(Helpful_votes);
Total_votes_1 = table2array(Total_votes);
Helpful_rate = Helpful_votes_1 ./ (Total_votes_1+eps);

v_zheng = [max(Helpful_rate), 1, 1, max(rp1), min(rs1)];
% v_zheng_1 = table2array(v_zheng);
v_fu = [min(Helpful_rate), 0, 0, min(rp1), max(rs1)];%这里应为00
% v_fu_1 = table2array(v_fu);
V = [array2table(Helpful_rate), Vine, Verify_purchase, rp, rs];
V1 = table2array(V);

% [n, m1] = size(V);
%Distance_v_fu = zeros([1, n]);
Distance_v_fu = sqrt(v_fu.^2*ones(size(V1'))+ones(size(v_fu))*(V1').^2-2*v_fu*V1');
% Distance_v_fu_1 = table2array(Distance_v_fu);
%Distance_v_zheng = zeros([1, n]);
Distance_v_zheng = sqrt(v_zheng.^2*ones(size(V1'))+ones(size(v_zheng))*(V1').^2-2*v_zheng*V1');
% Distance_v_zheng_1 = table2array(Distance_v_zheng);
Confidence = Distance_v_fu ./ (Distance_v_fu + Distance_v_zheng);
Confidence(isnan(Confidence)) = 0;
%得出解
PP = Confidence*P
