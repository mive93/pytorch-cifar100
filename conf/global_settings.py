""" configurations for this project

author baiyu
"""
import os
from datetime import datetime

#CIFAR100 dataset path (python version)
#CIFAR100_PATH = '/nfs/private/cifar100/cifar-100-python'

#mean and std of cifar100 dataset
CIFAR100_TRAIN_MEAN = (0.5070751592371323, 0.48654887331495095, 0.4409178433670343)
CIFAR100_TRAIN_STD = (0.2673342858792401, 0.2564384629170883, 0.27615047132568404)

#CIFAR100_TEST_MEAN = (0.5088964127604166, 0.48739301317401956, 0.44194221124387256)
#CIFAR100_TEST_STD = (0.2682515741720801, 0.2573637364478126, 0.2770957707973042)

#directory to save weights file
CHECKPOINT_PATH = 'checkpoint'

#total training epoches
EPOCH = 200
MILESTONES = [60, 120, 160]

#initial learning rate
#INIT_LR = 0.1

DATE_FORMAT = '%A_%d_%B_%Y_%Hh_%Mm_%Ss'
#time of we run the script
TIME_NOW = datetime.now().strftime(DATE_FORMAT)

#tensorboard log dir
LOG_DIR = 'runs'

#save weights file per SAVE_EPOCH epoch
SAVE_EPOCH = 10

ADAPTIVE_PATIENCE = True

# maximum patience since last minimum val loss value
MAX_PATIENCE = 15

# maximum batchsize allowed by the GPU in use
MAX_BATCH_SIZE = 2000

# use cutom logic
CUSTOM_LOGIC = True

# disable Learning rate Annealing
LRA_DIS = False

# disable Incremental Batch size
IBS_DIS = True

# using learning rate annealing if True, incremental batch size if False in the current iteration
USING_LRA = True

# If altern is set to true, both logics are active and alterned
ALTERN = False

FINISH_EPOCHS = False

# maximum iteration of custom logic
MAX_CUSTOM_ITER = 3

#maximum loss value 
MAX_LOSS = 9999999

# learning rate annealing decay
LRA_DECAY = 0.2

# incremental batch size increment
IBS_INCREMENT = 2

# scheduling of learning rate activate at milestones
FIXED_SCHEDULING_LR = False

# scheduling of batch size activate at milestones
FIXED_SCHEDULING_BS = False

