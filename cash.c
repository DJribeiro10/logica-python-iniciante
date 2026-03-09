#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float cash;
    do
    {
        cash = get_float("Qual o valor: ");
    }
    while ( cash <= 0 );

    int centavos = round(cash * 100);
    int contador = 0;

    while ( centavos >= 25 )
    {
        centavos = (centavos - 25);
        contador++;
    }

    while ( centavos >= 10 )
    {
        centavos = (centavos - 10);
        contador++;
    }

    while ( centavos >= 5 )
    {
        centavos = (centavos - 5);
        contador++;
    }

    while ( centavos >= 1 )
    {
        centavos = (centavos - 1);
        contador++;
    }
    printf("%i\n",contador);
    return 0;
}
