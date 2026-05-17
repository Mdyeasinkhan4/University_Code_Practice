#include <graphics.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>

int main() {
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    setbkcolor(BLACK);
    cleardevice();

    srand(time(0));

    int x[100], y[100];
    int dx[100];

    int maxx = getmaxx();
    int maxy = getmaxy();
    int ground = maxy - 100;

    for (int i = 0; i < 100; i++) {
        x[i] = rand() % maxx;
        y[i] = rand() % maxy;
        dx[i] = (rand() % 3) + 2;
    }

    while (!kbhit()) {
        cleardevice();


        setfillstyle(SOLID_FILL, DARKGRAY);
        bar(0, ground, maxx, maxy);

        setcolor(WHITE);
        line(0, ground, maxx, ground);


        for (int i = 0; i < maxx; i += 40) {
            line(i, ground + 50, i + 20, ground + 50);
        }

        setcolor(LIGHTCYAN);
        for (int i = 0; i < 100; i++) {
            line(x[i], y[i], x[i] + dx[i], y[i] + 10);

            y[i] += 10;
            x[i] += dx[i];

            if (y[i] > maxy || x[i] > maxx) {
                y[i] = 0;
                x[i] = rand() % maxx;
                dx[i] = (rand() % 3) + 2;
            }
        }

        delay(50);
    }

    closegraph();
    return 0;
}