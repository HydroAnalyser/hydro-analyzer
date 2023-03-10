from PySide6.QtWidgets import QWidget

from HyAn.ui.ui_analysis import Ui_Analysis
from PySide6.QtCore import Slot

class Analysis(QWidget, Ui_Analysis):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.btn_fit.clicked.connect(self.fit_theis)

    @Slot(list)
    def fit_data(self, data):
        print(f"fit_data: {data}")
        self.theis_data = data
        self.btn_fit.setEnabled(True)
        #self.wid_analysis_graph.thies_analysis(self.theis_data)
        
    def fit_theis(self):
        self.wid_analysis_graph.thies_analysis(self.theis_data)
        S = round(self.wid_analysis_graph.S, 4)
        T = round(self.wid_analysis_graph.T, 4)
        self.l_edit_output_storativity.setText(str(S))
        self.l_edit_output_transmissivity.setText(str(T))
