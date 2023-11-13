import logging
import pandas as pd
import os
from datetime import datetime

class ExperimentLogger:
    def __init__(self, log_file='experiment.log', log_level=logging.INFO):
        self.log_file = log_file
        self.log_level = log_level
        self.logger = logging.getLogger('ExperimentLogger')
        self.logger.setLevel(self.log_level)
        file_handler = logging.FileHandler(self.log_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.df = pd.DataFrame(columns=['timestamp', 'task', 'algorithm', 'parameters', 'metrics'])
        self.csv_file = '../results.csv'

    def start_experiment(self, task, algorithm, parameters):
        self.logger.info(f'Starting experiment with task: {task}, algorithm: {algorithm} and parameters: {parameters}')
        self.start_time = datetime.now()
        self.task = task
        self.algorithm = algorithm
        self.parameters = parameters

    def end_experiment(self, metrics):
        self.end_time = datetime.now()
        self.logger.info(f'Ending experiment with metrics: {metrics}')
        self.df = self.df._append({'timestamp': self.start_time,
                                  'task': self.task,
                                  'algorithm': self.algorithm,
                                  'parameters': self.parameters,
                                  'metrics': metrics}, ignore_index=True)

    def save_results(self):
        if not os.path.exists(self.csv_file):
            self.df.to_csv(self.csv_file, index=False)
        else:
            existing_df = pd.read_csv(self.csv_file)
            combined_df = pd.concat([existing_df, self.df], ignore_index=True)
            combined_df.to_csv(self.csv_file, index=False)