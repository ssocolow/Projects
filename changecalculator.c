//Simon Socolow
//Enter the change owed and this will print out the least number of coins required out of quarters, dimes, nickles, pennies

#include <stdio.h>
#include <cs50.h>
#include <math.h>

float get_change(void);

int main(void)
{
    float change = get_change();
    int cents0 = round(change * 100);
    int quarters = cents0 / 25;
    int cents1 = cents0 - (quarters * 25);
    int dimes = cents1 / 10;
    int cents2 = cents1 - (dimes * 10);
    int nickles = cents2 / 5;
    int cents3 = cents2 - (nickles * 5);
    int pennys = cents3;
    
    int coins = quarters + dimes + nickles + pennys;
    printf("%d\n", coins);
}

float get_change(void)
{
    float change;
    do
    {
        change = get_float("Change owed: ");
    }
    while(change < 0);
    return change;
}
