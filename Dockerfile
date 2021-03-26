FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WorkDIR ./API /API
COPY  requirements.txt  requirements.txt

RUN pip3 install -r requirements.txt
COPY . .


#EXPOSE 8800:800
CMD ["uvicorn", "API.main:app"]



