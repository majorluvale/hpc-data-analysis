FROM python:3.13-slim

WORKDIR /console-app
#copier les fichiers de notre app dans dossier du travail

COPY . /console-app/

#installer les dependances
RUN pip install -r requirements.txt

#Definir la commanda
CMD [ "python", "hpc_data.py"]