#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


int n = 1;
int u = 1;
int v = 1;
int w = 1;
int z = 1;
int dim = 1;
int total_primes_diag = 0;
int diag_size = 1;

void update(){
    int new_n = n + 1;


    dim = 2 * new_n - 1;
    v = u + 1 + dim - 2;
    w = v + dim - 1;
    z = w + dim - 1;
    u = z + dim - 1;

    n = new_n;


};


int * sieve(int b){

    static int * primes;
    primes = (int *)malloc(sizeof(int) * (b+1));

    for(int i=0; i<=b; i++){
        primes[i] = 1;
    };

    primes[0] = 0;
    primes[1] = 0;

    int p = 2;
    while(p * p <= b){
        if(primes[p] == 1){
            int k = p * p;
            while(k <= b){
                primes[k] = 0;
                k += p;
            };
        };
        p += 1;
    };

    return(primes);

};



int main(){

    double ratio = 1.0;

    int b = 1000 * 1000 * 1000;
    int * primes = sieve(b);
    printf("Found primes until %d \n", b);

    while(ratio >= 0.1){
        update();


        if(primes[u] == 1){
            total_primes_diag += 1;
        };
        if(primes[v] == 1){
            total_primes_diag += 1;
        };
        if(primes[w] == 1){
            total_primes_diag += 1;
        };
        if(primes[z] == 1){
            total_primes_diag += 1;
        };

        diag_size += 4;

        ratio = (double) total_primes_diag / diag_size;

        if(n % 100 == 0){
            printf("n %d - u %d - v %d - w %d - z %d - ratio=%d/%d = %f \n",
            n, u, v, w, z, total_primes_diag, diag_size, ratio);
        };

    };

    printf("n %d - u %d - v %d - w %d - z %d - ratio=%d/%d = %f \n",
    n, u, v, w, z, total_primes_diag, diag_size, ratio);


};