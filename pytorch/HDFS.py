import pyhdfs
import os
import time

hdfs = pyhdfs.HdfsClient('10.10.10.1:50070')


# hdfs = pyhdfs.HdfsClient('10.10.1.1:50070')

def mkdir(remotepath):
    if not exists(remotepath):
        hdfs.mkdirs(remotepath)


def get(remotepath, localpath):
    if exists(remotepath):
        hdfs.copy_to_local(remotepath, localpath)


# load remote data
def getDir(remotepath, localpath):
    if exists(remotepath):
        dirs = hdfs.listdir(remotepath)
        for d in dirs:
            try:
                hdfs.copy_to_local(remotepath + '/' + d, localpath + '/' + d)
            except:
                getDir(remotepath + '/' + d, localpath + '/' + d)
            # hdfs.delete(remotepath+'/'+d, recursive=True)


def putDir(localfile, remotefile):
    try:
        # print(localfile)
        if exists(remotefile):
            dirs = os.listdir(localfile)
            for d in dirs:
                delete(remotefile + '/' + d)
                # print(remotefile+'/'+d)
                hdfs.copy_from_local(localfile + '/' + d, remotefile + '/' + d)
        else:
            dirs = os.listdir(localfile)
            for d in dirs:
                hdfs.copy_from_local(localfile + '/' + d, remotefile + '/' + d)
    except:
        print("Upload later.")
        time.sleep(0.5)
        putDir(localfile, remotefile)


def putOldDir(localfile, remotefile):
    if exists(remotefile):
        dirs = os.listdir(localfile)
        for d in dirs:
            hdfs.copy_from_local(localfile + '/' + d, remotefile + '/' + d)


def delDir(remotefile):
    if exists(remotefile):
        dirs = hdfs.listdir(remotefile)
        for d in dirs:
            hdfs.delete(remotefile + '/' + d, recursive=True)


def put(localfile, remotefile):
    if exists(remotefile):
        delete(remotefile)
    hdfs.copy_from_local(localfile, remotefile)


def getDirPath(filename):
    return os.path.dirname(filename)


def exists(remotepath):
    return hdfs.exists(remotepath)


def delete(remotepath):
    if exists(remotepath):
        hdfs.delete(remotepath, recursive=True)
