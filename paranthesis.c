#include <stdio.h>
#include<string.h>
int search1(char *str,char search);
int main()
{
    char s[100];
    int flag=0;
    scanf("%s",s);
    char a[100];
    int j=-1;
    for(int i=0;i<strlen(s);i++){
        char str1[] = "[{(";
        char str2[] = "]})";
        int pos=search1(str1,s[i]);
        if (pos>=0){
            j++;
            a[j]=s[i];
        }
        else{
            if((j!=-1) && (search1(str1,a[j])==search1(str2,s[i]))){
                j--;
            }
            else{
                flag=1;
                break;
            }
        }
    }
    if((j==-1) && (flag==0)){
        printf("balanced");
    }
    else{
        printf("unbalanced");
    }
    return 0;
}
int search1(char *str,char search)
{
	char *position_ptr = strchr(str, search);
	int position = (position_ptr == NULL ? -1 : position_ptr - str);
	return position;
}
