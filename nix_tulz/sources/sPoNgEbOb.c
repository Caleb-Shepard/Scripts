#include <stdio.h>

void stupify(char *str){
    int modulate;

    modulate = 1;
    while(*str){
        // if it's a letter, alternate
        if(*str > 64 && *str < 123){
            // logical optimization, still checking
            if(*str < 91 || *str > 96){
                modulate %= 2;

                if(!modulate && *str > 96)
                    printf("%c", *str - 32);
                else if(modulate && *str < 91)
                    printf("%c", *str + 32);
                else
                    printf("%c", *str);

                modulate++;
            }
        }
        else
            printf("%c", *str);

        str++;
    }
}

int main(int argc, char **argv){
    if(argc > 1)
        stupify(argv[1]);
    printf("\n");

    return 0;
}
