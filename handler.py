import runpod
import time

# from comfy_script.runtime import *
# # ComfyUI server/path
# load(r'ComfyUI')  
# from comfy_script.runtime.nodes import *
# from pathlib import Path

def handler(event):
#   This function processes incoming requests to your Serverless endpoint.
#
#    Args:
#        event (dict): Contains the input data and request metadata
#       
#    Returns:
#       Any: The result to be returned to the client
    
    # Extract input data
    print(f"Worker Start")
    input = event['input']
    
    prompt = input.get('prompt')  
    seconds = input.get('seconds', 0)   

    print(f"Received prompt is hahaha: {prompt}")
    print(f"Sleeping for {seconds} seconds...")

    # output_path = Path('images/sc2.png')

    # with Workflow(wait=True):
    #   clip = CLIPLoader(clip_name='qwen_3_4b.safetensors', type='lumina2', device='default')

    #   model = UNETLoader('z_image_turbo_bf16.safetensors', 'default')
    #   model = ModelSamplingAuraFlow(model, 3)

    #   vae = VAELoader('ae.safetensors')
    

    #   conditioning = CLIPTextEncode('''a girl kiss a cat''', clip)
    #   conditioning2 = ConditioningZeroOut(conditioning)
    #   latent = EmptySD3LatentImage(width=544, height=960, batch_size=4)
    #   latent = KSampler(model=model, seed=611015986142011, steps=9, cfg=1, sampler_name='res_multistep', scheduler='simple', positive=conditioning, negative=conditioning2, latent_image=latent, denoise=1)
   
    #   image = VAEDecode(latent, vae)
    #   images = util.get_images(image)
    
    # output_path.parent.mkdir(parents=True, exist_ok=True)
    # if len(images) == 1:
    #   images[0].save(output_path)
    # else:
    #   for index, generated_image in enumerate(images, start=1):
    #       numbered_path = output_path.with_name(f'{output_path.stem}_{index:03d}{output_path.suffix}')
    #       generated_image.save(numbered_path)


    
    # You can replace this sleep call with your own Python code
    # time.sleep(seconds)  
    
    # file_path = r'D:/workspace/PythonProjects/runpod_serverless/models/diffusion_models/cmd.txt'
    file_path = r'/runpod-volume/models/diffusion_models/cmd.txt'

    try:
    # 使用 with 语句打开文件，它会在操作完成后自动关闭文件
    # encoding='utf-8' 参数用于正确读取包含中文等字符的文件，防止乱码
      with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # 读取文件的全部内容
        # print(content)         # 打印文件内容
    except FileNotFoundError:
      content = "错误：找不到文件，请检查路径 '{file_path}' 是否正确。"
    except UnicodeDecodeError:
      content = "错误：文件编码错误，请尝试使用其他编码（如 'gbk'）。"

    return "hi, yjia007, you prompt is : " + content 

# Start the Serverless function when the script is run
if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })