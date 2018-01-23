#include <locale.h>
#include <stdio.h>
#include <wchar.h>

int main(int argc, char **argv){
    int i;

    i = 1;
    while(i < argc){
        while(*argv[i]){
            if(*argv[i] >= 'A' && *argv[i] <= 'z'){
                setlocale(LC_ALL, "");
                printf("%lc", (wint_t)(*argv[i]+65248));
            }
            else
                printf("%c", *argv[i]);
            argv[i]++;
        }
        i++;
    }

    printf("\n");
    return 0;
}
