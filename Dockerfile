

FROM pytorch/pytorch:2.4.1-cuda12.1-cudnn9-devel
ENV DEBIAN_FRONTEND=noninteractive
ENV FORCE_CUDA="1"
ENV MMCV_WITH_OPS=1
ENV TORCH_CUDA_ARCH_LIST="8.0"

ARG PIP_EXTRA_INDEX_URL

RUN apt update && \
    apt install -y bash \
    build-essential \
    git \
    git-lfs \
    curl \
    ca-certificates \
    libsndfile1-dev \
    wget \
    ffmpeg libsm6 libxext6 &&\
    rm -rf /var/lib/apt/lists

RUN python3 -m pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY . /app


# jupyter lab --no-browser --ip 0.0.0.0 --port 2233 --allow-root --notebook-dir=.
