FROM python:3.10-slim

WORKDIR /

# 1. 先将本地的 ComfyUI 目录拷贝到镜像的 /ComfyUI 路径下
# 假设你的项目结构是：项目根目录/ComfyUI/requirements.txt
COPY ComfyUI /ComfyUI

# Install dependencies
RUN pip install --no-cache-dir runpod
# RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130
# RUN pip install -r ComfyUI/requirements.txt 
# RUN pip install -U "comfy-script[default]"

# Copy your handler file
COPY handler.py /

# Start the container
CMD ["python3", "-u", "handler.py"]