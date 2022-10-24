#include <stdio.h>
int main()
{
char s[100], t[100], c[200];
printf("Input String 1 : ");
scanf("%[^\n]s", s);
while(getchar() != '\n');
printf("Input String 2 : ");
scanf("%[^\n]s", t);
int i = 0, j = 0;
while(s[i] != '\0')
{
c[j] = s[i];
i++; j++;
}
i = 0;
while (t[i] != '\0')
{
c[j] = t[i];
i++; j++;
}
c[j] = '\0';
printf("The concatenated string is : %s ", c);
return 0;
}
