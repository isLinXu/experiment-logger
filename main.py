# import logging
# import pandas as pd
# import os
# import time
#
# class TrainLogger:
#     def __init__(self, log_file, log_level=logging.INFO):
#         self.log_file = log_file
#         self.log_level = log_level
#         self._init_logger()
#         self._init_dataframe()
#
#     def _init_logger(self):
#         self.logger = logging.getLogger(__name__)
#         self.logger.setLevel(self.log_level)
#         formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#
#         file_handler = logging.FileHandler(self.log_file)
#         file_handler.setLevel(self.log_level)
#         file_handler.setFormatter(formatter)
#
#         stream_handler = logging.StreamHandler()
#         stream_handler.setLevel(self.log_level)
#         stream_handler.setFormatter(formatter)
#
#         self.logger.addHandler(file_handler)
#         self.logger.addHandler(stream_handler)
#
#     def _init_dataframe(self):
#         if os.path.exists(self.log_file):
#             self.df = pd.read_csv(self.log_file)
#         else:
#             self.df = pd.DataFrame(columns=['timestamp', 'epoch', 'loss', 'accuracy'])
#
#     def log(self, epoch, loss, accuracy):
#         timestamp = time.time()
#         self.logger.info(f'Epoch: {epoch}, Loss: {loss}, Accuracy: {accuracy}')
#         self.df = self.df.append({'timestamp': timestamp, 'epoch': epoch, 'loss': loss, 'accuracy': accuracy}, ignore_index=True)
#
#     def save(self):
#         self.df.to_csv(self.log_file, index=False)
#
# if __name__ == '__main__':
#     logger = TrainLogger('train_log.csv')
#
#     # 假设我们进行了10轮训练
#     for epoch in range(10):
#         # 假设这里是您的模型训练过程，我们使用随机数模拟损失和准确率
#         import random
#         loss = random.random()
#         accuracy = random.random()
#
#         logger.log(epoch, loss, accuracy)
#
#     logger.save()


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
        self.df = pd.DataFrame(columns=['timestamp', 'algorithm', 'parameters', 'accuracy', 'loss'])
        self.csv_file = 'results.csv'

    def start_experiment(self, algorithm, parameters):
        self.logger.info(f'Starting experiment with algorithm: {algorithm} and parameters: {parameters}')
        self.start_time = datetime.now()

    def end_experiment(self, accuracy, loss):
        self.end_time = datetime.now()
        self.logger.info(f'Ending experiment with accuracy: {accuracy} and loss: {loss}')
        self.df = self.df._append({'timestamp': self.start_time,
                                  'algorithm': algorithm,
                                  'parameters': parameters,
                                  'accuracy': accuracy,
                                  'loss': loss}, ignore_index=True)

    def save_results(self):
        if not os.path.exists(self.csv_file):
            self.df.to_csv(self.csv_file, index=False)
        else:
            existing_df = pd.read_csv(self.csv_file)
            combined_df = pd.concat([existing_df, self.df], ignore_index=True)
            combined_df.to_csv(self.csv_file, index=False)

if __name__ == '__main__':
    # 示例使用
    experiment_logger = ExperimentLogger()

    # 开始实验
    algorithm = 'SVM'
    parameters = {'C': 1.0, 'kernel': 'linear'}
    experiment_logger.start_experiment(algorithm, parameters)

    # 结束实验
    accuracy = 0.95
    loss = 0.05
    experiment_logger.end_experiment(accuracy, loss)

    # 保存实验结果
    experiment_logger.save_results()