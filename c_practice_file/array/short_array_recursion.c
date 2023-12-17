/*
	0	1	2	3	4	5	6	7	8	9
											size = 10
a=	100	20	4	85	97	36	45	25	78	1
					MaxIndex [0]		Max[100]
(1) short (a,size)
(2) a[ size-1 ] = a [maxIndex]; ----- (swap)
	(1) call (1) short (a,size-1)
(3) if (size>1)

*/
int getIndex(int a[], int size);
int sort(int a[],int size);

int main()
	{
		int a[]={100,20,4,85,97,36,45,25,78,1};
		int size=10,i;
		sort(a,size);
		for(i=0;i<size;i++)
		{
			printf("%d\t",a[i]);
		}
	}
	
int sort(int a[],int size)
{
	int max,temp;
	if(size>1)
	{
		max=getIndex(a,size);
		temp=a[size-1];
		a[size-1]=a[max];
		a[max]=temp;
		sort(a,size-1);
	}
}

int getIndex(int a[], int size)
{
	int max,maxIndex,i;
	max=a[0];
	maxIndex=0;
	for(i=1;i<size;i++)
	{
		if(max<a[i])
		{
			max=a[i];
			maxIndex=i;
		}
	}
return (maxIndex);
}
