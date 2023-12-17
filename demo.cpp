#include<iostream>
#include<stdio.h>
using namespace std;
class A
{
public:
int x,temp;
	void get_data()
	{
		cout<< "enter number in Class A =-  : ";
		cin>>x;
		temp=x;
	}
};
//-----------------------------------------------
class B :public A
{
int i ,remain,sum=0;
public:
 void cal ()
 {
 	while (x!=0)
 	{
 		remain=x%10;
 		sum=(sum*10)+remain;
 		x=x/10;
 	}
 	cout<< sum;
 if (temp==sum)
 {
 	cout<<"class B :: poli "<<temp <<endl;
 }
 else
 cout<<" class B ::isn't poli "<<temp <<endl;
 }
};
//----------------------------------------
class D :public B
{
public:
int remain,x1,sum=0;
void add()
{	
x1=temp;
	while (x1!=0)
	{
		remain=x1%10;
		sum=sum+remain;
		x1=x1/10;
	}
cout<<sum <<" Class D is Calling  "<<endl;
cout<<" Sum of Given Number in Class input from Class A inharite from Class A \n";
}
};
//-------------------------------------------------
class E:public B
{
public:
void e()
	{
	cout<<"  Call From Class E inharite from Class A \n";
		cout << " Class E is Calling "<< endl;	
	}
};
//----------------------------------------
class C:public A
{
public:
 void fun()
 {	cout << "Input data form class A - ";
 	cout<< " hello Class C is calling "<< endl;
 }
};
//-----------------------------------------------------
class F :public C
{
	public:
	void grater()
	{
		int max=0,remain;
		while (temp!=0)
		{
			remain=temp%10;
			if(remain>=max)
			{
				max=remain;
			}
			temp=temp/10;
		}
		cout<< "Grater = "<<max<<endl;
		cout<<" Class F is calling by C "<<endl;
		cout<<" Call from Class F inharite from Class C input data from Class A \n";

	}
};
//---------------------------------------------
class G :public C
{
public:
	void smallest()
	{
		int min=10,remain;
		while (temp!=0)
		{
			remain=temp%10;
			if(remain<=min)
			{
				min=remain;
			}
			temp=temp/10;
		}
		cout<< "Smallest = "<<min<<endl;
		cout<<" Class F is calling by C "<<endl;
		cout<<" Call from Class G inharite from Class C input data from Class A \n\n";
		}

};
//*******************************************

int main()
{
 E e1;
 D d1;
 F f1;
 G g1;
 cout <<"-----output from E Class object ----"<<endl;
 e1.get_data();
 e1.cal();
 e1.e();
cout <<endl<<"-----output from D Class object ----\n"<<endl;
 
 d1.get_data();
 d1.cal();
 d1.add();
cout <<endl<<"-----output from F Class object ----\n"<<endl;
f1.get_data();
f1.fun();
f1.grater();
cout <<endl<<"-----output from G Class object ----\n"<<endl;
g1.get_data();
g1.fun();
g1.smallest();
}
