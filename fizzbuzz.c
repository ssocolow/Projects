#include <stdio.h>

void fizzbuzz(int a);

int main(void)
{
    for(int i = 1; i <= 100; i++)
    {
        fizzbuzz(i);
    }
}

void fizzbuzz(int a)
{
    if((a % 3 == 0) && (a % 5 == 0))
    {
        printf("fizzbuzz\n");
    }
    else if(a % 3 == 0)
    {
        printf("buzz\n");
    }
    else if(a % 5 == 0)
    {
        printf("fizz\n");
    }
    else
    {
        printf("%i\n", a);
    }
}
