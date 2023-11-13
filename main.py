
from exp_logger.experiment_logger import ExperimentLogger
import warnings
warnings.filterwarnings("ignore")

if __name__ == '__main__':
    experiment_logger = ExperimentLogger()

    # Image Classification
    task = 'Image Classification'
    algorithm = 'CNN'
    parameters = {'layers': 5, 'filters': [32, 64, 128, 256, 512]}
    experiment_logger.start_experiment(task, algorithm, parameters)
    metrics = {'accuracy': 0.95, 'loss': 0.05}
    experiment_logger.end_experiment(metrics)
    experiment_logger.save_results()

    # Object Detection
    task = 'Object Detection'
    algorithm = 'YOLOv5'
    parameters = {'model': 'yolov5s', 'epochs': 100, 'batch_size': 16}
    experiment_logger.start_experiment(task, algorithm, parameters)
    metrics = {'mAP': 0.75, 'precision': 0.8, 'recall': 0.7}
    experiment_logger.end_experiment(metrics)
    experiment_logger.save_results()

    # Semantic Segmentation
    task = 'Semantic Segmentation'
    algorithm = 'U-Net'
    parameters = {'layers': 4, 'filters': [64, 128, 256, 512]}
    experiment_logger.start_experiment(task, algorithm, parameters)
    metrics = {'mIoU': 0.6, 'pixel_accuracy': 0.9}
    experiment_logger.end_experiment(metrics)
    experiment_logger.save_results()

    # Natural Language Processing
    task = 'Natural Language Processing'
    algorithm = 'BERT'
    parameters = {'model': 'bert-base-uncased', 'epochs': 3, 'batch_size': 32}
    experiment_logger.start_experiment(task, algorithm, parameters)
    metrics = {'accuracy': 0.85, 'f1_score': 0.8}
    experiment_logger.end_experiment(metrics)
    experiment_logger.save_results()