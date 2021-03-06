#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
from .ttypes import *
RESULTSET_TYPE_FORWARD_ONLY = 1
RESULTSET_TYPE_INSENSITIVE = 2
RESULTSET_TYPE_SENSITIVE = 3
RESULTSET_TYPE_UNKNOWN = 4
DEFAULT_AUTOCOMMIT = False
DEFAULT_RESULTSET_TYPE = 1
DEFAULT_RESULTSET_UPDATABLE = False
DEFAULT_RESULTSET_HOLD_CURSORS_OVER_COMMIT = False
DRIVER_JDBC = 1
DRIVER_ODBC = 2
DEFAULT_SESSION_TOKEN_SIZE = 16
DEFAULT_RESULTSET_BATCHSIZE = 1024
DEFAULT_LOB_CHUNKSIZE = 2097152
TRANSACTION_NONE = 0
TRANSACTION_READ_UNCOMMITTED = 1
TRANSACTION_READ_COMMITTED = 2
TRANSACTION_REPEATABLE_READ = 4
TRANSACTION_SERIALIZABLE = 8
TRANSACTION_NO_CHANGE = 64
DEFAULT_TRANSACTION_ISOLATION = 0
XA_OK = 0
XA_RDONLY = 3
XA_TMNOFLAGS = 0
XA_TMJOIN = 2097152
XA_TMENDRSCAN = 8388608
XA_TMSTARTRSCAN = 16777216
TMSUSPEND = 33554432
XA_TMSUCCESS = 67108864
XA_TMRESUME = 134217728
XA_TMFAIL = 536870912
XA_TMONEPHASE = 1073741824
COLUMN_PRECISION_UNKNOWN = 0
COLUMN_SCALE_UNKNOWN = 0
DECIMAL_MAX_PRECISION = 127
INVALID_ID = 0
NEXTRS_CLOSE_ALL_RESULTS = 0
NEXTRS_KEEP_CURRENT_RESULT = 1
NEXTRS_CLOSE_CURRENT_RESULT = 2
ROWSET_LAST_BATCH = 1
ROWSET_HAS_MORE_ROWSETS = 2
ROWSET_BEFORE_FIRST = 4
ROWSET_AFTER_LAST = 8
STATEMENT_TYPE_SELECT = 0
STATEMENT_TYPE_INSERT = 1
STATEMENT_TYPE_UPDATE = 2
STATEMENT_TYPE_DELETE = 3
STATEMENT_TYPE_CALL = 4
STATEMENT_TYPE_DDL = 5
BULK_CLOSE_RESULTSET = 1
BULK_CLOSE_LOB = 2
BULK_CLOSE_STATEMENT = 3
BULK_CLOSE_CONNECTION = 4
