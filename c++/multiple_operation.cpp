#include <iostream>
using namespace std;
int main()
{
	int a,b,x,c;
	cout<<"enter a - \t";
	cin>>a;
	cout<<"enter b - \t";
	cin>>b;
	cout<<" 1.add";
	cout<<" 2.sub";
	cout<<" 3.multi";
cout<<"select operation : ";
cin>>x;
	switch(x)
	{
		case 1:
		c=a+b;
		cout<<c;
		break;
	}
}
