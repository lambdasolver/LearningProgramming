// Question 1. Write a program of structure that reads and displays the information of student.

#include <stdio.h>
#include <curses.h>
#include <stdlib.h>
#define MAX 100
typedef struct student
{
    char name[100];
    int roll;
    char sec;
    int marks;
} STUDENT;
// Globally declare the array
STUDENT s[MAX];
// function to store data
void store(int i)
{
    system("cls ");
    fflush(stdin);
    printf("[*] Enter name : ");
    gets(s[i].name);
    fflush(stdin);
    printf("[*] Enter roll no .: - ");
    scanf("%d", &s[i].roll);
    printf("[*] Enter section : - ");
    fflush(stdin);
    scanf("%c", &s[i].sec);
    fflush(stdin);
    printf("[*] Enter marks : - ");
    scanf("%d", &s[i].marks);
    fflush(stdin);
}
// display function
void display(int i)
{
    int j;
    system("cls ");
    for (j = 0; j < i; j++)
    {
        printf("\n\n[*] Name : - %s", s[j].name);
        printf("\n[*] Roll : - %d", s[j].roll);
        printf("\n[*] Sec : - %c", s[j].sec);
        printf("\n[*] Marks : - %d", s[j].marks);
        printf("\n[*] Press Enter to Continue ");
        getch();
    }
}
int main()
{
    int i = 0, option;
    char menu;
    do
    {
        system("cls "); // command to clear the screen
        printf("[*] Press 1 to store data \n[*] Press 2 to display data \n[*] Press 3 to exit \n[*] Enter your choise : ");
        scanf("%d", &option);
        switch (option)
        {
        case 1:
        {
            store(i);
            i++;
            while (1)
            {
                printf("[*] Do you want to store again [y/n]: ");
                scanf("%c", &menu);
                if (menu == 'n')
                    break;
                else
                {
                    store(i);
                    i++;
                }
            }
            break;
        }
        case 2:
        {
            display(i);
            break;
        }
        case 3:
            exit(1);

        default:
            printf("[*] Invalid option ");
            break;
        }
    } while (option != 3);
    getch();
    return 0;
}
