#include <cs50.h>
#include <stdio.h>

void miau(int n);

int main(void)
{
        miau(10);
        miau(10);
        miau(10);
}

void miau(int n)
{
    for ( int i = 0; i < n; i++)
    {
        for ( int j = 0; j < n; j++ )
        {
            printf("miau");
        }
        printf("\n");
    }
}
