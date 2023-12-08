#include <stdio.h>
#include <conio.h>
#include <graphics.h>

struct Vertex {
    int x, y, z;
};

struct Polygon {
    int v1, v2, v3;
};

void drawPolygon(struct Vertex vertices[], struct Polygon polygon) {
    line(vertices[polygon.v1].x, vertices[polygon.v1].y, vertices[polygon.v2].x, vertices[polygon.v2].y);
    line(vertices[polygon.v2].x, vertices[polygon.v2].y, vertices[polygon.v3].x, vertices[polygon.v3].y);
    line(vertices[polygon.v3].x, vertices[polygon.v3].y, vertices[polygon.v1].x, vertices[polygon.v1].y);
}

void painterAlgorithm(struct Vertex vertices[], struct Polygon polygons[], int numPolygons) {
    int i;
    for (i = 0; i < numPolygons; i++) {
	setcolor(i+2);

	drawPolygon(vertices, polygons[i]);
    }
}

int main() {
	struct Vertex vertices[4];
	struct Polygon polygons[2];
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\Turboc3\\BGI");


    vertices[0].x = 100; vertices[0].y = 100; vertices[0].z = 0;
    vertices[1].x = 200; vertices[1].y = 100; vertices[1].z = 2;
    vertices[2].x = 200; vertices[2].y = 200; vertices[2].z = 1;
    vertices[3].x = 100; vertices[3].y = 200; vertices[3].z = 3;


    polygons[0].v1 = 0; polygons[0].v2 = 1; polygons[0].v3 = 2;
    polygons[1].v1 = 1; polygons[1].v2 = 2; polygons[1].v3 = 3;

    cleardevice();

    painterAlgorithm(vertices, polygons, 2);

    getch();
    closegraph();
    return 0;
}