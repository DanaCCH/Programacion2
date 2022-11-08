#include<stdio.h>
#include<ctype.h>

// int main(){
//     int a, b, c, d =6,e;
//     a = b = 3;
//     c = a*b+d;
//     e = (c+5)/4-3;
//     e+=5;
//     printf("Los resultados son %d y %d ", c, e);
//     return 0;
// } 

// int main(){
//     int a,b,c,d=6,e;
//     a = 3;
//     b = a-d/3; 
//     a *= b; 
//     c = a+d/a-3/a*b;
//     e= c+8/4-b;
//     e+=5;
//     printf("Los resultados son %d y %d ",c,e);
//     return 0;
// } 'los resultados son 4 y 10

// int main(){
//     float x,y;
//     printf("Introduzca 2 números:\n");
//     scanf("%f%f",&x,&y);
//     printf("La suma de %f y %f vale %f \n", x,y,x+y);
//     printf("La suma de %4f y %4.2f vale %10.3f\n",x,y,x+y);
//     printf("La suma de %e y %e vale %e\n",x,y,x+y);
//     return 0;
// }

//---SELECCION 
// EJERCICIO 4
// int main(){
//     int x;
//     printf("Introduzca un valor de temperatura: ");
//     scanf("%d",&x);
//     if (x<0){
//         printf("El estado es sólido");
//     }
//     else if (x<100){
//         printf("El estado es líquido");
//     }
//     else if (x>100){
//         printf("El estado es gaseoso");
//     }
//     return 0;
// }
// EJERCICIO 5
// int main(){
//     int x;
//     printf("Ingrese la nota del alumno:");
//     scanf("%d",&x);
//     if (x<=1 && !isdigit(x)){
//         printf("La nota es incorrecta");
//     }
//     else if (x>=2 && x<=5){
//         printf("Insuficiente");
//     }
//     else if (x == 6){
//         printf("Aprobado");
//     }
//     else if (x == 7){
//         printf("Bueno");
//     }
//     else if ( x == 8){
//         printf("Muy bueno");
//     }
//     else if (x==9){
//         printf("Distinguido");
//     }
//     else if (x == 10){
//         printf("Sobresaliente");
//     }
//     return 0;
// }
//EJERCICIO 6
// int main(){
//     int d,m;
//     printf("Ingrese el día de nacimiento:\n");
//     printf("Ingrese el mes de nacimiento:\n");
//     scanf("%d%d", &d, &m);
//     if (d>=1 && d<=31){
//         if (m>=1 && m<=12){
//             if (d>=22 && m==12 || d>=1 && d<=20 && m == 1){
//                 printf("Capricornio");
//             }
//             else if (d>=21 && m==1 || d>=1 && d<=19 && m==2){
//                 printf("Acuario");
//             }
//             else if (d>=20 && m==2 || d>=1 && d<=20 && m==3){
//                 printf("Piscis");
//             }
//             else if (d>=21 && m==3 || d>=1 && d<=19 && m==4){
//                 printf("Aries");
//             }
//             else if (d>=20 && m==4 || d>=1 && d<=20 && m==5){
//                 printf("Tauro");
//             }
//             else if (d>=21 && m==5 || d>=1 && d<=21 && m==6){
//                 printf("Géminis");
//             }
//             else if (d>=22 && m ==6 || d>=1 && d<=21 && m==7){
//                 printf("Cancer");
//             }
//             else if (d>=22 && m==7 || d>=1 && d<=21 && m==8){
//                 printf("Leo");
//             }
//             else if (d>=22 && m==8 || d>=1 && d<=22 && m==9){
//                 printf("Virgo");
//             }
//             else if (d>= 23 && m==9 || d>=1 && d<=22 && m==10){
//                 printf("Libra");
//             }
//             else if (d>=23 && m==10 || d>=1 && d<=21 && m==11){
//                 printf("Escorpio");
//             }
//             else if (d>=22 && m==1 || d>=1 && d<=21 && m==12){
//                 printf("Sagitario");
//             }
//             }
//     else{
//         printf("Datos incorrectos");
//     }}
// }
//EJERCICIO 7
// int main(){
//     int x;
//     printf("Ingrese un año: ");
//     scanf("%d", &x);
//     if (x%4 ==0 && x%100 != 0){
//         printf("Año Bisiesto");
//     }
//     else if ( x%400 == 0){
//         printf("Año bisiesto");
//     }
//     else{
//         printf("No es bisiesto");
//     }
// }
//EJERCICIO 8
// int main(){
//     int x;
//     printf("Ingrese la edad:");
//     scanf("%d",&x);
//     if (x >64 ){
//         printf("Seguridad Social");
//     }
//     else if (x<18){
//         printf("Exento");
//     }
// }
//----BUCLE WHILE
//EJERCICIO 9
// int main(){
//     int i = 100;
//     while (i>=1){
//         printf("n = %d\n",i);
//         i--;
//     }
// }
//EJERCICIO 10
// int main(){
//     int i = 1;
//     while (i<100){
//         if( !(i % 2 ==0)){
//             printf("n= %d\n",i);
//         }
//     i++;
//     }
// }
//EJERCICIO 11
// int main(){
//     int x,y;
//     printf("Ingrese el primer numero:\n");
//     printf("Ingrese el segundo numero:\n");
//     scanf("%d%d",&x,&y);
//     while (x<=y){
//         printf("%d\n",y);
//         y--;
//     }
// }
//EJERCICIO 12
// int main(){
//     int x;
//     printf("Ingrese un numero: ");
//     scanf("%d",&x);
//     int i = 1;
//     int divisores =0;
//     while(i<=x){
//         if (x % i == 0){
//             ++divisores;
//         }
//         ++i;
//     }
//     if (divisores == 2){
//         printf("Primo");
//     }
//     else{
//         printf("No es primo");
//     }
// }
// //EJERCICIO 13
// int main(){
//     int x;
//     printf("Ingrese un numero: ");
//     scanf("%d",&x);
//     int i = 1;
//     while(x!=0){
//         i = i*x;
//         x = x-1;
//     }
//     printf("El factorial es%d",i);
// }

//-----FUNCIONES
//EJERCICIO 15
// int max(int param1, int param2){
//     if (param1>param2){
//         return param1;
//     }
//     else if (param2>param1)
//     {
//         return param2;
// }
// int main(){
//     int num1, num2;
//     printf("Ingrese el primer numero:\n");
//     printf("Ingrese el segundo numero:\n");
//     scanf("%d%d",&num1,&num2);

//     int resultado = max(num1,num2);
//     printf("El maximo es %d",resultado);
//     return 0;
// }
//EJERCICIO 16

//ladosTriangulos: int int int -> int 

// int ladosTriangulos(int l1,int l2,int l3){
//     int maximo = max(l1,max(l2,l3));
//     if (maximo == l1){
//         int suma = l2 + l3;
//         if (suma > l1){
//             return 1;
//         }
//         else {
//             return 0;
//         } 
//     }
    
//     else if (maximo == l2){
//         int suma = l1 + l3;
//         if (suma > l2){
//             return 1;
//         }
//         else {
//             return 0;
//         }
//     }

//     else{
//         int suma = l1 + l2;
//         if (suma > l3){
//             return 1;
//         }
//         else {
//             return 0;
//         }
//     }
// }

// //EJERCICIO 17
// int Max3(int param1, int param2, int param3);
// int esRectangulo(int x, int y, int z);

// int main(){
//     int n1,n2,n3;
//     printf("Escribe tres numeros: ");
//     scanf("%d %d %d",&n1,&n2,&n3);
//     int maximo = Max3(n1,n2,n3);
//     int rectangulo = esRectangulo(n1,n2,n3);
//     printf("El maximo de los tres es %d",maximo);
//     printf("\nSe verifica que %d",rectangulo);
//     return 0;
// }
// int Max3(int param1, int param2, int param3){
//     int max;
//     if (param1> param2 && param1> param3){
//         return param1;
//     }
//     else if (param2> param1 && param2>param3){
//         return param2;
//     }
//     else if (param3> param1 && param3>param2){
//         return param3;
//     }
// }
// int esRectangulo(int x, int y, int z){
//     int maximo = Max3(x,y,z);
//     if (maximo*maximo> (y*y + z*z)){
//         return 1;
//     }
//     else if (maximo*maximo > (z*z + x*x)){
//         return 1;
//     }
//     else if (maximo*maximo> (y*y + x*x)){
//         return 1;
//     }
//     else{
//         return 0;
//      }
//  }
//EJERCICIO 18
int Fibonacci(int n){
    if (n==0){
        return 0;
    }
    else if (n==1){
        return 1;
    }
    else{
        return (Fibonacci(n-1)+ Fibonacci(n-2)); 
    }
}
int main(){
    int num;
    printf("Ingrese un numero: ");
    scanf("%d",&num);
    int resultado = Fibonacci(num);
    printf("Segun la sucesion de Fibonacci es %d",resultado);
    return 0;
}