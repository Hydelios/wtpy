# config.py
import os

# 当前文件路径（假设 config.py 和 common 是同级）
base_path = os.path.dirname(os.path.abspath(__file__))

# 通用目录
common_path = os.path.join(base_path, "common")
strategies_path = os.path.join(base_path, "Strategies")
storage_path = os.path.join(base_path, "storage")

# 配置文件路径
project = "cta_fut_bt"
# project = "cta_stk_bt"
# project = "hft_fut"
cfg_path = os.path.join(base_path, f"{project}/configbt.yaml")  # 可根据你的真实路径调整

# JSON 配置文件路径（自动生成）
commodities_path     = os.path.join(common_path, "commodities.json")
contracts_path       = os.path.join(common_path, "contracts.json")
etfs_path            = os.path.join(common_path, "etfs.json")
etf_comms_path       = os.path.join(common_path, "etf_comms.json")
fees_path            = os.path.join(common_path, "fees.json")
fees_stk_path        = os.path.join(common_path, "fees_stk.json")
fopt_comms_path      = os.path.join(common_path, "fopt_comms.json")
fut_options_path     = os.path.join(common_path, "fut_options.json")
holidays_path        = os.path.join(common_path, "holidays.json")
hots_path            = os.path.join(common_path, "hots.json")
ifopt_comms_path     = os.path.join(common_path, "ifopt_comms.json")
if_options_path      = os.path.join(common_path, "if_options.json")
seconds_path         = os.path.join(common_path, "seconds.json")
sessions_path        = os.path.join(common_path, "sessions.json")
sopt_comms_path      = os.path.join(common_path, "sopt_comms.json")
stk_comms_path       = os.path.join(common_path, "stk_comms.json")
stk_options_path     = os.path.join(common_path, "stk_options.json")
stk_sessions_path    = os.path.join(common_path, "stk_sessions.json")
stocks_path          = os.path.join(common_path, "stocks.json")
