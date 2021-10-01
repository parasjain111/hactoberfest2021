class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        vector<long long int> pre;
        long long int s=0;
        for(auto it:chalk){
            s+=it;
            pre.push_back(s);
        }
        long long int z=k%s;
        if(z==0){
            return 0;
        }
        z=upper_bound(pre.begin(),pre.end(),z)-pre.begin();
        
        return z;
    }
};