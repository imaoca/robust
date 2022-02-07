/*
$ wget https://project-downloads.drogon.net/wiringpi-latest.deb
$ sudo dpkg -i wiringpi-latest.deb
$ gcc -Wall -o jammer jammer.c -lwiringPi
*/

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#define pin 7
int main (void)
{
  wiringPiSetup () ;
  pinMode (pin, OUTPUT) ;
  for (;;)
  {
    digitalWrite (pin, HIGH) ; delay (15) ;
    digitalWrite (pin,  LOW) ; delay (10+rand()%10) ;
  }
  return 0 ;
}
