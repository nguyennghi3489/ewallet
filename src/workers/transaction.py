import threading
from services.transaction import checkTransactionExpire

def addJob():
    threading.Timer(30.0, addJob).start()
    checkTransactionExpire()
    print("Process unfinished transaction...")

def startTransactionWorker():
    print("Worker running...")
    addJob()


    