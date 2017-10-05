#include <locale.h>
#include <unistd.h>
#include <stdio.h>
#include <wchar.h>      /* wint_t */

void poly_putchar(char c){
    write(1, &c, 1);
}

int main(int argc, char **argv){
    int i;

    i = 1;
    while(i < argc)
    {
        while(*argv[i]){
            if(*argv[i] >= 'A' && *argv[i] <= 'z'){
                setlocale(LC_ALL, "");
                printf("%lc", (wint_t)(*argv[i]+65248));
            }
            else
                poly_putchar(*argv[i]);
            argv[i]++;
        }
        i++;
    }

    printf("\n");
    return 0;
}
