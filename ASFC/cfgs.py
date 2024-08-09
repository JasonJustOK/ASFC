from easydict import EasyDict as edict

model_cfg = edict()
model_cfg.name = 'model_cfg'

model_cfg.deterministic = False


model_cfg.self_info_len = 4
model_cfg.self_info_dim = 8


model_cfg.num_heads = 1
model_cfg.rr_qkv_in_dim = 3
model_cfg.rr_att_dim = 64

model_cfg.ri_qkv_in_dim = 3
model_cfg.ri_att_dim = 64


