#include<iostream>
using namespace std;
 int main()
 {
 	int a,b,c;
 	cout<<"\nenter a - \t";
 	cin>>a;
 	cout<<"\nenter b - \t";
 	cin>>b;
 	cout<<"\nenter c - \t";
 	cin>>c;
 	
	(a>b&&a>c)?cout<<"a - "<<a:(b>c)?cout<<"b - "<<b:cout<<"c - "<<c;
	
}
