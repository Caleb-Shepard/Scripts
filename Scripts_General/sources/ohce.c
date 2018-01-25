#include "unistd.h"
#include "string.h"

// This is a spartan version of echo, backwards
int main(int argc, char **argv){
    int argz;
    int charz;

    argz = argc - 1;
    while(argz > 0){
        charz = strlen(argv[argz]) - 1;
        while(charz > -1){
            write(1, &argv[argz][charz], 1);
            charz--;
        }
        write(1, " ", 1);
        argz--;
    }
    write(1, "\n", 1);
}
