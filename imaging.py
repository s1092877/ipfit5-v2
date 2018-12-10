with open("/dev/sda",'rb') as f:
    with open("~/imagingtest.dd", "wb") as i:
        while True:
            if i.write(f.read(512)) == 0:
                break