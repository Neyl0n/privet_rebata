#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QPushButton, QGroupBox, QHBoxLayout, QWidget, QRadioButton, QLabel, QVBoxLayout, QMessageBox
from random import shuffle


class Questions():
    def __init__(self, quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Questions('Столица Австралии', 'Канберра', 'Мадрид', 'Оттава', 'Ниамей'))
question_list.append(Questions('Какого цвета не та флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
question_list.append(Questions('Национальной русский головной убор', 'Шапка-ушанка', 'Шляпа', 'Панама', 'Картуз'))
question_list.append(Questions('Какая автомобиль немецкого производства?', 'Мерседес', 'Шкода', 'Лада', 'Ламборгини'))
question_list.append(Questions('Столица Португалии?', 'Лиссабон', 'Оттава', 'Стамбул', 'Париж'))
question_list.append(Questions('Какая мировая религия считается самой старой?', 'Буддизм', 'Христианство', 'Ислам', 'Иудаизм'))
question_list.append(Questions('Самый сексуальный мужчина в мире?', 'Райан Гослинг', 'Джонни Депп', 'Дуэйн Джонсон', 'Вин Дизель'))
question_list.append(Questions('Лучший фильм за всю историю мира?', 'Барби', 'Аватар', 'Титаник', 'Гнев человеческий'))
question_list.append(Questions('Самая лучшая обувь?', 'Подкрадули', 'Макасины', 'Тапочки', 'Шлёпки'))
question_list.append(Questions('Что надо говорить при встрече с другом?', 'ВАААААЙ!!! Мага что за подкрадули? эиии, жиесть', 'Зравствуйте многоуважаемый товарищ, я хотел бы с вами обсудить несколько вещей', 'эуууу, иди сюда! Давай деньги. Сейчас на Барби пойдём', 'Ропопо ропопо ропопо ропопо'))
question_list.append(Questions('Что надо делать если утебя высокий рост?', 'Пьяным в канаве валяться', 'Правильно подбирать одежду', 'Идти в киномакс на Барби', 'Собирать бутылки и зарабатывать деньги на подкрадули'))
question_list.append(Questions('Лучшая игра в мире?', 'DMC 5', 'Ведьмак 3: Дикая охота', 'Дота 2', 'Майнкрафт'))
question_list.append(Questions('В каком году должен был наступить коне света?', '2012', '568', '2013', '2030'))




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')

questions = QLabel('Какой национальности не существует?')

lineh_1 = QHBoxLayout()
lineh_1.addWidget(questions )




RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чульмцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


btn = QPushButton('Ответить')

lineh_2 = QHBoxLayout()
lineh_2.addWidget(RadioGroupBox)

lineh_3 = QHBoxLayout()
lineh_3.addWidget(btn)



AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)

lineh_2.addWidget(AnsGroupBox)



line_card = QVBoxLayout()
line_card.addLayout(lineh_1)
line_card.addLayout(lineh_2)
line_card.addLayout(lineh_3)

AnsGroupBox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def test():
    if 'Ответить' == btn.text():
        show_result()
    else:
        show_questions()

btn.clicked.connect(test)



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Questions):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    questions.setText(q.quest)
    lb_Correct.setText(q.right_answer)
    show_questions()



def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        print('Всего вопросов:', main_win.total)
        print('Всего вопросов:', main_win.score)
        print('Процент правильных ответов:', main_win.score / main_win.total * 100)
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            print('Всего вопросов:', main_win.total)
            print('Всего вопросов:', main_win.score)
            print('Процент правильных ответов:', main_win.score / main_win.total * 100)
            show_correct('Неверно')


def next_question():
    main_win.cur_questions =  main_win.cur_questions + 1
    main_win.total = main_win.total + 1
    if main_win.cur_questions >= len(question_list):
        main_win.cur_questions = 0
    q = question_list[main_win.cur_questions]
    ask(q)

def click_Ok():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()



main_win = QWidget()
main_win.setLayout(line_card)
main_win.setWindowTitle('Меню card')


main_win.cur_questions = -1
main_win.total = 1  
main_win.score = 0 



btn.clicked.connect(click_Ok)




main_win.setLayout(line_card)
main_win.show()
app.exec_()

