#include<iostream>
using namespace std;
int partition(int a[],int lo,int hi)
{
    int pivot = a[hi];
    int i = lo;
    for(int j=lo;j<hi;j++)
    {
        if(a[j]<pivot)
        {
            int temp = a[j];
            a[j]=a[i];
            a[i]=temp;
            i++;
        }
    }
    return i;

}
void quickSort(int a[],int lo,int hi)
{
if(lo<hi)
{
    int  p = partition(a,lo,hi);
    quickSort(a,lo,p-1);
    quickSort(a,p+1,hi);
}

}
int main(){
    int n;
    int nums[100];
    cout<<"N : "<<endl;
    cin>>n;
    for(int a = 0;a<n;a++)
    {
        cout<<"n:"<<endl;
        cin>>nums[a];
    }
    quickSort(nums,0,n);
    for(int k = 0;k<n;k++)
    {
        cout<<nums[k]<<"\t";
    }

}