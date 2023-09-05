import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg,
                                                NavigationToolbar2QT)
from matplotlib.figure import Figure


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class GraphWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([1.0, 2.0, 3.0, 4.0, 5.0], [1.0, 4.0, 9.0, 16.0, 25.0])

        # Create toolbar, passing canvas as the first parameter
        # and parent (self, the MainWindow) as the second.
        toolbar = NavigationToolbar2QT(self.sc, self)

        actions = toolbar.actions()
        for action in actions:
            # print(action.text())
            if action.text() in ['Customize', 'Subplots']:
                toolbar.removeAction(action)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)

        self.sc.axes.set_xlabel('X-axis')
        self.sc.axes.set_ylabel('Y-axis')

        self.setCentralWidget(widget)
        self.plot_data([1.0, 2.0, 3.0, 4.0, 5.0],
                       [1.0, 4.0, 9.0, 16.0, 25.0])

    def plot_data(self, x_axes, y_axes):
        self.sc.axes.plot(x_axes, y_axes)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GraphWindow()
    ex.show()
    sys.exit(app.exec())
