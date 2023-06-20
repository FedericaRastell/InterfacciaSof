# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass


from PySide6.QtGui import QImage, QPixmap, QPainter,QPen, QTransform
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QVBoxLayout,QCheckBox,QDialogButtonBox, QRadioButton, QLabel
from PySide6.QtGui import QAction



class ClassificationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Image Classification')

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Classify Image:')
        layout.addWidget(label)

        self.button_negative = QRadioButton('Negative')
        layout.addWidget(self.button_negative)

        self.button_doubtful = QRadioButton('Doubtful')
        layout.addWidget(self.button_doubtful)

        self.button_suspicious = QRadioButton('Suspicious')
        layout.addWidget(self.button_suspicious)

        self.button_carcinoma = QRadioButton('Carcinoma')
        layout.addWidget(self.button_carcinoma)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)


class ImageViewer(QtWidgets.QMainWindow):

    def __init__(self, qlabel, list_widget):
        super().__init__()
        self.qlabel_image = qlabel
        self.list_widget = list_widget
        self.qimage_scaled = QImage()
        self.current_image=QImage()
        self.qpixmap = QPixmap()
        self.zoom = 1
        self.anchor=None
        self.pressed=None
        self.position = QPoint(0, 0)
        self.selected_area_is_displayed = False
        self.click_pos_image=QPoint(0,0)
        self.selection_rect = QtCore.QRect()
        self.statusbar = self.statusBar()
        self.qlabel_image.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        self.__connectEvents()



    def __connectEvents(self):
        # Mouse events
        self.qlabel_image.mousePressEvent = self.mousePressAction
        self.qlabel_image.mouseMoveEvent = self.mouseMoveAction
        self.qlabel_image.mouseReleaseEvent = self.mouseReleaseAction
        self.qlabel_image.mouseDoubleClickEvent=self.mouseDoubleClickAction
        self.list_widget.itemClicked.connect(self.onListItem_click)



    def loadImage(self, imagePath):
        ''' Per caricare e mostrare un'immagine presente nella lista dei files che apro tramite il tasto openFolder.'''
        self.qimage = QImage(imagePath)
        if not self.qimage.isNull():
            # reset Zoom factor and Pan position
            self.zoom = 1
            self.position = QPoint(0, 0)
            self.qimage_scaled = self.qimage.scaled(self.qlabel_image.width(), self.qlabel_image.height(), QtCore.Qt.IgnoreAspectRatio) #per scalare le dimensioni dell'immagine alle dimensioni della QLabelWidget
            self.qlabel_image.setPixmap(QtGui.QPixmap.fromImage(self.qimage_scaled)) #per mostrare l'immagine scalata alle dimensioni della QLabelWidget nella QLabelWidget
            self.qpixmap=QPixmap(self.qimage)
            self.current_image=self.qimage_scaled

        else:
            self.statusbar.showMessage('Cannot open this image! Try another one.', 5000)


    def update(self):
        if not self.qimage.isNull():

            # Calcola la dimensione scalata dell'immagine a seconda del fattore di zoom
            scaled_width = self.qimage_scaled.width() * self.zoom
            scaled_height = self.qimage_scaled.height() * self.zoom

            # Calcola la posizione centrale dell'immagine scalata in base al fattore di zoom
            center_x = scaled_width / 2
            center_y = scaled_height / 2

            # Calcola la posizione in alto a sinistra dell'immagine per poi disegnare l'immagine tenendo conto dello zoom e del pan
            top_left_x = center_x - self.qlabel_image.width() / 2 - self.position.x()
            top_left_y = center_y - self.qlabel_image.height() / 2 - self.position.y()

            #scala in base al fattore di zoom l'immagine adattata alle dimensioni della QlabelWidget
            self.current_image= self.qimage_scaled.scaled(scaled_width,scaled_height).copy(int(top_left_x),
                        int(top_left_y), self.qlabel_image.width(), self.qlabel_image.height())


            #mostra l'immagine aggiornata a seconda dello zoom e del pan nella QLabelWidget

            self.qlabel_image.setPixmap(QPixmap.fromImage(self.current_image))


        else:
              self.qlabel_image.clear()

    #le funzioni zoomIn e ZoomOut vengono richiamate dal file main dalla funzione wheelevent

    def zoomIn(self):

        self.zoom *=2
        self.update()

    def zoomOut(self):

        self.zoom /= 2
        self.update()


    def mousePressAction(self, QMouseEvent):
        #x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()

        if QMouseEvent.button() == Qt.LeftButton:
            self.pressed = QMouseEvent.pos()
            self.anchor = self.position

        elif QMouseEvent.button() == Qt.RightButton and self.selected_area_is_displayed:

            self.selected_item = self.list_widget.currentItem()

            dialog = ClassificationDialog(self)
            if dialog.exec() == QDialog.Accepted:

                # Ottieni le selezioni delle caselle di controllo

                is_negative = dialog.button_negative.isChecked()
                is_doubtful = dialog.button_doubtful.isChecked()
                is_suspicious = dialog.button_suspicious.isChecked()
                is_carcinoma = dialog.button_carcinoma.isChecked()

                #cliccando sulle caselle di controllo etichetto quell'area dell'immagine come segue
                if is_negative:
                    self.label = 'Negativo'
                elif is_doubtful:
                    self.label='Dubbioso'
                elif is_suspicious:
                    self.label='Sospetto'
                elif is_carcinoma:
                    self.label='Carcinoma'

                if self.label:
                    self.selected_item.setText(self.label)
                    pixmap = self.selected_item.icon().pixmap(QtCore.QSize(256, 256))  # Ottieni la pixmap dell'immagine annotata
                    self.saveSelectedAnnotation(pixmap, self.label)


            self.selected_area_is_displayed = False
            self.restoreCurrentImage()




    def mouseMoveAction(self, QMouseEvent):
        x, y = QMouseEvent.pos().x(), QMouseEvent.pos().y()
        if self.pressed:
            self.qlabel_image.setCursor(QtCore.Qt.ClosedHandCursor)
            dx, dy = x - self.pressed.x(), y - self.pressed.y()        # calcolare il vettore di drag
            self.position = self.anchor + QPoint(dx, dy)  # aggiorna la posizione del pan
            self.update()  # mostra l'immagine con la posizione del pan aggiornata


    def mouseDoubleClickAction(self,QMouseEvent):
        if QMouseEvent.button()==Qt.LeftButton:
            if not self.qimage.isNull():


                click_pos_image = QMouseEvent.pos()

                if self.zoom>1:

                    selection_width=40*self.zoom
                    selection_height=40*self.zoom

                elif self.zoom<1:
                    selection_width=40/self.zoom
                    selection_height=40/self.zoom

                else:
                    selection_width=40
                    selection_height=40

                selection_rect = QtCore.QRect(
                    click_pos_image.x() - (selection_width // 2),
                    click_pos_image.y() - (selection_height // 2),
                    selection_width,
                    selection_height
                )

                selected_area = self.current_image.copy(selection_rect)
                self.label='generico'
                self.saveSelectedArea(selected_area,self.label)
                image_with_selection = self.current_image.copy()

                painter = QPainter(image_with_selection)
                painter.setPen(QPen(Qt.red, 2*self.zoom, Qt.SolidLine))
                painter.drawRect(selection_rect)
                painter.end()

                self.qlabel_image.setPixmap(QPixmap.fromImage(image_with_selection))


    def mouseReleaseAction(self, QMouseEvent):
          self.pressed = None
          self.qlabel_image.setCursor(Qt.ArrowCursor)


    def saveSelectedArea(self,qimage_scaled,label):

        list_item=QtWidgets.QListWidgetItem(label)
        icon=QtGui.QIcon(QtGui.QPixmap.fromImage(qimage_scaled))
        list_item.setIcon(icon)
        self.list_widget.addItem(list_item)


    def onListItem_click(self, item):

        icon=item.icon()

        pixmap = icon.pixmap(icon.availableSizes()[0])
        resized_pixmap = pixmap.scaled(self.qlabel_image.size()/2, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.SmoothTransformation)

        self.qlabel_image.setPixmap(resized_pixmap)

        self.selected_area_is_displayed=True

    def restoreCurrentImage(self):
            self.qlabel_image.setPixmap(QPixmap.fromImage(self.current_image))

    def saveSelectedAnnotation(self, pixmap, label):
        save_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.xpm *.jpg)")
        if save_path:
            pixmap.save(save_path)



