#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Digite um numero: ");
    }
    while (n < 1 || n > 8);

    // ALTURA (linhas)
    for (int i = 0; i < n; i++)
    {
        // imprimir ESPACOS
        for (int a = 0; a < n - i - 1; a++)
        {
            printf(" ");
        }

        // LARGURA (# a cada linha)
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }

        printf("\n");
    }
}
