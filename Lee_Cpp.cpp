#include <stdlib.h>
#define EXPORT

// 컴파일 명령어
// g++ -shared -fPIC -o C_Python4.so C_Python4.cpp

extern "C"
{
    EXPORT int* lee_matrix_mul(int* a, int* b, int cnt1, int cnt2){
        int* ret = (int*)malloc(sizeof(int) * cnt1 * cnt2 + 1);

        for(int i=0; i<cnt1; i++){
            for(int j=0; j<cnt2; j++){
                int sum = 0;
                for(int k=0; k<cnt1; k++){
                    sum = sum + a[i * cnt1 + k] * b[k * cnt1 + j];
                }
                ret[i * cnt1 + j] = sum;
            }
        }

        ret[9] = '\0';
        return ret;
    }
}
