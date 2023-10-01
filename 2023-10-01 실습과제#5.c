#include <stdio.h>

int main() {
    char name[100];
    int student_id;
    char department[100];

    printf("이름을 입력하세요: ");
    scanf("%s", name);

    printf("학번을 입력하세요: ");
    scanf("%d", &student_id);

    printf("학과를 입력하세요: ");
    scanf("%s", department);

    printf("이름: %s\n", name);
    printf("학번: %d\n", student_id);
    printf("학과: %s\n", department);

    return 0;
}
