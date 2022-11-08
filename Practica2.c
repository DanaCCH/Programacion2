#include<stdio.h>
//SWITCH

//EJERCICIO 1
// int main(){
// int i;
// printf("Ingresa un numero: ");
// scanf("%d",&i);

// switch (i) {
//     case 6:
//         printf("El numero de la cara opuesta es uno");
//         break;
//     case 5:
//         printf("El numero de la cara opuesta es dos");
//     case 4:
//         printf("El numero de la cara opuesta es tres");
//     case 3:
//         printf("El numero de la cara opuesta es cuatro");
//     case 2:
//         printf("El numero de la cara opuesta es cinco");
//     case 1:
//         printf("El numero de la cara opuesta es seis");
//     default:
//         printf("El numero es incorrecto");
//         break;  
// }
// return 0;
// }

//EJERCICIO 2
// int main(){
//     int i;
//     printf("Habitacion:\n1.Azul\n2.ROja\n3.Verde\n4.Rosa\n5.Gris""\nIngrese un numero asociado a una habitacion: ");
//     scanf("%d",&i);
// switch (i)
// {
// case 1:
//     printf("Primera planta, dos camas");
//     break;
// case 2:
//     printf("Primera planta, una cama");
//     break;
// case 3:
//     printf("Segunda planta, tres camas");
//     break;
// case 4:
//     printf("Segunda planta, dos camas");
//     break;
// case 5:
//     printf("Tercera planta, una cama");
//     break;
// default:
//     printf("Numero no asociado a habitación.");
//     break;
// }
// return 0;
// }

//ESTRUCTURA FOR

//EJERCICIO 3

int sumatoria1(int i){
    double sumatoria = 0;
    for (int i = 1; i<= 100; i++){
        sumatoria += 1/i;
    }
    return printf("%f",sumatoria);
}
int main(){
    sumatoria1(100);
}

// int main(){
//     int sumatoria = 0;
//     for (int i = 1; i<=30;i++){
//         sumatoria = sumatoria + (1/i*i);
//     }
//     printf("El resultado de la sumatoria es %d",sumatoria);
//     return 0;
// }