# 必填字段

# TG 对话 ID
TG_CHAT_ID = ''
# TG 机器人 Token
TG_BOT_TOKEN = ''

# 可选字段：关于代理的配置

# 是否使用代理 1 是 | 0 否
USE_PROXY = 0
# 访问 Dmm 是否使用代理 1 是 | 0 否 （该字段的值由自己决定，与 USE_PROXY 无关）
USE_PROXY_DMM = 0
# 如果不使用代理，以下三个字段不用管
# 代理类型 http | socks5 | socks4
PROXY_SCHEME = 'http'
# IP 地址
PROXY_ADDR_HOST = '127.0.0.1'
# 端口地址
PROXY_ADDR_PORT = '7890'

# 可选字段：关于自动发送磁链到 Pikpak 的配置

# 是否使用 Pikpak 自动发送功能 1 是 | 0 否
USE_PIKPAK = 0
# 如果不使用 Pikpak 自动发送功能，以下两个字段不用管（在这里申请 API：https://my.telegram.org/apps）
# TG API ID
TG_API_ID = ''
# TG API HASH
TG_API_HASH = ''