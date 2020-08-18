##data##
path = '/data/luomingshuang/lms_codes/GE2E_SV_encoder_lms_pytorch/source_speakers'
sr = 16000
window = 0.025 #(s)=25ms
hop = 0.01 #(s)=10ms
nmels = 40
tisv_frame = 300
nfft = 512

##model##
hidden_dim = 512
num_layers = 3
proj_dim = 256

##train##
device = 'cuda'
trn_speakers = 5 #number of speakers in every batch
trn_utterances = 5  #number of utterances per speaker
trn_epochs = 10000000000
lr = 0.01
trn_num_worker = 0
log_interval = 30
log_file = 'train_states'
save_dir = 'weights'

propotion = 0.1

weights = 'weights/epoch_300_iteration_162239_EER_0.07879628986120224.pth'

##test##
tst_speakers = 4
tst_utterances = 6
tst_num_worker = 8
tst_epochs = 10
