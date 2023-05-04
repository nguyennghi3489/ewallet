from helpers.HttpRequestHandler import startServer
from workers.transaction import startTransactionWorker

if __name__ == '__main__':
    startTransactionWorker()
    startServer()