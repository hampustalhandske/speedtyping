import pandas as pd
import matplotlib.pyplot as plt
import os
import io
import base64


class point_handler:

    def __init__(self) -> None:
        self.nbr_of_words = 0
        self.correct_words = 0 
        self.words_per_minute = 0
        self.words_per_secound = 0
        self.percentage = 0
    
    def update_correct_words(self):
        self.correct_words += 1
        self.update_nbr_of_words()
    
    def update_nbr_of_words(self):
        self.nbr_of_words += 1

    def reset_points(self): 
        self.nbr_of_words = 0
        self.correct_words = 0 
        self.words_per_minute = 0
        self.words_per_secound = 0
        self.percentage = 0

    def wpm(self, time):
        print(self.nbr_of_words)
        print(self.correct_words)
        self.words_per_minute = self.correct_words / (time  / 60)
        return self.words_per_minute
    
    def wps(self, time):
        self.words_per_secound = self.correct_words / (time)
        return self.words_per_secound
    
    def correct_procentage(self):
        if self.nbr_of_words == 0:
            return 0
        else:
            self.percentage = (self.correct_words/self.nbr_of_words) * 100
            return self.percentage 
        
    def final_score(self):
        wpm = self.words_per_minute
        wps = self.words_per_secound
        percentage = self.percentage
        dictionary = {
            'wpm': wpm,
            'wps': wps,
            'percentage': percentage
        }
        data_file = 'data.xlsx'
        if os.path.exists(data_file):
            df = pd.read_excel('data.xlsx', engine='openpyxl')
        else:
            df = pd.DataFrame(columns=['wpm', 'wps', 'percentage'])
        new_row = {'wpm': wpm, 'wps': wps, 'percentage': percentage}
        if all(value > 0 for value in new_row.values()):
            df.loc[len(df.index)] = new_row
        
        df.to_excel('data.xlsx', index=False)
        return dictionary
    
    def get_plot(self):
        df = pd.read_excel('data.xlsx', engine='openpyxl')
        percentage_values = df['percentage'].tolist()
        wpm_values = df['wpm'].tolist()

        row_numbers = list(range(len(df)))

        dictionary = {"percentage" : percentage_values, "wpm" : wpm_values, "nbr" : row_numbers}

        plt.plot(row_numbers, percentage_values, label='Percentage')
        plt.plot(row_numbers, wpm_values, label='WPM-values')

        plt.xlabel('order')
        plt.ylabel('Values')

        plt.legend()

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)

        img_base64 = base64.b64encode(img_buffer.read()).decode('utf-8')

        return dictionary

ph = point_handler()
ph.get_plot()