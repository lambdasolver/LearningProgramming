#include <stdio.h>
struct student
{
    char name[30];
    int roll;
    float mks;
};
int main()
{
    struct student s;
    struct student *ps;
    ps = &s;
    printf(" Enter name : ");
    gets(ps -> name);
    printf(" Enter roll :");
    scanf("%d", &ps -> roll);
    printf(" Enter Marks : ");
    scanf("%f", &ps -> mks);
    printf("\ nName : %s", ps->name);
    printf("\ nPrice : %d", ps->roll);
    printf("\ nQuantity : %f", ps->mks);
    return 0;
}