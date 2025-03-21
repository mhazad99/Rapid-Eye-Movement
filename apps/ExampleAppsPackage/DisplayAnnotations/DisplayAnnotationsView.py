"""
@ Valorisation Recherche HSCM, Societe en Commandite – 2024
See the file LICENCE for full license details.
"""
DEBUG = False
from PySide2.QtWidgets import QMessageBox
from qtpy import QtWidgets

from ExampleAppsPackage.DisplayAnnotations.Ui_DisplayAnnotationsView import Ui_DisplayAnnotationsView
from CEAMSModules.PSGReader.PSGReaderManager import PSGReaderManager

class DisplayAnnotationsView(Ui_DisplayAnnotationsView, QtWidgets.QWidget):
    """
    """
    def __init__(self, managers, params, **kwargs):
        super().__init__(**kwargs)
        self._managers = managers
        self._params = params

        # init UI
        self.setupUi(self)

        # Create control buttons to the navigation bar
        self._navigation_button1 = QtWidgets.QPushButton("Open File")
        self._managers.navigation_manager.add_app_widget(self._navigation_button1)
        self._navigation_button1.clicked.connect(self.slot_navigation_button1)

        # Look if the app is opened by the file menu.
        if params is not None and "startup_action" in params and params["startup_action"] == "open_file":
            self._open_file()


    def close_app(self):
        # Remove the widget added to the navigation bar 
        #   otherwise they will be added each time you open the app
        self._managers.navigation_manager.remove_app_widget(self._navigation_button1)


    def is_dirty(self):
        return False


    # Slot definition to handle the button from the navigation bar
    def slot_navigation_button1(self):
        self.lineEdit.setText("button1 from navigation bar pressed")  
        self._open_file()


    def slot_UI_buttonA(self):
        self.lineEdit.setText("buttonA from app UI pressed")  
    

    def _ask_user_file(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        psg_reader_manager = PSGReaderManager()
        psg_reader_manager._init_readers()
        dlg.setNameFilters(psg_reader_manager.get_file_extensions_filters())

        if dlg.exec_():
            filenames = dlg.selectedFiles()
            return filenames[0]
        return None


    def _open_file(self):
        filename = self._ask_user_file()
        if filename is not None:
            self._current_filename = filename

            psg_reader_manager = PSGReaderManager()
            psg_reader_manager._init_readers()
            psg_reader_manager.open_file(filename)
            self._events = psg_reader_manager.get_events() # Type DataFrame
            psg_reader_manager.close_file()

            self.write_df_to_qtable(self._events, self.tableWidget)

            log_msg = QMessageBox()
            log_msg.setWindowTitle("Information")
            log_msg.setText("File loaded")
            log_msg.setIcon(QMessageBox.Information)
            log_msg.exec_()


    def write_df_to_qtable(self, df, table):
        headers = list(df)
        table.setRowCount(df.shape[0])
        table.setColumnCount(df.shape[1])
        table.setHorizontalHeaderLabels(headers)        

        # getting data from df is computationally costly so convert it to array first
        df_array = df.values
        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(str(df_array[row,col])))