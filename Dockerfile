FROM python:3.10-slim

WORKDIR /

# 1. 先将本地的 ComfyUI 目录拷贝到镜像的 /ComfyUI 路径下
# 假设你的项目结构是：项目根目录/ComfyUI/requirements.txt
COPY ComfyUI /ComfyUI

# Install dependencies
RUN pip install --no-cache-dir runpod
# RUN pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130

# RUN pip install torch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 --index-url https://download.pytorch.org/whl/cu118

# --- 关键修改：升级到 PyTorch 2.3.0 ---
# 这个版本既包含了 float8_e4m3fn 支持，又通常兼容旧驱动 (470+)
# 注意：使用 cu118 源，不要用 nightly 源，否则可能拉到 CUDA 12 的包
RUN pip install torch==2.3.0 torchvision==0.18.0 torchaudio==2.3.0 --index-url https://download.pytorch.org/whl/cu118


RUN pip install -r ComfyUI/requirements.txt 
RUN pip install -U "comfy-script[default]"

# Copy your handler file
COPY handler.py /

# Start the container
CMD ["python3", "-u", "handler.py"]