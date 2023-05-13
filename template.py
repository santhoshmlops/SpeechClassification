import os
from pathlib import Path
import logging

logging.basicConfig(
    level= logging.INFO,
    filename="template_structure.log",
    filemode='w',
    format= '%(asctime)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

list_of_files = [
    "hate/__init__.py"
    "hate/components/__init__.py",
    "hate/components/data_ingestion.py",
    "hate/components/data_transformation.py",
    "hate/components/model_trainer.py",
    "hate/components/model_pusher.py",
    "hate/components/model_evaluation.py",
    "hate/configuration/__init__.py",
    "hate/configuration/s3_syncer.py",
    "hate/constant/__init__.py",
    "hate/constant/constant.py",
    "hate/entity/__init__.py",
    "hate/entity/artifact_entity.py",
    "hate/entity/config_entity.py",
    "hate/pipeline/__init__.py",
    "hate/pipeline/predict_pipeline.py",
    "hate/pipeline/train_pipeline.py",
    "hate/exception/__init__.py",
    "hate/exception/exception.py",
    "hate/logger/__init__.py",
    "hate/logger/logger.py",
    "hate/utils/__init__.py",
    "hate/utils/utils.py",
    "static/style.css",
    "template/index.html",
    "template/predict.html",
    "setup.py",
    "requirements.txt",
    "app.py",
    "Dockerfile",
    "Procfile"
]

for filepath in list_of_files:
    filepath = Path(filepath) 
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project Structure is completed") 
