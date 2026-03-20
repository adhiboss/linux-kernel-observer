#include <stdio.h>

int main() {

    FILE *f;
    char buffer[256];

    printf("==== Linux Kernel Telemetry ====\n\n");

    printf("Kernel Version:\n");
    f = fopen("/proc/version","r");
    fgets(buffer,256,f);
    printf("%s\n",buffer);
    fclose(f);

    printf("System Load:\n");
    f = fopen("/proc/loadavg","r");
    fgets(buffer,256,f);
    printf("%s\n",buffer);
    fclose(f);

    printf("Memory Info:\n");
    f = fopen("/proc/meminfo","r");

    for(int i=0;i<5;i++){
        fgets(buffer,256,f);
        printf("%s",buffer);
    }

    fclose(f);

    return 0;
}
