import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# Чтобы проект стал многостраничным, нужно в рабочей директории создать папку pages, в которой будут другие пайтон скрипты с другой логикой
# Например скрипт first_page.py, second_page.py
# Деплой в облако: чтобы постоянно не запускать проект локально (на пк), можно задеплоить приложение в облако

# Название
st.title('Data analysis application')
# Описание
st.write('Загрузка CSV файла, заполнение пропусков')

# Шаг 1. Загрузить CSV файл.
# Поместим в сайдбар
uploaded_file = st.sidebar.file_uploader('Загрузи CSV файл', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
else:
    st.stop()

# Шаг 2. Проверить наличие пропусков в файле
missed_values = df.isna().sum()
missed_values = missed_values[missed_values.apply(lambda x: x > 0)]
# st.write(missed_values)
if len(missed_values) > 0:
    fig, ax = plt.subplots()
    ax1 = sns.barplot(x=missed_values.index, y=missed_values.values)
    ax.set_title('Пропуски в столбцах')
    st.pyplot(fig)

    # Шаг 3. Заполнить пропуски
    if len(missed_values) != 0:
        button = st.button('Заполни пропуски')
        if button:
            df_filled = df[missed_values.index].copy()
            for col in df_filled.columns:
                if df_filled[col].dtype == 'object':  # Категориальный признак
                    df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
                else:  # Числовые признаки
                    df_filled[col] = df_filled[col].fillna(df_filled[col].median())
            st.write(df_filled.head(5))
            # Шаг 4. Выгрузить заполненный от пропусков CSV файл
            download_button = st.download_button(label='Скчать CSV файл',
                                                 data=df_filled.to_csv(),
                                                 file_name='filled_date.csv')
else:
    st.write('Нет пропусков в данных')
    st.stop()

# Алгоритм действий для деплоя
# 1. Провести подготовительную работу. Мы для этого создавали репозиторий. Имеется много изменений в репозитории, нужно эти изменения туда подтянуть.
# 2. Создание файла с зависимостями. pip3 freeze requirements.txt