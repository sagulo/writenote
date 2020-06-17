# coding: utf-8
import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QFileDialog, QTextEdit, QMenu, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QToolBar
import os
# from PyQt5.QtGui import QIcon
# from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTextEdit,QMainWindow,QTextEdit,QLineEdit, QLabel,QVBoxLayout,QWidget,QApplication,QDesktopWidget,QAction,qApp,QTreeWidget,QHeaderView,QTreeWidgetItem,QDockWidget,QTabWidget,QMessageBox,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QPixmap
import chardet

getRunPath = os.path.split(os.path.realpath(__file__))[0]
getPath = os.getcwd()
class MainWindows(QMainWindow):
    
    def __init__(self):
        super().__init__()        
        self.tabList = [0]
        self.L1 = []
        self.L2 = []
        self.initUI()
        self.createTab()

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))  
        if action == quitAct:
            qApp.quit()

    # def closeEvent(QDockWidget, event):
    #     print("11")

    def resizeEvent(self, evt):
        x1 = 1
        window = self.geometry()
        windowwidth = window.width()
        windowheight=window.height()
        if x1 == 1:
            if windowwidth == 960 and windowheight == 540:
                self.statusbar.showMessage("Ready")
                x1 = 2
            else:
                self.statusbar.showMessage("{},{}".format(windowwidth,windowheight),1000)

    def createTab(self):
        self.qwidget1 = QWidget()
        self.setCentralWidget(self.qwidget1)
        self.text2 = QTextEdit()
        self.text3 = QTextEdit()
        # # self.text2.setAlignment(Qt.AlignCenter)
        # # self.setCentralWidget(self.text2)
        
        self.tab1 = QTabWidget(self.qwidget1)
        self.tab1.setMovable(True)
        self.tab1.setTabShape (QTabWidget.Triangular)# 三角，0，默认
        self.tab1.setTabsClosable(True)
        self.tab1.addTab(self.text2,"untitled.txt")
        self.tab1.setTabText(0, "untitled.txt")
        self.untitled_tabwidget = self.tab1.currentWidget()
        self.untitled_tabwidget.setObjectName('untitled')
        # untitled = self.tab1.tabBar()
        # untitled.addTab("untitled.txt")

        self.untitled = QTreeWidgetItem(self.opening)
        self.untitled.setText(0,"untitled.txt")
        self.untitled.setText(1,'0')

        
        # 标签图标
        # self.tab1.addTab(self.text3,QIcon("{}\\icon\\quan.png".format(self.getRunPath)),"Tab 2")
        self.tab1.setTabPosition(QTabWidget.North)
        self.setCentralWidget(self.tab1)

        self.tab1.currentChanged[int].connect(self.on_currentChanged)
        self.tab1.tabCloseRequested.connect(self.closeTab)

    def on_currentChanged(self, index):
        print("current tab index:", index)
    
    def on_visibilityChanged(self, visible):
        print(visible)

    def closeTab(self, index):
        print(index)
        self.tab1.removeTab(index)

        
    def createMenuBar(self):
        # 新建按钮
        newAct = QAction('&New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('New')
        newAct.triggered.connect(self.newEdit)
        # 打开按钮
        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open')
        openFile.triggered.connect(self.openFileDialog)
        # 选择文件夹
        selectFolder= QAction('Folder', self)
        selectFolder.setShortcut('Ctrl+K')
        selectFolder.setStatusTip('Folder')
        selectFolder.triggered.connect(self.selectFolderDialog)
        # 保存按钮
        saveFile = QAction('Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save')
        saveFile.triggered.connect(self.saveFile)
        # 退出按钮
        exitAct = QAction('&Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit')
        exitAct.triggered.connect(qApp.quit)
        # 撤销按钮
        undoAct = QAction('&Undo', self)
        undoAct.setShortcut("Ctrl+Z")
        undoAct.setStatusTip('Undo')
        # 关于按钮
        aboutAct = QAction('&About', self)
        aboutAct.setStatusTip('About')
        aboutAct.triggered.connect(self.aboutMessage)
        #dock
        self.viewStatAct = QAction('Resource manager', self, checkable=True)
        self.viewStatAct.setStatusTip('Resource manager')
        self.viewStatAct.setChecked(True)
        self.viewStatAct.triggered[bool].connect(self.viewBool)

        resetAct = QAction("Reset", self)
        resetAct.setStatusTip('Reset')
        resetAct.triggered.connect(self.resetWindow)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        windowMenu = menubar.addMenu('&Window')
        # windowMenu.aboutToShow.connect(self.updateWindowMenu)
        helpMenu = menubar.addMenu('&Help')
        fileMenu.addAction(newAct)
        fileMenu.addAction(openFile)
        fileMenu.addAction(selectFolder)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(exitAct)
        editMenu.addAction(undoAct)
        helpMenu.addAction(aboutAct)
        windowMenu.addAction(self.viewStatAct)
        windowMenu.addAction(resetAct)
    # def creteToolBar(self):
    #     self.toolBar = QToolBar()
    #     #MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
    #     self.addToolBar(Qt.LeftToolBarArea,self.toolBar)
    #     L1 = []
    #     L2 = []
    #     for files in os.listdir(self.path):
    #         if os.path.isfile(files):
    #             L1.append(files)
    #         else:
    #             L2.append(files)
    #     if L1 or L2:
    #         self.Ls1 = self.insert_sort(list(L1))
    #         self.Ls2 = self.insert_sort(list(L2))
    #         for i in self.Ls2:
    #             self.toolBar.addAction(i)
    #         for i in self.Ls1:
    #             self.toolBar.addAction(i)

        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(newAct)
    def resetWindow(self):
        if self.viewStatAct.isChecked or self.dock1.isFloating():
            self.viewStatAct.setChecked(True)
            self.dock1.show()
            self.dock1.setFloating(False)
            self.setArea(Qt.LeftDockWidgetArea)
        

    def viewBool(self, b):
        if b:
            self.dock1.show()
        else:
            self.dock1.hide()

    def createTreeView(self):
        
        self.tree = QTreeWidget(self)
        
        self.tree.setColumnCount(1)
        # 表头名称
        # self.tree.setHeaderLabels(['Resource manager'])
        # 隐藏表头
        self.tree.setHeaderHidden(True)

        # 按表头排序
        # self.tree.setSortingEnabled(True)
        # self.tree.header().setHighlightSections(True)
        # 设置默认宽度
        self.tree.header().setDefaultSectionSize(30)
        self.tree.header().setSectionResizeMode(QHeaderView.Fixed)
        self.tree.header().setCascadingSectionResizes(True)
        

        self.createCwdTree(getPath)

        self.dock1 = QDockWidget('Resource manager')
        # dock1.setFeatures(QDockWidget.DockWidgetFloatable)
        self.dock1.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea | Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.dock1.visibilityChanged[bool].connect(self.on_visibilityChanged)
        # dock1.setFeatures(QDockWidget.AllDockWidgetFeatures | QDockWidget.DockWidgetVerticalTitleBar)
        # 返回该停靠窗口使用的标题栏部件
        # dock1.setTitleBarWidget(self.tree)
        # 去除顶部边框
        # titleBar=QWidget()
        # dock1.setTitleBarWidget(titleBar)
        self.dock1.setWidget(self.tree)
        # self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)
        self.setArea(Qt.LeftDockWidgetArea)
        # self.dock1.sizeHint()
        # self.dock1.adjustSize()
        self.dock1.dockLocationChanged[Qt.DockWidgetArea].connect(self.on_dockLocationChanged)

    def setArea(self, area):
        self.addDockWidget(area, self.dock1)

    def on_dockLocationChanged(self,area):
        print(area)

    def on_visibilityChanged(self, visible):
        if visible:
            self.viewStatAct.setChecked(True)
        else:
            self.viewStatAct.setChecked(False)

    def closeEvent(QDockWidget, event):
        print("1")

    def createCwdTree(self, pather):
        self.tree.clear()
        self.L1.clear()
        self.L2.clear()
        self.opening = QTreeWidgetItem(self.tree)
        self.opening.setText(0,"Opening")
        self.opening.setText(1,'0')

        workspace = QTreeWidgetItem(self.tree)
        workspace.setText(0,"Workspace")
        workspace.setText(1,'0')

        self.root = QTreeWidgetItem(workspace)
        self.root.setText(0,getPath)
        self.root.setText(1,'0')

        for files in os.listdir(pather):
            if os.path.isfile(files):
                self.L1.append(files)
            elif os.path.isdir(files):
                self.L2.append(files)
                
        if self.L1 or self.L2:
            self.Ls1 = self.merge_sort(list(self.L1))
            self.Ls2 = self.merge_sort(list(self.L2))
            for i in self.Ls2:
                locals()['Ls_'+str(i)] = QTreeWidgetItem(self.root)
                locals()['Ls_'+str(i)].setText(0,i)
                locals()['Ls_'+str(i)].setText(1,'1')
                locals()['Ls_'+str(i)].setIcon(0,QIcon("{}\\icon\\folder.png".format(getRunPath)))
            for i in self.Ls1:
                locals()['Ls_'+str(i)] = QTreeWidgetItem(self.root)
                locals()['Ls_'+str(i)].setText(0,i)
                locals()['Ls_'+str(i)].setText(1,'1')
                if ".py" in i:
                    locals()['Ls_'+str(i)].setIcon(0,QIcon("{}\\icon\\python.png".format(getRunPath)))
                elif ".txt" in i:
                    locals()['Ls_'+str(i)].setIcon(0,QIcon("{}\\icon\\txt.png".format(getRunPath)))
                elif ".xml" in i:
                    pass    
                else:
                    locals()['Ls_'+str(i)].setIcon(0,QIcon("{}\\icon\\other.png".format(getRunPath)))
        self.tree.addTopLevelItem(self.root)
        self.tree.clicked.connect(self.onTreeClicked)
        self.tree.expandAll()
        
    def onTreeClicked(self, qmodelindex):
        try:
            item = self.tree.currentItem()
            print("key=%s ,value=%s" % (item.text(0), item.text(1)))
            if os.path.isfile(item.text(0)):
                self.textEdit = QTextEdit()
                self.tab1.addTab(self.textEdit,item.text(0))
                if item.text(0) and item.text(0)[-4:] != '.exe':
                    on = open(item.text(0), 'r', encoding=self.get_encoding(item.text(0)))
                    with on:
                        data = on.read()
                        self.textEdit.setText(data)
        except Exception as e:
                QMessageBox.warning(self, 'warning', "{}".format(e), QMessageBox.Yes)
	
    def addTreeNodeBtn(self):
        print('--- addTreeNodeBtn ---')
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0,'newNode')
        node.setText(1,'10')
        
    def updateTreeNodeBtn(self):
        print('--- updateTreeNodeBtn ---')
        item = self.tree.currentItem()
        item.setText(0,'updateNode')
        item.setText(1,'20')
        
    def delTreeNodeBtn(self):
        print('--- delTreeNodeBtn ---')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)
            
    def initUI(self):
        # 获取桌面像素
        screen = QDesktopWidget().screenGeometry()
        self.createMenuBar()
        self.createTreeView()
        self.statusbar = self.statusBar()
        # label4.setScaledContents (True) # 自适应
        # self.setGeometry(x/4, y/4, x/2, y/2)
        self.resize(screen.width()/2, screen.height()/2)
        self.setWindowTitle("writenote")    
        self.setWindowIcon(QIcon(QIcon("{}\\icon\\writenote.png".format(getRunPath))))
        self.show()

    def onDockListIndexChanged(self, index):
        item = self.items[index]
        self.text2.setText(item)

    def aboutMessage(self):
        self.about_window = AboutMessage()
        self.about_window.show()

    def updateWindowMenu(self):
        pass
        

    def toggleMenu(self, state):
        x = 0
        for w in QApplication.topLevelWidgets():
            x = x + 1
        print(x)
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def selectFolderDialog(self):
        try:
            folderPath = QFileDialog.getExistingDirectory(self, '选取文件', './')
            if folderPath == "":
                return
            else:
                getPath = folderPath
                # 更改工作目录
                os.chdir(getPath)
                self.root.setText(0,getPath)
                self.createCwdTree(getPath)
                # 展开所有节点
                self.tree.expandAll()
        except Exception as e:
            QMessageBox.warning(self, 'warning', "{}".format(e), QMessageBox.Yes)

    def openFileDialog(self):
            try:
                oname = QFileDialog.getOpenFileName(self, 'Open file', './', "Text file (*.txt);;Python file (*.py)")
                if len(oname[0]) == 0:
                    return
                else:
                    self.textEdit = QTextEdit()
                    self.tab1.addTab(self.textEdit,oname[0])
                    locals()[str(oname[0])] = QTreeWidgetItem(self.opening)
                    locals()[str(oname[0])].setText(0,oname[0])
                    locals()[str(oname[0])].setText(1,'0')
                    print(oname[0])
                    if oname[1]:
                        if oname[0]:
                            self.setWindowTitle("{}-writenote".format(oname[0]))
                            on = open(oname[0], 'r', encoding="utf-8")

                            with on:
                                data = on.read()
                                self.textEdit.setText(data)
            except Exception as e:
                QMessageBox.warning(self, 'warning', "{}".format(e), QMessageBox.Yes)

    def newEdit(self):
        self.tabList.append(self.tabList[-1]+1)
        locals()['untitled{}_textedit'.format(self.tabList[-1])] = QTextEdit()

        # locals()['untitled{}_tabwidget'.format(self.tabList[-1])] = self.tab1.currentWidget()
        # locals()['untitled{}_tabwidget'.format(self.tabList[-1])].setObjectName("'untitled{}_tabwidget'.format(self.tabList[-1])")
        
        

        self.tab1.addTab(locals()['untitled{}_textedit'.format(self.tabList[-1])],"untitled({}).txt".format(self.tabList[-1]))

        locals()['untitled{}_textedit'.format(self.tabList[-1])] = QTreeWidgetItem(self.opening)
        locals()['untitled{}_textedit'.format(self.tabList[-1])].setText(0,"untitled({}).txt".format(self.tabList[-1]))
        locals()['untitled{}_textedit'.format(self.tabList[-1])].setText(1,'0')
        # self.setCentralWidget(self.newTextEdit)
        # textLabel = QLabel("1")
        # self.textLineEdit = QLineEdit()
        
    def saveFile(self):
        fileName2, ok2 = QFileDialog.getSaveFileName(self,
            "Save File",
            getPath+'/untitled.txt',
            "Text Files (*.txt)")
        
        if not fileName2:
            return
        else:
            f = open(fileName2, "w", encoding="utf-8")
            f.write(self.textEdit.toPlainText())

    # def insert_sort(self, lists):
    #     count = len(lists)
    #     for i in range(1, count):
    #         key = lists[i]
    #         j = i - 1
    #         while j >= 0:
    #             if lists[j] > key:
    #                 lists[j + 1] = lists[j]
    #                 lists[j] = key
    #             j -= 1
    #     return lists
    
    def clicked(self,qModelIndex):
        #提示信息弹窗，你选择的信息
        QMessageBox.information(self,'ListWidget','你选择了：'+self.qList[qModelIndex.row()])

    def get_encoding(self,filename):
        with open(filename,'rb') as f:
            tmp = chardet.detect(f.read(2))
        return tmp['encoding']

    def merge_sort(self,nums):
        import math
        if len(nums) < 2:
            return nums
        middle = math.floor(len(nums)/2)
        left, right = nums[0:middle], nums[middle:]
        return self.merge(self.merge_sort(left), self.merge_sort(right))

    def merge(self,left, right):
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))

        return result


class AboutMessage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About Me") 
        self.setFixedSize(300,300)
        # 取消放大缩小按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon(QIcon("{}\\icon\\writenote.png".format(getRunPath))))
        abountPix = QPixmap("{}\\icon\\about.jpg".format(getRunPath)).scaled(300, 300, Qt.IgnoreAspectRatio)
        aboutPixLabel = QLabel(self)
        aboutPixLabel.setPixmap(abountPix)
        aboutPixLabel.setScaledContents(True)

        aboutLabel = QLabel(self)
        aboutLabel.setText("Simply Playing")
        # 居中
        aboutLabel.setAlignment(Qt.AlignCenter)
        self.v_layout = QVBoxLayout(self)
        self.v_layout.addWidget(aboutPixLabel)
        self.v_layout.addWidget(aboutLabel)
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindows()
    sys.exit(app.exec_())
