rm /home/peter/.cache/huggingface/accelerate/default_config.yaml
CUDA_VISIBLE_DEVICES=1 python accelerate_config.py
CUDA_VISIBLE_DEVICES=1 accelerate launch train.py \
  --pretrained_model_name_or_path=CompVis/stable-diffusion-v1-4  \
  --instance_data_dir=jung \
  --output_dir=output \
  --instance_prompt="a photo of face of jung" \
  --resolution=256 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --learning_rate=5e-6 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=800 \
  --enable_xformers_memory_efficient_attention
  # --train_text_encoder \
  # --class_data_dir=class_data_dir \
  # --num_class_images=200 \
  # --with_prior_preservation \
  # --prior_loss_weight=1.0 \
  # --class_prompt="a photo of face of man" \
