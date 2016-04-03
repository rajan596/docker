#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define fin freopen("i1.txt","r",stdin)
#define fout freopen("o1.txt","w",stdout)
#define fastio ios_base::sync_with_stdio(false); cin.tie(0)
#define pf(n) cout<<n<<endl;
#define pb(x) push_back(x)

int main(){
    fin;

    ll n;
    cin>>n;

    vector< pair<ll,ll> > v,vv;
    map< pair<ll,ll> , ll > ans;

    for(ll i=0;i<n;i++){
        ll x,y;
        cin>>x>>y;
        v.push_back({x,y});
        vv.push_back({x,y});
    }

    sort(v.begin(),v.end());

    for(ll i=0;i<n;i++){
        // do binary search for vv[i]
        ll L=-1,R=-1;

        ll l=0,r=n-1,mid;

        while(l<=r) {
            mid=(l+r)/2;
            if(v[i].first <= v[mid].first) {
                L=mid;
                r=mid-1;
            }
            else{
                l=mid+1;
            }
        }

        l=0,r=n-1;
        while(l<=r) {
            mid=(l+r)/2;
            if(v[i].second >= v[mid].second) {
                R=mid;
                l=mid+1;
            }
            else{
                r=mid-1;
            }
        }

        if(L==-1 || R==-1) {
            ans[v[i]]=0;
            continue;
        }
        else{
            ans[v[i]]=R-L+1;
        }
    }

    for(ll i=0;i<n;i++){
        if(ans[vv[i]]<=0)
            cout<<"0"<<endl;
        else
            cout<<ans[vv[i]]-1<<endl;
    }

    return 0;
}
