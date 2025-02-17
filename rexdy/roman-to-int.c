#include <string.h>

int rti(char c){
    switch(c){
        case 'I':
        case 'i':
        return 1;
        case 'V':
        case 'v':
        return 5;
        case 'X':
        case 'x':
        return 10;
        case 'L':
        case 'l':
	return 50;
        case 'C':
        case 'c':
        return 100;
        case 'D':
        case 'd':
        return 500;
        case 'M':
        case 'm':
        return 1000;
        default:
        return -1;
    }
    return -1;
}

int romanToInt(char* s) {
    int len = strlen(s);
    int sum = rti(s[len-1]);

    for(int i=len-2; i>=0; i--){
        if(rti(s[i])<rti(s[i+1])){
            sum-=rti(s[i]);
        }
        else{
            sum+=rti(s[i]);
        }
    }
    return sum;
}
