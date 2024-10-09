import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Название
st.header('Демонстрация анализа датафрейма "Чаевые в ресторане"')
st.write('##### На базе выполненной работы в jupyter notbook. Файл vis-04.ipynb')

# Шаг 1. Загрузить CSV файл.
# Поместим в сайдбар
st.write('Шаг 0. Загрузи файл для обработки')
first_step = st.checkbox('Загрузил файл')
uploaded_file = st.sidebar.file_uploader('Шаг 0. \ Загрузи CSV файл', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.stop()

if first_step == True:
    st.write('Шаг 2. Ознакомься с ДатаФреймом. (Жми виджет при каждом шаге)')
else:
    st.write('Подтверди загрузку файла')

if first_step == True:
    st.sidebar.write('Шаг 2')
    step_2 = st.sidebar.button('Проверить DataFrame')

    if step_2 == True:
        st.write(f'Количество строчек = ***{df.shape[0]}***. Количество столбцов ***{df.shape[1]}***.')

    num_of_rows = st.selectbox('Выбери количество строчек для вывода ДФ', range(1,len(df)+1))
    st.write(df.head(num_of_rows))

    st.write('Шаг 3. Создай столбец `time_order`. Заполни его случайной датой в промежутке от 2023-01-01 до 2023-01-31')
    st.sidebar.write('Шаг 3')
    step_3 = st.sidebar.button('Шаг 3. ДатаФрейм')

    if 'step_3' not in st.session_state:
        st.session_state['step_3'] = False
    if step_3 == True:
        st.session_state['step_3'] = True
    if st.session_state['step_3']:
        tips = df
        # Пример начальной и конечной даты
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 31)
        # Генерация диапазона дат с помощью pd.date_range
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        tips['time_order'] = np.random.choice(dates, size=len(tips))
        st.write(tips.head(num_of_rows))
        df = tips

    tips = df
    st.write('Шаг 4. Построй график показывающий динамику чаевых во времени')
    st.sidebar.write('Шаг 4')
    step_4 = st.sidebar.button('Шаг 4. График')
    if 'step_4' not in st.session_state:
        st.session_state['step_4'] = False
    try:
        if step_4 == True:
            st.session_state['step_4'] = True
        if st.session_state['step_4']:
            g = sns.relplot(tips, x='time_order', y='tip', kind="line", height=3, aspect=3)
            plt.xticks(rotation=90)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 5. Нарисуйте гистограмму `total_bill`')
    st.sidebar.write('Шаг 5')
    step_5 = st.sidebar.button('Шаг 5. График')
    if 'step_5' not in st.session_state:
        st.session_state['step_5'] = False
    try:
        if step_5 == True:
            st.session_state['step_5'] = True
        if st.session_state['step_5']:
            g = sns.displot(tips, x='time_order', y='total_bill', height=3, aspect=3)
            plt.xticks(rotation=90)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 6. Нарисуйте scatterplot, показывающий связь между `total_bill` and `tip`')
    st.sidebar.write('Шаг 6')
    step_6 = st.sidebar.button('Шаг 6. График')
    if 'step_6' not in st.session_state:
        st.session_state['step_6'] = False
    try:
        if step_6 == True:
            st.session_state['step_6'] = True
        if st.session_state['step_6']:
            g = sns.relplot(tips, x='tip', y='total_bill', kind='scatter', height=3, aspect=2, size='size', hue='sex')
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 7. Нарисуйте 1 график, связывающий `total_bill`, `tip`, и `size`')
    st.sidebar.write('Шаг 7')
    step_7 = st.sidebar.button('Шаг 7. График')
    if 'step_7' not in st.session_state:
        st.session_state['step_7'] = False
    try:
        if step_7 == True:
            st.session_state['step_7'] = True
        if st.session_state['step_7']:
            g = sns.jointplot(tips, x='total_bill', y='tip', height=6, hue='size')
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 8. Покажите связь между днем недели и размером счета')
    st.sidebar.write('Шаг 8')
    step_8 = st.sidebar.button('Шаг 8. График')
    if 'step_8' not in st.session_state:
        st.session_state['step_8'] = False
    try:
        if step_8 == True:
            st.session_state['step_8'] = True
        if st.session_state['step_8']:
            g = sns.catplot(tips, x='time_order', y='total_bill', kind='bar', height=3, aspect=3)
            plt.xticks(rotation=90)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 9. Нарисуйте `scatter plot` с днем недели по оси **Y**, чаевыми по оси **X**, и цветом по полу')
    st.sidebar.write('Шаг 9')
    step_9 = st.sidebar.button('Шаг 9. График')
    if 'step_9' not in st.session_state:
        st.session_state['step_9'] = False
    try:
        if step_9 == True:
            st.session_state['step_9'] = True
        if st.session_state['step_9']:
            g = sns.relplot(tips, x='tip', y='time_order', hue='sex', height=4, aspect=2)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 10. Нарисуйте `box plot` c суммой всех счетов за каждый день, разбивая по `time` (Dinner/Lunch)')
    st.sidebar.write('Шаг 10')
    step_10 = st.sidebar.button('Шаг 10. График')
    if 'step_10' not in st.session_state:
        st.session_state['step_10'] = False
    try:
        if step_10 == True:
            st.session_state['step_10'] = True
        if st.session_state['step_10']:
            g = sns.catplot(tips, x='time', y='total_bill', kind='box', height=4, aspect=2)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 11. Нарисуйте 2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали.')
    st.sidebar.write('Шаг 11')
    step_11 = st.sidebar.button('Шаг 11. График')
    if 'step_11' not in st.session_state:
        st.session_state['step_11'] = False
    try:
        if step_11 == True:
            st.session_state['step_11'] = True
        if st.session_state['step_11']:
            g = sns.relplot(tips, x='time_order', y='tip', col='time', height=3, aspect=1.5)
            g.set_xticklabels(rotation=90)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write('Шаг 12. Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали.')
    st.sidebar.write('Шаг 12')
    step_12 = st.sidebar.button('Шаг 12. График')
    if 'step_12' not in st.session_state:
        st.session_state['step_12'] = False
    try:
        if step_12 == True:
            st.session_state['step_12'] = True
        if st.session_state['step_12']:
            g = sns.relplot(tips, x='total_bill', y='tip', hue='smoker', col='sex', height=4, aspect=1)
            g.set_xticklabels(rotation=90)
            st.pyplot(g)
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)

    st.write(
        'Шаг 13. Построй тепловую карту зависимостей численных переменных')
    st.sidebar.write('Шаг 13')
    step_13 = st.sidebar.button('Шаг 13. График')
    if 'step_13' not in st.session_state:
        st.session_state['step_13'] = False
    try:
        if step_13 == True:
            st.session_state['step_13'] = True
        if st.session_state['step_13']:
            fig, ax = plt.subplots(figsize=(10,6))
            sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
            st.pyplot(fig)
            # По окончании всех графиков будет объявлена кнопка скачивания файла
            download_button = st.sidebar.download_button(label='Скчать CSV файл',
                                                         data=tips.to_csv(),
                                                         file_name='tips_after_homework.csv')
    except:
        st.write('<span style="color:red">Нажимать на этот шаг нужно после нажатия Шага 3, так как датафрейм не готов.</span>',unsafe_allow_html=True)
    st.write('---------------------')
    st.write('Очистка страницы.')
    st.write('1. Установи галочку, если хочешь очистить страницу')
    zero_step = st.checkbox('Удалить все графики')
    if zero_step == True:
        st.session_state.clear()
    st.write('2. После активации подожди, пока в правом верхнем углу завершится обработка страницы')
    st.write('3. Убери галочку')
    st.write('4. Шаг за шагом нажимай виджеты')