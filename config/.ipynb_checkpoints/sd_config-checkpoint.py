init_image_list=[]
init_image_list.extend([f"/root/Share/LOTUSROOM/ref/HTR_S24LOOK-{i}.jpg" for i in range(1, 31)])

sd_params = {
    'width': 860,
    'height': 860,
    'min_strength': 0.5,
    'max_strength': 0.8,
    'min_lora_weight': 0.3,
    'max_lora_weight': 1.0,
    'guidance_scale': 7.0,
    'num_inference_steps': 24,
    'init_image_list': init_image_list,
}