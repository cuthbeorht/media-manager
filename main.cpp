#include <QApplication>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    QPushButton button("Hello M1 Mac World!");
    button.resize(300, 100);
    button.show();

    return app.exec();
}
