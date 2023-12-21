#include<iostream>
using namespace std;
{
int a,b,c;
public:
void getdata()
{
cout<<"enter the three values";
cin>>a,b,c;
}
void operator-()
a=-b;
b=-b;
c=-c;
void show()
{
cout<<"a="<<endl;
cout<<"b="<<endl;
cout<<"c="<<endl;
}
};
int main()
{
XYZ xy;
xy.getdata();
xy.display();
-xy;
xy.display();
}
