import torch
from math import log2

START_TRAIN_AT_IMG_SIZE = 256
DATASET = 'succulents'
CHECKPOINT_GEN = "generator.pth"
CHECKPOINT_CRITIC = "critic.pth"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SAVE_MODEL = True
LOAD_MODEL = True
GENERATE_EXAMPLE = True
LEARNING_RATE = 1e-3
BATCH_SIZES = [16, 16, 16, 16, 8, 8, 8, 8, 4]  # Change based on your vRAM
CHANNELS_IMG = 3
Z_DIM = 256  # should be 512 in original paper
IN_CHANNELS = 256  # should be 512 in original paper
CRITIC_ITERATIONS = 1
LAMBDA_GP = 10
PROGRESSIVE_EPOCHS = [20] * len(BATCH_SIZES)   # Change based on your vRAM
FIXED_NOISE = torch.randn(8, Z_DIM, 1, 1).to(DEVICE)
NUM_WORKERS = 1