import logging
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

class ExperimentLogger:
    def __init__(self, log_file='experiment.log', log_level=logging.INFO, log_format=None, output_format='csv'):
        self.log_file = log_file
        self.log_level = log_level
        self.log_format = log_format if log_format else '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.output_format = output_format
        self.logger = logging.getLogger('ExperimentLogger')
        self.logger.setLevel(self.log_level)
        file_handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter(self.log_format)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.df = pd.DataFrame(columns=['timestamp', 'task', 'algorithm', 'parameters'])
        self.csv_file = 'results.csv'
        self.json_file = 'results.json'

    def start_experiment(self, task, algorithm, parameters):
        self.logger.info(f'Starting experiment with task: {task}, algorithm: {algorithm} and parameters: {parameters}')
        self.start_time = datetime.now()
        self.task = task
        self.algorithm = algorithm
        self.parameters = parameters

    def end_experiment(self, metrics):
        self.end_time = datetime.now()
        self.logger.info(f'Ending experiment with metrics: {metrics}')
        experiment_data = {'timestamp': self.start_time,
                           'task': self.task,
                           'algorithm': self.algorithm,
                           'parameters': self.parameters}
        experiment_data.update(metrics)  # 将指标添加到实验数据中
        self.df = self.df._append(experiment_data, ignore_index=True)

    def save_results(self):
        if self.output_format == 'csv':
            self._save_csv()
        elif self.output_format == 'json':
            self._save_json()
        else:
            raise ValueError(f'Unsupported output format: {self.output_format}')

    def _save_csv(self):
        if not os.path.exists(self.csv_file):
            self.df.to_csv(self.csv_file, index=False)
        else:
            existing_df = pd.read_csv(self.csv_file)
            combined_df = pd.concat([existing_df, self.df], ignore_index=True)
            combined_df.to_csv(self.csv_file, index=False)

    def _save_json(self):
        if not os.path.exists(self.json_file):
            self.df.to_json(self.json_file, orient='records')
        else:
            existing_df = pd.read_json(self.json_file)
            combined_df = pd.concat([existing_df, self.df], ignore_index=True)
            combined_df.to_json(self.json_file, orient='records')

    def plot_results(self, metric, xlabel=None, ylabel=None, title=None):
        sns.set(style="whitegrid")
        plt.figure(figsize=(12, 6))
        sns.barplot(x='algorithm', y=metric, data=self.df)
        plt.xlabel(xlabel if xlabel else 'Algorithm')
        plt.ylabel(ylabel if ylabel else metric.capitalize())
        plt.title(title if title else f'{metric.capitalize()} by Algorithm')
        plt.show()