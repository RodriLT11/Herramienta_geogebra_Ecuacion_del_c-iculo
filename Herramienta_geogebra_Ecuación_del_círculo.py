# importing various libraries
import sys
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtGui import (QIcon, QPixmap, QFont)
from random import *
import matplotlib.pyplot as plt



class Window(QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        
        self.figure = plt.figure()

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Crear circulo')
        self.button.clicked.connect(self.add_circ)
        self.label = QLabel('(x-h)^2 + (y-k)^2 = r^2', self)
        self.lbl_count = QLabel('Ecuacion')
        self.btn_button = QPushButton('Valores sustituidos en la ecuacion')
        self.btn_button.clicked.connect(self.ecu_ci)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        layout.addWidget(self.btn_button)
        layout.addWidget(self.label)
        layout.addWidget(self.lbl_count)

        self.setLayout(layout)
         
        self.cen1 = 0
        self.cen2 = 0
        
        
    def add_circ(self):
         
        self.angulo = np.linspace( 0 , 2 * np.pi , 150 )
        self.radius = randrange(-1000,1000,1)
        
        self.c1 = randrange(-1000,1000,1)
        self.c2 = randrange(-1000,1000,1)  
        
        self.x = self.c1 + self.radius * np.cos(self.angulo)
        self.y = self.c2 + self.radius * np.sin(self.angulo)
        
    
        self.c1 = int(self.c1)
        self.c2 = int(self.c2)
        
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)      
        self.ax.plot( self.x, self.y )
        
        self.a = randrange(-1000, 1000, 1)
        self.b = randrange(-1000, 1000, 1)
        plt.plot([self.a], [self.b])
        
        self.ax.spines['left'].set_position('center')
        self.ax.spines['bottom'].set_position('center')
        
        self.canvas.draw()
        #plt.show()

    def ecu_ci(self):
   
            self.cen1 += self.c1
            self.cen2 += self.c2
            self.cen1_str = str(self.cen1)
            self.cen2_str = str(self.cen2)
            self.radius_str = str(self.radius)
            
            self.lbl_count.setText("(x" + "+" + "(" + self.cen1_str + "))^2 " + "+" +  "(y" +"+" + "(" + self.cen2_str + "))^2" + "=" + "(" + self.radius_str +  ")^2 ")
                    
            self.cen1 = 0
            self.cen2 = 0
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())