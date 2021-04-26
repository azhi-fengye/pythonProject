host = None,  # 要连接的主机地址
user = None,  # 用于登录的数据库用户
password = '',  # 密码
database = None,  # 要连接的数据库
port = 0,  # 端口，一般为 3306
unix_socket = None,  # 选择是否要用unix_socket而不是TCP/IP
charset = '',  # 字符编码
sql_mode = None,  # Default SQL_MODE to use.
read_default_file = None,  # 从默认配置文件(my.ini或my.cnf)中读取参数
conv = None,  # 转换字典
use_unicode = None,  # 是否使用 unicode 编码
client_flag = 0,  # Custom flags to send to MySQL. Find potential values in constants.CLIENT.
cursorclass = <

class <'pymysql.cursors.Cursor' >,  # 选择 Cursor 类型


init_command = None,  # 连接建立时运行的初始语句
connect_timeout = 10,  # 连接超时时间，(default: 10, min: 1, max: 31536000)
ssl = None,  # A dict of arguments similar to mysql_ssl_set()'s parameters.For now the capath and cipher arguments are not supported.
read_default_group = None,  # Group to read from in the configuration file.
compress = None,  # 不支持
named_pipe = None,  # 不支持
no_delay = None,  #
autocommit = False,  # 是否自动提交事务
db = None,  # 同 database，为了兼容 MySQLdb
passwd = None,  # 同 password，为了兼容 MySQLdb
local_infile = False,  # 是否允许载入本地文件
max_allowed_packet = 16777216,  # 限制 `LOCAL DATA INFILE` 大小
defer_connect = False,  # Don't explicitly connect on contruction - wait for connect call.
auth_plugin_map = {},  #
read_timeout = None,  #
write_timeout = None,
bind_address = None  # 当客户有多个网络接口，指定一个连接到主机
