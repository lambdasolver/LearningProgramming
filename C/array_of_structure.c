// Qs: Write a program to demonstrate the usage of Array of structure.

#include <stdio.h>
#include <string.h>
struct student
{
    int roll;
    char name[50];
    float mks;
};
int main()
{
    int i;
    struct student record[2];
    // 1st student ’s record
    record[0].roll = 1;
    strcpy(record[0].name, " Soham ");
    record[0].mks = 86.5;
    // 2nd student ’s record
    record[1].roll = 2;
    strcpy(record[1].name, " Niladri ");
    record[1].mks = 90.5;
    // 3rd student ’s record
    record[2].roll = 3;
    strcpy(record[2].name, " Koustav ");
    record[2].mks = 81.5;
    for (i = 0; i < 3; i++)
    {
        printf(" Records of STUDENT : %d \n", i + 1);
        printf(" Roll is: %d \n", record[i].roll);
        printf(" Name is: %s \n", record[i].name);
        printf(" mks is: %f\n\n", record[i].mks);
    }
    return 0;
}