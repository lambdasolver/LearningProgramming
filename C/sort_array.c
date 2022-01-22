#include <stdio.h>
void main()
{
    int i = 0, n, flag = 1;
    double temp, num[1000];
    printf(" Enter number of elements in the array : ");
    scanf("%d", &n);
    printf(" Enter the numbers :\n");
    while (i != n)
    {
        scanf(" %lf", &num[i]);
        i++;
    }
    while (flag == 1)
    {
        flag = 0;
        for (i = 0; i < n; i++)
        {
            if (num[i] < num[i + 1])
            {
                temp = num[i];
                num[i] = num[i + 1];
                num[i + 1] = temp;
                flag = 1;
                break;
            }
        }
    }
    if (flag == 0)
    {
        printf("The numbers after sorting : -\n");
        for (i = 0; i < n; i++)
        {
            printf("%lf\t", num[i]);
        }
    }
}