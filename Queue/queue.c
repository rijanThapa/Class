#include<stdio.h>
#include<conio.h>
#include<process.h>
#define max 5

int rear=0, front=0;
int queue[max];

void enqueue() {
    if(rear==max)
        printf("The queue is full\n");
    else {
        int a;
        printf("Enter the data to be inserted\n");
        scanf("%d", &a);
        queue[rear] = a;
        rear = rear + 1;
    }
}

void dequeue() {
    if(rear==front)
        printf("The queue is empty\n");
    else {
        printf("The data deleted from the queue is %d\n", queue[front]);
        front++;
    }
}

void display() {
    if (front == rear)
        printf("The queue is empty\n");
    else {
    	int i;
        printf("Elements in the queue are:\n");
        for ( i = front; i < rear; i++)
            printf("%d ", queue[i]);
        printf("\n");
    }
}

int main() {
    int choice;
    do {
        printf("\nEnter your choice:\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit\n");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                enqueue();
                break;

            case 2:
                dequeue();
                break;

            case 3:
                display();
                break;

            case 4:
                exit(0);
        }
    } while(choice <= 4);
    
    return 0;
}

