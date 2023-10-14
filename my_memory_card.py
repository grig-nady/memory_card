from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from PyQt5.QtGui import QFont
from random import shuffle


class Question():
    def __init__(self, question, right_answer, wrong1):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1



questions_list = [] 
questions_list.append(Question('КАК ЗОВУТ ДВОРЕЦКОГО СЕМЕЙКИ АДАМС?','Ларч','Фрэнк'))
questions_list.append(Question('КЕМ ЯВЛЯЕТСЯ БЬЯНКА?','Русалкой','Вампиром'))
questions_list.append(Question('А ЧТО ЕСЛИ Я БОЛГАРКА?','Да','Нет'))
questions_list.append(Question('ПРАВДА, ЧТО УЭНСДЕЙ НЕ МОРГАЕТ?','Да','Нет'))
questions_list.append(Question('УЭНСДЕЙ ПИШЕТ КНИГУ?','Да','Нет'))
questions_list.append(Question('КАК ЗОВУТ БРАТА УЭНСДЕЙ?','Ларч','Фрэнк'))
questions_list.append(Question('КАК НАЗЫВАЕТСЯ ВТОРАЯ ГЛАВА УЭНСДЕЙ?','Одинокое число','Чудовище из Леса'))
questions_list.append(Question('КАКАЯ КОМАНДА ВЫИГРАЛА КУБОК ПО?','Черные кошки','Золотые жуки'))
questions_list.append(Question('КАК УЭНСДЕЙ ОТОМСТИЛА ХУЛИГАНАМ ЗА БРАТА?','Выпустила пираний в бассейн','Укусила хулигана'))
questions_list.append(Question('КАК ЗОВУТ СОСЕДКУ ПО КОМНАТЕ УЭНСДЕЙ','Энид','Лиза'))
questions_list.append(Question('ЭНИД НРАВИТСЯ АЯКС?','Да','Нет'))
questions_list.append(Question('ЧТО НУЖНО БЫЛО СДЕЛАТЬ, ЧТОБЫ ОТКРЫЛАСЬ ДВЕРЬ В ПОТАЙНУЮ БИБЛИОТЕКУ?','Дважды щелкнуть','Прочитать стих'))
questions_list.append(Question('КАК ЗОВУТ ОСНОВАТЕЛЯ ДЖЕРИКО?','Джозеф Крекстоун','Роберт Уилимс'))
questions_list.append(Question('МОРТИША УЧИЛАСЬ В НЕВЕРМОРЕ?','Да','Нет'))
questions_list.append(Question('МОРТИША И ДИРЕКТОР УЧИЛИСЬ ВМЕСТЕ?','Да','Нет'))
questions_list.append(Question('КСАВЬЕ ВСТРЕЧАЛСЯ С БЬЯНКОЙ?','Да','Нет'))



app = QApplication([])


btn_OK = QPushButton('Ответить') 
btn_OK.setFont(QFont("Times New Roman", 20, QFont.Bold))
lb_Question = QLabel('Самый сложный вопрос в мире!') 
lb_Question.setFont(QFont("Times New Roman", 20, QFont.Bold))

RadioGroupBox = QGroupBox("Варианты") 
RadioGroupBox.setFont(QFont("Times New Roman", 20, QFont.Bold))


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')



RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)



layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)



layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) 


RadioGroupBox.setLayout(layout_ans1) 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) 


def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    RadioGroup.setExclusive(True) 

answers = [rbtn_1, rbtn_2]


def ask(q: Question):
    shuffle(answers) 
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)

    lb_Question.setText(q.question) 
    lb_Correct.setText(q.right_answer) 
    show_question() 


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked() or answers[1].isChecked():
        show_correct('Жми далее')



def next_question():
    window.cur_question = window.cur_question + 1 
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q) 


def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question() 


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('КТО ТЫ ИЗ WEDNESDAY')
window.cur_question = -1    


btn_OK.clicked.connect(click_OK)



next_question()
window.resize(400, 300)
window.show()
app.exec()
