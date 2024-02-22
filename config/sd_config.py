init_image_list=[]
sd_params = {
    'width': 860,
    'height': 860,
    'min_strength': 0.63,
    'max_strength': 0.95,
    'min_lora_weight': 0.7,
    'max_lora_weight': 1.0,
    'guidance_scale': 7.0,
    'num_inference_steps': 20,
    'init_image_list': init_image_list.extend([f"/root/Share/LOTUSROOM/ref/HTR_S24LOOK-{i}.jpg" for i in range(1, 31)])
}