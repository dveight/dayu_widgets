#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.2
# Email : muyanru345@163.com
###################################################################
import dayu_widgets.examples._mock_data as mock
from dayu_widgets.MDivider import MDivider
from dayu_widgets.MFieldMixin import MFieldMixin
from dayu_widgets.MItemModel import MTableModel, MSortFilterModel
from dayu_widgets.MItemView import MListView
from dayu_widgets.MLineEdit import MLineEdit
from dayu_widgets.qt import *
from dayu_widgets import dayu_theme


class MListViewTest(QWidget, MFieldMixin):
    def __init__(self, parent=None):
        super(MListViewTest, self).__init__(parent)
        self._init_ui()

    def _init_ui(self):
        table_small = MListView(size=dayu_theme.small)
        table_default = MListView()
        table_large = MListView(size=dayu_theme.large)

        model_1 = MTableModel()
        model_1.set_header_list(mock.header_list)
        model_sort = MSortFilterModel()
        model_sort.setSourceModel(model_1)
        table_small.setModel(model_sort)
        table_default.setModel(model_sort)
        table_large.setModel(model_sort)
        model_sort.set_header_list(mock.header_list)
        table_small.set_header_list(mock.header_list)
        table_default.set_header_list(mock.header_list)
        table_large.set_header_list(mock.header_list)
        model_1.set_data_list(mock.data_list)

        line_edit = MLineEdit.search(size=dayu_theme.small)
        line_edit.textChanged.connect(model_sort.set_search_pattern)

        main_lay = QVBoxLayout()
        main_lay.addWidget(line_edit)
        main_lay.addWidget(MDivider('Small Size'))
        main_lay.addWidget(table_small)
        main_lay.addWidget(MDivider('Default Size'))
        main_lay.addWidget(table_default)
        main_lay.addWidget(MDivider('Large Size'))
        main_lay.addWidget(table_large)
        main_lay.addStretch()
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MListViewTest()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
