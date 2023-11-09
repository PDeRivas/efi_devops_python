#imagen python.
FROM python:3.9-alpine

#Copia el directorio del contenedor.
COPY . /efi_devops_python
WORKDIR /efi_devops_python

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


#expone el puerto del contenedor
EXPOSE 5005


# Define environment variables
ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0



# Make the script executable
# RUN chmod +x /sql_alchemy/run.sh

# Run the script when the container starts
CMD ["sh", "run.sh"]
# CMD ["flask", "run","--host=0.0.0.0", "--port=5005"]