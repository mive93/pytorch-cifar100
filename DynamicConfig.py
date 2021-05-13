import yaml
import os
import sys, getopt

class DynamicConfig:
    def __init__(self, config_file= ""):
        if config_file == "":
            # default values
            self.network = "mobilenet"          # network to use
            self.adaptive_patience = True       # maximum patience since last minimum val loss value
            self.patience_decay = 2             # decay of patience, if adaptative
            self.max_patience = 15              # maximum batchsize allowed by the GPU in use
            self.max_batch_size = 2000          # maximum batchsize allowed by the GPU in use
            self.custom_logic = True            # use cutom logic
            self.lra_dis = False                # disable Learning rate Annealing
            self.ibs_dis = True                 # disable Incremental Batch size
            self.using_lra = True               # using learning rate annealing if True, incremental batch size if False in the current iteration
            self.altern = False                 # If altern is set to true, both logics are active and alterned
            self.finish_epochs = False          # complete all the epochs, even if patience is 0
            self.max_custom_iter = 3            # maximum iteration of custom logic
            self.lra_decay = 0.2                # learning rate annealing decay
            self.ibs_increment = 2              # incremental batch size increment
            self.fixed_scheduling_lr = False    # scheduling of learning rate activate at milestones
            self.fixed_scheduling_bs = False    # scheduling of batch size activate at milestones

        else:
            with open(config_file, "r") as c_file:
                try:
                    read_config = yaml.safe_load(c_file)
                except yaml.YAMLError as exc:
                    print(exc)

                self.network = read_config["NETWORK"]
                self.adaptive_patience = read_config["ADAPTIVE_PATIENCE"]
                self.patience_decay = read_config["PATENCE_DECAY"]
                self.max_patience = read_config["MAX_PATIENCE"]
                self.max_batch_size = read_config["MAX_BATCH_SIZE"]
                self.custom_logic = read_config["CUSTOM_LOGIC"]
                self.lra_dis = read_config["LRA_DIS"]
                self.ibs_dis = read_config["IBS_DIS"]
                self.using_lra = read_config["USING_LRA"]
                self.altern = read_config["ALTERN"]
                self.finish_epochs = read_config["FINISH_EPOCHS"]
                self.max_custom_iter = read_config["MAX_CUSTOM_ITER"]
                self.lra_decay = read_config["LRA_DECAY"]
                self.ibs_increment = read_config["IBS_INCREMENT"]
                self.fixed_scheduling_lr = read_config["FIXED_SCHEDULING_LR"]
                self.fixed_scheduling_bs = read_config["FIXED_SCHEDULING_BS"]

        print("network", self.network, end=", ")
        print("adaptive_patience", self.adaptive_patience, end=", ")
        print("patence_decay", self.patience_decay, end=", ")
        print("max_patience", self.max_patience, end=", ")
        print("max_batch_size", self.max_batch_size, end=", ")
        print("custom_logic", self.custom_logic, end=", ")
        print("lra_dis", self.lra_dis, end=", ")
        print("ibs_dis", self.ibs_dis, end=", ")
        print("using_lra", self.using_lra, end=", ")
        print("altern", self.altern, end=", ")
        print("finish_epochs", self.finish_epochs, end=", ")
        print("max_custom_iter", self.max_custom_iter, end=", ")
        print("lra_decay", self.lra_decay, end=", ")
        print("ibs_increment", self.ibs_increment, end=", ")
        print("fixed_scheduling_lr", self.fixed_scheduling_lr, end=", ")
        print("fixed_scheduling_bs", self.fixed_scheduling_bs)

