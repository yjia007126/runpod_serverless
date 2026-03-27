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
    # file_path = r'/runpod-volume/models/diffusion_models/cmd.txt'

    text_content = "这是要保存的文本内容。\nPython 文件操作非常简单！"
    file_path = r'/runpod-volume/images/new.txt'
    content = ""
    try:
      with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text_content)
        content = "save file success"
    except Exception as e:    
        # print(f"❌ 保存失败: {e}")
        content = "save file faile:"+{e}

    return "hi, yjia007, you prompt is : " + content 

# Start the Serverless function when the script is run
if __name__ == '__main__':
    runpod.serverless.start({'handler': handler })