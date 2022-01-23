import general

def split_file_into_mtu(filepath, mtu):
    data_fragments = []
    try:
        fd = open(filepath, "rb")
        while True:
            df = fd.read(mtu - general.IP_HEADER_LENGTH - general.UDP_HEADER_LENGTH - general.SCU_HEADER_LENGTH)
            if not df:
                break
            data_fragments.append(df)
        fd.close()
    except:
        fd.close()
        return None

    return data_fragments

def write_file(filename, data):
    with open(filename, mode='wb') as f:
        f.write(data)

def endpoint2str(addr, fileid):
    return f"{addr[0]}:{addr[1]}:{fileid}"

def fold_data(l, length):
    filedata = b""
    for i in range(0, length):
        filedata += l[i]
    return filedata
