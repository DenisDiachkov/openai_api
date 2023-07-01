FROM continuumio/miniconda3
RUN pip install openai==0.27.8
RUN pip install flask==2.3.2
RUN pip install pillow
COPY . /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN echo "source activate base" > ~/.bashrc

ENV PATH /opt/conda/envs/base/bin:$PATH
