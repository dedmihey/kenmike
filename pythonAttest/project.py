import os
import json
import pandas as pd


class PriceMachine():

    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, file_path=''):
        '''
            Сканирует указанный каталог. Ищет файлы со словом price в названии.
            В файле ищет столбцы с названием товара, ценой и весом.
            Допустимые названия для столбца с товаром:
                товар
                название
                наименование
                продукт
                
            Допустимые названия для столбца с ценой:
                розница
                цена
                
            Допустимые названия для столбца с весом (в кг.)
                вес
                масса
                фасовка
        '''
        global df_1, df_2, df_3
        directory = 'analiseprice'
        file_path = 'price'
        filtered_files = [f for f in os.listdir(directory) if file_path in f]
        print(filtered_files)
        name = ['товар', 'название', 'наименование', 'продукт']
        price = ['розница', 'цена']
        weight = ['вес', 'масса', 'фасовка']
        for fname in filtered_files:
            df = pd.read_csv(directory + '\\' + fname)
            for i in name:
                if i in df:
                    df = df.rename(columns={i: 'наименование'})
            for j in price:
                if j in df:
                    df = df.rename(columns={j: 'цена'})
            for k in weight:
                if k in df:
                    df = df.rename(columns={k: 'вес'})
            df_concat = df[['наименование', 'цена', 'вес']]
            # print(df_concat)
            df_concat['цена за кг'] = df_concat['цена']/df_concat['вес']
            df_concat.insert(3, 'файл', fname)
            # print(df_concat)
            self.data.append(df_concat)
        df_sum = pd.concat(self.data)
        df_sum = df_sum.sort_values(by='цена за кг', ascending=True)
        df_sum['наименование'] = df_sum['наименование'].str.lower()
        #print(df_sum)
        result = df_sum.to_html()
        print(result)
        return (df_sum)

    # def _search_product_price_weight(self, headers):
    #     '''
    #         Возвращает номера столбцов
    #     '''

    # def export_to_html(self, fname='output.html'):
    #     result = '''
    #     <!DOCTYPE html>
    #     <html>
    #     <head>
    #         <title>Позиции продуктов</title>
    #     </head>
    #     <body>
    #         <table>
    #             <tr>
    #                 <th>Номер</th>
    #                 <th>Наименование</th>
    #                 <th>Цена</th>
    #                 <th>Вес</th>
    #                 <th>Файл</th>
    #                 <th>Цена за кг.</th>
    #             </tr>
    #     '''

    def find_text(self, df_sum):
        while True:
            text = input("Введите фрагмент наименования товара для поиска или exit для выхода: ").lower()
            if text == 'exit':
                break
            filtered_df = df_sum[df_sum['наименование'].str.contains(text)]
            if filtered_df['наименование'].count() != 0:
                print(filtered_df)
            else:
                print('Ничего не найдено')


pm = PriceMachine()
my_df_sum = pm.load_prices()
print(my_df_sum)

'''
    Логика работы программы
    Считываем файлы .csv с фрагментом 'price' в названии, преобразуя их в DataFrame.
    Просматриваем возможные варианты названия столбцов и переименовываем их для однообразия.
    Из переименованных столбцов образуем новый DataFrame.
    Добавляем в новый DataFrame столбцы "Цена за кг" и "Файл".
    HTML-вариант вывода организуем при помощи метода .to_html.
    Предлагаем пользователю для поиска ввести фрагмент наименования или exit для выхода.
    Если введённый фрагмент отсутствует, то выводим "Ничего не найдено".
    Все наименования и вводимый пользователем текст переведены в нижний регистр во избежание 
    чувствительности к регистру.
      
'''
pm.find_text(my_df_sum)
print('the end')
# print(pm.export_to_html())
