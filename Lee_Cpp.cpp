#include <stdlib.h>
#define EXPORT

extern "C"
{
    EXPORT int* lee_matrix_mul(int* a, int* b, int row, int col){
        int* ret = (int*)malloc(sizeof(int) * row * col + 1);

        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                int sum = 0;
                for(int k=0; k<row; k++){
                    sum = sum + a[i * row + k] * b[k * row + j];
                }
                ret[i * row + j] = sum;
            }
        }

        ret[row * col] = '\0';
        
        return ret;
    }
}
