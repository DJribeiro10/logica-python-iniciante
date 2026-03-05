#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x = get_int("Digite um numero: ");

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j < x; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
