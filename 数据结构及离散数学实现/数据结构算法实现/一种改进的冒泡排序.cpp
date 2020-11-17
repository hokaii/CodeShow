void bubbleSort(int a[],int n)
{
     int i,j,temp;
     Status change=TRUE;
     for(i=n-1;i>1&&change;--i)
     {
          change =FALSE;
          for(j=0;j<i;++j)
               if(a[j]>a[j+1])
               {
                    temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
               }
     }
}
