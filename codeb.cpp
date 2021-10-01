class StockSpanner {
public:
     stack<pair<int, int>> s;
    StockSpanner() {
        
    }
    
    int next(int price) {
        int ans=1;
        while(s.size()>0 && s.top().first<=price){
            ans+=s.top().second;
            s.pop();
        }
        s.push({price,ans});
        return ans;
    }
};
